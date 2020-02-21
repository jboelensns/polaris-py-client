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


class DeviceServiceDiscoverObject(object):
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
        'ip_address': 'str',
        'metadata': 'str',
        'name': 'str',
        'port': 'str',
        'protocol': 'str',
        'service_name': 'str'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'metadata': 'metadata',
        'name': 'name',
        'port': 'port',
        'protocol': 'protocol',
        'service_name': 'service_name'
    }

    def __init__(self, ip_address=None, metadata=None, name=None, port=None, protocol=None, service_name=None):  # noqa: E501
        """DeviceServiceDiscoverObject - a model defined in Swagger"""  # noqa: E501

        self._ip_address = None
        self._metadata = None
        self._name = None
        self._port = None
        self._protocol = None
        self._service_name = None
        self.discriminator = None

        self.ip_address = ip_address
        if metadata is not None:
            self.metadata = metadata
        self.name = name
        self.port = port
        if protocol is not None:
            self.protocol = protocol
        self.service_name = service_name

    @property
    def ip_address(self):
        """Gets the ip_address of this DeviceServiceDiscoverObject.  # noqa: E501


        :return: The ip_address of this DeviceServiceDiscoverObject.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DeviceServiceDiscoverObject.


        :param ip_address: The ip_address of this DeviceServiceDiscoverObject.  # noqa: E501
        :type: str
        """
        if ip_address is None:
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def metadata(self):
        """Gets the metadata of this DeviceServiceDiscoverObject.  # noqa: E501

        optional JSON encoded metadata  # noqa: E501

        :return: The metadata of this DeviceServiceDiscoverObject.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DeviceServiceDiscoverObject.

        optional JSON encoded metadata  # noqa: E501

        :param metadata: The metadata of this DeviceServiceDiscoverObject.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this DeviceServiceDiscoverObject.  # noqa: E501


        :return: The name of this DeviceServiceDiscoverObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceServiceDiscoverObject.


        :param name: The name of this DeviceServiceDiscoverObject.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def port(self):
        """Gets the port of this DeviceServiceDiscoverObject.  # noqa: E501


        :return: The port of this DeviceServiceDiscoverObject.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DeviceServiceDiscoverObject.


        :param port: The port of this DeviceServiceDiscoverObject.  # noqa: E501
        :type: str
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this DeviceServiceDiscoverObject.  # noqa: E501


        :return: The protocol of this DeviceServiceDiscoverObject.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this DeviceServiceDiscoverObject.


        :param protocol: The protocol of this DeviceServiceDiscoverObject.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def service_name(self):
        """Gets the service_name of this DeviceServiceDiscoverObject.  # noqa: E501


        :return: The service_name of this DeviceServiceDiscoverObject.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this DeviceServiceDiscoverObject.


        :param service_name: The service_name of this DeviceServiceDiscoverObject.  # noqa: E501
        :type: str
        """
        if service_name is None:
            raise ValueError("Invalid value for `service_name`, must not be `None`")  # noqa: E501

        self._service_name = service_name

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
        if issubclass(DeviceServiceDiscoverObject, dict):
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
        if not isinstance(other, DeviceServiceDiscoverObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other