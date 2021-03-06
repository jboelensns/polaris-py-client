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


class IpFilterObject(object):
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
        'description': 'str',
        'id': 'str',
        'is_enabled': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'is_enabled': 'is_enabled',
        'name': 'name'
    }

    def __init__(self, description=None, id=None, is_enabled=None, name=None):  # noqa: E501
        """IpFilterObject - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._id = None
        self._is_enabled = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_enabled is not None:
            self.is_enabled = is_enabled
        self.name = name

    @property
    def description(self):
        """Gets the description of this IpFilterObject.  # noqa: E501


        :return: The description of this IpFilterObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IpFilterObject.


        :param description: The description of this IpFilterObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this IpFilterObject.  # noqa: E501

        UUID1 string  # noqa: E501

        :return: The id of this IpFilterObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IpFilterObject.

        UUID1 string  # noqa: E501

        :param id: The id of this IpFilterObject.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_enabled(self):
        """Gets the is_enabled of this IpFilterObject.  # noqa: E501


        :return: The is_enabled of this IpFilterObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this IpFilterObject.


        :param is_enabled: The is_enabled of this IpFilterObject.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def name(self):
        """Gets the name of this IpFilterObject.  # noqa: E501


        :return: The name of this IpFilterObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IpFilterObject.


        :param name: The name of this IpFilterObject.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(IpFilterObject, dict):
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
        if not isinstance(other, IpFilterObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
