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


class MacResponse(object):
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
        'age': 'int',
        'created_at': 'str',
        'device_name': 'str',
        'mac': 'str',
        'vlan': 'int'
    }

    attribute_map = {
        'age': 'age',
        'created_at': 'created_at',
        'device_name': 'device_name',
        'mac': 'mac',
        'vlan': 'vlan'
    }

    def __init__(self, age=None, created_at=None, device_name=None, mac=None, vlan=None):  # noqa: E501
        """MacResponse - a model defined in Swagger"""  # noqa: E501

        self._age = None
        self._created_at = None
        self._device_name = None
        self._mac = None
        self._vlan = None
        self.discriminator = None

        if age is not None:
            self.age = age
        if created_at is not None:
            self.created_at = created_at
        if device_name is not None:
            self.device_name = device_name
        if mac is not None:
            self.mac = mac
        if vlan is not None:
            self.vlan = vlan

    @property
    def age(self):
        """Gets the age of this MacResponse.  # noqa: E501


        :return: The age of this MacResponse.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this MacResponse.


        :param age: The age of this MacResponse.  # noqa: E501
        :type: int
        """

        self._age = age

    @property
    def created_at(self):
        """Gets the created_at of this MacResponse.  # noqa: E501


        :return: The created_at of this MacResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MacResponse.


        :param created_at: The created_at of this MacResponse.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def device_name(self):
        """Gets the device_name of this MacResponse.  # noqa: E501


        :return: The device_name of this MacResponse.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this MacResponse.


        :param device_name: The device_name of this MacResponse.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def mac(self):
        """Gets the mac of this MacResponse.  # noqa: E501


        :return: The mac of this MacResponse.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this MacResponse.


        :param mac: The mac of this MacResponse.  # noqa: E501
        :type: str
        """

        self._mac = mac

    @property
    def vlan(self):
        """Gets the vlan of this MacResponse.  # noqa: E501


        :return: The vlan of this MacResponse.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this MacResponse.


        :param vlan: The vlan of this MacResponse.  # noqa: E501
        :type: int
        """

        self._vlan = vlan

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
        if issubclass(MacResponse, dict):
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
        if not isinstance(other, MacResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
