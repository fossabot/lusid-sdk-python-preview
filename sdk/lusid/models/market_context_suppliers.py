# coding: utf-8

"""
    LUSID API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.10.1389
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class MarketContextSuppliers(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'commodity': 'str',
        'credit': 'str',
        'equity': 'str',
        'fx': 'str',
        'rates': 'str'
    }

    attribute_map = {
        'commodity': 'Commodity',
        'credit': 'Credit',
        'equity': 'Equity',
        'fx': 'Fx',
        'rates': 'Rates'
    }

    required_map = {
        'commodity': 'optional',
        'credit': 'optional',
        'equity': 'optional',
        'fx': 'optional',
        'rates': 'optional'
    }

    def __init__(self, commodity=None, credit=None, equity=None, fx=None, rates=None):  # noqa: E501
        """
        MarketContextSuppliers - a model defined in OpenAPI

        :param commodity: 
        :type commodity: str
        :param credit: 
        :type credit: str
        :param equity: 
        :type equity: str
        :param fx: 
        :type fx: str
        :param rates: 
        :type rates: str

        """  # noqa: E501

        self._commodity = None
        self._credit = None
        self._equity = None
        self._fx = None
        self._rates = None
        self.discriminator = None

        if commodity is not None:
            self.commodity = commodity
        if credit is not None:
            self.credit = credit
        if equity is not None:
            self.equity = equity
        if fx is not None:
            self.fx = fx
        if rates is not None:
            self.rates = rates

    @property
    def commodity(self):
        """Gets the commodity of this MarketContextSuppliers.  # noqa: E501


        :return: The commodity of this MarketContextSuppliers.  # noqa: E501
        :rtype: str
        """
        return self._commodity

    @commodity.setter
    def commodity(self, commodity):
        """Sets the commodity of this MarketContextSuppliers.


        :param commodity: The commodity of this MarketContextSuppliers.  # noqa: E501
        :type: str
        """
        allowed_values = ["DataScope", "Lusid", "Isda", "Client", "Edi", "TraderMade", "FactSet"]  # noqa: E501
        if commodity not in allowed_values:
            raise ValueError(
                "Invalid value for `commodity` ({0}), must be one of {1}"  # noqa: E501
                .format(commodity, allowed_values)
            )

        self._commodity = commodity

    @property
    def credit(self):
        """Gets the credit of this MarketContextSuppliers.  # noqa: E501


        :return: The credit of this MarketContextSuppliers.  # noqa: E501
        :rtype: str
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this MarketContextSuppliers.


        :param credit: The credit of this MarketContextSuppliers.  # noqa: E501
        :type: str
        """
        allowed_values = ["DataScope", "Lusid", "Isda", "Client", "Edi", "TraderMade", "FactSet"]  # noqa: E501
        if credit not in allowed_values:
            raise ValueError(
                "Invalid value for `credit` ({0}), must be one of {1}"  # noqa: E501
                .format(credit, allowed_values)
            )

        self._credit = credit

    @property
    def equity(self):
        """Gets the equity of this MarketContextSuppliers.  # noqa: E501


        :return: The equity of this MarketContextSuppliers.  # noqa: E501
        :rtype: str
        """
        return self._equity

    @equity.setter
    def equity(self, equity):
        """Sets the equity of this MarketContextSuppliers.


        :param equity: The equity of this MarketContextSuppliers.  # noqa: E501
        :type: str
        """
        allowed_values = ["DataScope", "Lusid", "Isda", "Client", "Edi", "TraderMade", "FactSet"]  # noqa: E501
        if equity not in allowed_values:
            raise ValueError(
                "Invalid value for `equity` ({0}), must be one of {1}"  # noqa: E501
                .format(equity, allowed_values)
            )

        self._equity = equity

    @property
    def fx(self):
        """Gets the fx of this MarketContextSuppliers.  # noqa: E501


        :return: The fx of this MarketContextSuppliers.  # noqa: E501
        :rtype: str
        """
        return self._fx

    @fx.setter
    def fx(self, fx):
        """Sets the fx of this MarketContextSuppliers.


        :param fx: The fx of this MarketContextSuppliers.  # noqa: E501
        :type: str
        """
        allowed_values = ["DataScope", "Lusid", "Isda", "Client", "Edi", "TraderMade", "FactSet"]  # noqa: E501
        if fx not in allowed_values:
            raise ValueError(
                "Invalid value for `fx` ({0}), must be one of {1}"  # noqa: E501
                .format(fx, allowed_values)
            )

        self._fx = fx

    @property
    def rates(self):
        """Gets the rates of this MarketContextSuppliers.  # noqa: E501


        :return: The rates of this MarketContextSuppliers.  # noqa: E501
        :rtype: str
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this MarketContextSuppliers.


        :param rates: The rates of this MarketContextSuppliers.  # noqa: E501
        :type: str
        """
        allowed_values = ["DataScope", "Lusid", "Isda", "Client", "Edi", "TraderMade", "FactSet"]  # noqa: E501
        if rates not in allowed_values:
            raise ValueError(
                "Invalid value for `rates` ({0}), must be one of {1}"  # noqa: E501
                .format(rates, allowed_values)
            )

        self._rates = rates

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MarketContextSuppliers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
