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


class IPAMPool(object):
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
        'default_type': 'str',
        'description': 'str',
        'ipv4_default_prefix_length': 'int',
        'ipv6_default_prefix_length': 'int',
        'name': 'str',
        'tags_list': 'list[str]'
    }

    attribute_map = {
        'default_type': 'default_type',
        'description': 'description',
        'ipv4_default_prefix_length': 'ipv4_default_prefix_length',
        'ipv6_default_prefix_length': 'ipv6_default_prefix_length',
        'name': 'name',
        'tags_list': 'tags_list'
    }

    def __init__(self, default_type=None, description=None, ipv4_default_prefix_length=None, ipv6_default_prefix_length=None, name=None, tags_list=None):  # noqa: E501
        """IPAMPool - a model defined in Swagger"""  # noqa: E501

        self._default_type = None
        self._description = None
        self._ipv4_default_prefix_length = None
        self._ipv6_default_prefix_length = None
        self._name = None
        self._tags_list = None
        self.discriminator = None

        if default_type is not None:
            self.default_type = default_type
        if description is not None:
            self.description = description
        if ipv4_default_prefix_length is not None:
            self.ipv4_default_prefix_length = ipv4_default_prefix_length
        if ipv6_default_prefix_length is not None:
            self.ipv6_default_prefix_length = ipv6_default_prefix_length
        self.name = name
        if tags_list is not None:
            self.tags_list = tags_list

    @property
    def default_type(self):
        """Gets the default_type of this IPAMPool.  # noqa: E501


        :return: The default_type of this IPAMPool.  # noqa: E501
        :rtype: str
        """
        return self._default_type

    @default_type.setter
    def default_type(self, default_type):
        """Sets the default_type of this IPAMPool.


        :param default_type: The default_type of this IPAMPool.  # noqa: E501
        :type: str
        """

        self._default_type = default_type

    @property
    def description(self):
        """Gets the description of this IPAMPool.  # noqa: E501


        :return: The description of this IPAMPool.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IPAMPool.


        :param description: The description of this IPAMPool.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ipv4_default_prefix_length(self):
        """Gets the ipv4_default_prefix_length of this IPAMPool.  # noqa: E501


        :return: The ipv4_default_prefix_length of this IPAMPool.  # noqa: E501
        :rtype: int
        """
        return self._ipv4_default_prefix_length

    @ipv4_default_prefix_length.setter
    def ipv4_default_prefix_length(self, ipv4_default_prefix_length):
        """Sets the ipv4_default_prefix_length of this IPAMPool.


        :param ipv4_default_prefix_length: The ipv4_default_prefix_length of this IPAMPool.  # noqa: E501
        :type: int
        """

        self._ipv4_default_prefix_length = ipv4_default_prefix_length

    @property
    def ipv6_default_prefix_length(self):
        """Gets the ipv6_default_prefix_length of this IPAMPool.  # noqa: E501


        :return: The ipv6_default_prefix_length of this IPAMPool.  # noqa: E501
        :rtype: int
        """
        return self._ipv6_default_prefix_length

    @ipv6_default_prefix_length.setter
    def ipv6_default_prefix_length(self, ipv6_default_prefix_length):
        """Sets the ipv6_default_prefix_length of this IPAMPool.


        :param ipv6_default_prefix_length: The ipv6_default_prefix_length of this IPAMPool.  # noqa: E501
        :type: int
        """

        self._ipv6_default_prefix_length = ipv6_default_prefix_length

    @property
    def name(self):
        """Gets the name of this IPAMPool.  # noqa: E501


        :return: The name of this IPAMPool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IPAMPool.


        :param name: The name of this IPAMPool.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tags_list(self):
        """Gets the tags_list of this IPAMPool.  # noqa: E501


        :return: The tags_list of this IPAMPool.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags_list

    @tags_list.setter
    def tags_list(self, tags_list):
        """Sets the tags_list of this IPAMPool.


        :param tags_list: The tags_list of this IPAMPool.  # noqa: E501
        :type: list[str]
        """

        self._tags_list = tags_list

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
        if issubclass(IPAMPool, dict):
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
        if not isinstance(other, IPAMPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other