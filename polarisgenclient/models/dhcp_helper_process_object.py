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


class DhcpHelperProcessObject(object):
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
        'device_name': 'str',
        'dst_ipv4_address': 'str',
        'is_enabled': 'bool',
        'port': 'str',
        'src_ipv4_address': 'str',
        'src_vrf': 'str',
        'tag_dhcp_request_packets': 'str'
    }

    attribute_map = {
        'description': 'description',
        'device_name': 'device_name',
        'dst_ipv4_address': 'dst_ipv4_address',
        'is_enabled': 'is_enabled',
        'port': 'port',
        'src_ipv4_address': 'src_ipv4_address',
        'src_vrf': 'src_vrf',
        'tag_dhcp_request_packets': 'tag_dhcp_request_packets'
    }

    def __init__(self, description=None, device_name=None, dst_ipv4_address=None, is_enabled=None, port=None, src_ipv4_address=None, src_vrf=None, tag_dhcp_request_packets=None):  # noqa: E501
        """DhcpHelperProcessObject - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._device_name = None
        self._dst_ipv4_address = None
        self._is_enabled = None
        self._port = None
        self._src_ipv4_address = None
        self._src_vrf = None
        self._tag_dhcp_request_packets = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.device_name = device_name
        self.dst_ipv4_address = dst_ipv4_address
        if is_enabled is not None:
            self.is_enabled = is_enabled
        self.port = port
        if src_ipv4_address is not None:
            self.src_ipv4_address = src_ipv4_address
        if src_vrf is not None:
            self.src_vrf = src_vrf
        if tag_dhcp_request_packets is not None:
            self.tag_dhcp_request_packets = tag_dhcp_request_packets

    @property
    def description(self):
        """Gets the description of this DhcpHelperProcessObject.  # noqa: E501


        :return: The description of this DhcpHelperProcessObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DhcpHelperProcessObject.


        :param description: The description of this DhcpHelperProcessObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def device_name(self):
        """Gets the device_name of this DhcpHelperProcessObject.  # noqa: E501

        Device name  # noqa: E501

        :return: The device_name of this DhcpHelperProcessObject.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this DhcpHelperProcessObject.

        Device name  # noqa: E501

        :param device_name: The device_name of this DhcpHelperProcessObject.  # noqa: E501
        :type: str
        """
        if device_name is None:
            raise ValueError("Invalid value for `device_name`, must not be `None`")  # noqa: E501

        self._device_name = device_name

    @property
    def dst_ipv4_address(self):
        """Gets the dst_ipv4_address of this DhcpHelperProcessObject.  # noqa: E501

        ip address to forward DHCP packets  # noqa: E501

        :return: The dst_ipv4_address of this DhcpHelperProcessObject.  # noqa: E501
        :rtype: str
        """
        return self._dst_ipv4_address

    @dst_ipv4_address.setter
    def dst_ipv4_address(self, dst_ipv4_address):
        """Sets the dst_ipv4_address of this DhcpHelperProcessObject.

        ip address to forward DHCP packets  # noqa: E501

        :param dst_ipv4_address: The dst_ipv4_address of this DhcpHelperProcessObject.  # noqa: E501
        :type: str
        """
        if dst_ipv4_address is None:
            raise ValueError("Invalid value for `dst_ipv4_address`, must not be `None`")  # noqa: E501

        self._dst_ipv4_address = dst_ipv4_address

    @property
    def is_enabled(self):
        """Gets the is_enabled of this DhcpHelperProcessObject.  # noqa: E501


        :return: The is_enabled of this DhcpHelperProcessObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this DhcpHelperProcessObject.


        :param is_enabled: The is_enabled of this DhcpHelperProcessObject.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def port(self):
        """Gets the port of this DhcpHelperProcessObject.  # noqa: E501

        Port/Interface to apply dhcp helper configuration  # noqa: E501

        :return: The port of this DhcpHelperProcessObject.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DhcpHelperProcessObject.

        Port/Interface to apply dhcp helper configuration  # noqa: E501

        :param port: The port of this DhcpHelperProcessObject.  # noqa: E501
        :type: str
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def src_ipv4_address(self):
        """Gets the src_ipv4_address of this DhcpHelperProcessObject.  # noqa: E501

        source ip address to use on switch  # noqa: E501

        :return: The src_ipv4_address of this DhcpHelperProcessObject.  # noqa: E501
        :rtype: str
        """
        return self._src_ipv4_address

    @src_ipv4_address.setter
    def src_ipv4_address(self, src_ipv4_address):
        """Sets the src_ipv4_address of this DhcpHelperProcessObject.

        source ip address to use on switch  # noqa: E501

        :param src_ipv4_address: The src_ipv4_address of this DhcpHelperProcessObject.  # noqa: E501
        :type: str
        """

        self._src_ipv4_address = src_ipv4_address

    @property
    def src_vrf(self):
        """Gets the src_vrf of this DhcpHelperProcessObject.  # noqa: E501

        source VRF to use on switch  # noqa: E501

        :return: The src_vrf of this DhcpHelperProcessObject.  # noqa: E501
        :rtype: str
        """
        return self._src_vrf

    @src_vrf.setter
    def src_vrf(self, src_vrf):
        """Sets the src_vrf of this DhcpHelperProcessObject.

        source VRF to use on switch  # noqa: E501

        :param src_vrf: The src_vrf of this DhcpHelperProcessObject.  # noqa: E501
        :type: str
        """

        self._src_vrf = src_vrf

    @property
    def tag_dhcp_request_packets(self):
        """Gets the tag_dhcp_request_packets of this DhcpHelperProcessObject.  # noqa: E501

        Tag DHCP packets with content  # noqa: E501

        :return: The tag_dhcp_request_packets of this DhcpHelperProcessObject.  # noqa: E501
        :rtype: str
        """
        return self._tag_dhcp_request_packets

    @tag_dhcp_request_packets.setter
    def tag_dhcp_request_packets(self, tag_dhcp_request_packets):
        """Sets the tag_dhcp_request_packets of this DhcpHelperProcessObject.

        Tag DHCP packets with content  # noqa: E501

        :param tag_dhcp_request_packets: The tag_dhcp_request_packets of this DhcpHelperProcessObject.  # noqa: E501
        :type: str
        """

        self._tag_dhcp_request_packets = tag_dhcp_request_packets

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
        if issubclass(DhcpHelperProcessObject, dict):
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
        if not isinstance(other, DhcpHelperProcessObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
