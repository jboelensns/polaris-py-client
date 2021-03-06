# coding: utf-8

"""
    Polaris API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Body7(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'canonical': 'str',
        'comment': 'str',
        'fqdn': 'str',
        'ttl': 'int',
        'view': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'canonical': 'canonical',
        'comment': 'comment',
        'fqdn': 'fqdn',
        'ttl': 'ttl',
        'view': 'view',
        'zone': 'zone'
    }

    def __init__(self, canonical=None, comment=None, fqdn=None, ttl=None, view=None, zone=None):  # noqa: E501
        """Body7 - a model defined in Swagger"""  # noqa: E501

        self._canonical = None
        self._comment = None
        self._fqdn = None
        self._ttl = None
        self._view = None
        self._zone = None
        self.discriminator = None

        self.canonical = canonical
        if comment is not None:
            self.comment = comment
        self.fqdn = fqdn
        if ttl is not None:
            self.ttl = ttl
        if view is not None:
            self.view = view
        if zone is not None:
            self.zone = zone

    @property
    def canonical(self):
        """Gets the canonical of this Body7.  # noqa: E501


        :return: The canonical of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._canonical

    @canonical.setter
    def canonical(self, canonical):
        """Sets the canonical of this Body7.


        :param canonical: The canonical of this Body7.  # noqa: E501
        :type: str
        """
        if canonical is None:
            raise ValueError("Invalid value for `canonical`, must not be `None`")  # noqa: E501

        self._canonical = canonical

    @property
    def comment(self):
        """Gets the comment of this Body7.  # noqa: E501


        :return: The comment of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Body7.


        :param comment: The comment of this Body7.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def fqdn(self):
        """Gets the fqdn of this Body7.  # noqa: E501


        :return: The fqdn of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this Body7.


        :param fqdn: The fqdn of this Body7.  # noqa: E501
        :type: str
        """
        if fqdn is None:
            raise ValueError("Invalid value for `fqdn`, must not be `None`")  # noqa: E501

        self._fqdn = fqdn

    @property
    def ttl(self):
        """Gets the ttl of this Body7.  # noqa: E501


        :return: The ttl of this Body7.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this Body7.


        :param ttl: The ttl of this Body7.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

    @property
    def view(self):
        """Gets the view of this Body7.  # noqa: E501


        :return: The view of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this Body7.


        :param view: The view of this Body7.  # noqa: E501
        :type: str
        """

        self._view = view

    @property
    def zone(self):
        """Gets the zone of this Body7.  # noqa: E501


        :return: The zone of this Body7.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this Body7.


        :param zone: The zone of this Body7.  # noqa: E501
        :type: str
        """

        self._zone = zone

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Body7, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body7):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
