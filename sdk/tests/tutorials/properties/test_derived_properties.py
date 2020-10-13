import unittest
import logging
import json

import lusid

import lusid.models as models
from utilities import InstrumentLoader
from utilities import TestDataUtilities


class DerivedPropertyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()
        cls.scopes_api = lusid.ScopesApi(api_client)
        cls.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        # load instruments from InstrumentLoader
        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = instrument_loader.load_instruments()
        # setup logging configuration
        logging.basicConfig(level=logging.INFO)

    def create_ratings_property(self, *ratings):

        ratings = [*ratings]

        for rating in ratings:
            property_definition = models.CreatePropertyDefinitionRequest(
                domain="Instrument",
                scope="Test-Demo",
                code=f"{rating}Rating",
                display_name=f"{rating}Rating",
                data_type_id=lusid.ResourceId(scope="system", code="number"),
            )

            try:
                # create property definition
                self.property_definitions_api.create_property_definition(
                    create_property_definition_request=property_definition
                )
            except lusid.ApiException as e:
                if json.loads(e.body)["name"] == "PropertyAlreadyExists":
                    logging.info(f"Property {rating} already exists")
                    pass

    def upsert_ratings_property(self, figi, fitch_value=None, moodys_value=None):

        properties = {
            "Instrument/Test-Demo/FitchRating": fitch_value,
            "Instrument/Test-Demo/MoodysRating": moodys_value,
        }

        # upsert property definition
        for key in properties:
            if properties[key] is not None:
                property_request = [
                    models.UpsertInstrumentPropertyRequest(
                        identifier_type="Figi",
                        identifier=figi,
                        properties=[
                            models.ModelProperty(
                                key=key,
                                value=models.PropertyValue(
                                    metric_value=models.MetricValue(
                                        value=properties[key]
                                    )
                                ),
                            )
                        ],
                    )
                ]

                self.instruments_api.upsert_instruments_properties(
                    upsert_instrument_property_request=property_request
                )

    def get_instruments_with_derived_prop(self, Figi):
        response = self.instruments_api.list_instruments(
            instrument_property_keys=["Instrument/Test-Demo/TestDerivedRating"],
            filter=f"Identifiers[Figi] eq '{Figi}'",
        )

        return response.values[0].properties[0].value.metric_value.value

    def get_instruments_func(self, Figi):
        response = self.instruments_api.get_instruments(
            identifier_type="Figi", request_body=[Figi]
        )
        return response

    def test_derived_property(self):

        self.create_ratings_property("Fitch", "Moodys")

        # create instrument property edge cases and upsert (using arbitrary numeric ratings)
        self.upsert_ratings_property("BBG000FD8G46", fitch_value=10, moodys_value=5)
        self.upsert_ratings_property("BBG000DW76R4")
        self.upsert_ratings_property("BBG000PQKVN8", moodys_value=5)
        self.upsert_ratings_property("BBG000BDWPY0", fitch_value=10)

        # create derived property using the 'Coalesce' derivation formula
        derivation_formula = "Coalesce(Properties[Instrument/Test-Demo/MoodysRating], Properties[Instrument/Test-Demo/FitchRating],0)"

        # create derived property request
        derived_prop_definition_req = models.CreateDerivedPropertyDefinitionRequest(
            domain="Instrument",
            scope="Test-Demo",
            code="TestDerivedRating",
            display_name="TestDerivedRating",
            data_type_id=lusid.ResourceId(scope="system", code="number"),
            derivation_formula=derivation_formula,
        )

        try:
            # create property definition
            self.property_definitions_api.create_derived_property_definition(
                derived_prop_definition_req
            )
        except lusid.ApiException as e:
            if json.loads(e.body)["name"] == "PropertyAlreadyExists":
                logging.info("Property 'derived' already exists")
                pass

        # test case for derived property with both ratings
        both_ratings = self.get_instruments_with_derived_prop("BBG000FD8G46")
        self.assertEqual(both_ratings, 5.0)

        # test case for derived property with no ratings
        no_ratings = self.get_instruments_with_derived_prop("BBG000DW76R4")
        self.assertEqual(no_ratings, 0.0)

        # test case for derived property with fitch only
        fitch_only = self.get_instruments_with_derived_prop("BBG000BDWPY0")
        self.assertEqual(fitch_only, 10.0)

        # test case for derived property with moodys only
        moodys_only = self.get_instruments_with_derived_prop("BBG000PQKVN8")
        self.assertEqual(moodys_only, 5.0)


if __name__ == "__main__":
    unittest.main()
