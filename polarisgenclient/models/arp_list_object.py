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


class ArpListObject(object):
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
        'address': 'str',
        'device_name': 'str',
        'is_agent_cache': 'bool',
        'mac': 'str',
        'port': 'str'
    }

    attribute_map = {
        'address': 'address',
        'device_name': 'device_name',
        'is_agent_cache': 'is_agent_cache',
        'mac': 'mac',
        'port': 'port'
    }

    def __init__(self, address=None, device_name=None, is_agent_cache=None, mac=None, port=None):  # noqa: E501
        """ArpListObject - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._device_name = None
        self._is_agent_cache = None
        self._mac = None
        self._port = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if device_name is not None:
            self.device_name = device_name
        if is_agent_cache is not None:
            self.is_agent_cache = is_agent_cache
        if mac is not None:
            self.mac = mac
        if port is not None:
            self.port = port

    @property
    def address(self):
        """Gets the address of this ArpListObject.  # noqa: E501


        :return: The address of this ArpListObject.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ArpListObject.


        :param address: The address of this ArpListObject.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def device_name(self):
        """Gets the device_name of this ArpListObject.  # noqa: E501


        :return: The device_name of this ArpListObject.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this ArpListObject.


        :param device_name: The device_name of this ArpListObject.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def is_agent_cache(self):
        """Gets the is_agent_cache of this ArpListObject.  # noqa: E501


        :return: The is_agent_cache of this ArpListObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_agent_cache

    @is_agent_cache.setter
    def is_agent_cache(self, is_agent_cache):
        """Sets the is_agent_cache of this ArpListObject.


        :param is_agent_cache: The is_agent_cache of this ArpListObject.  # noqa: E501
        :type: bool
        """

        self._is_agent_cache = is_agent_cache

    @property
    def mac(self):
        """Gets the mac of this ArpListObject.  # noqa: E501


        :return: The mac of this ArpListObject.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this ArpListObject.


        :param mac: The mac of this ArpListObject.  # noqa: E501
        :type: str
        """

        self._mac = mac

    @property
    def port(self):
        """Gets the port of this ArpListObject.  # noqa: E501


        :return: The port of this ArpListObject.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ArpListObject.


        :param port: The port of this ArpListObject.  # noqa: E501
        :type: str
        """

        self._port = port

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
        if issubclass(ArpListObject, dict):
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
        if not isinstance(other, ArpListObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other