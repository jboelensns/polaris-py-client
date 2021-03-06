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


class Body17(object):
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
        'comment': 'str',
        'description': 'str',
        'family': 'int',
        'is_from_pool': 'bool',
        'is_from_prefix': 'bool',
        'node': 'str',
        'parent_pool': 'str',
        'pool': 'str',
        'prefix': 'str',
        'prefix_length': 'int',
        'status': 'str',
        'tags': 'str',
        'tags_list': 'list[str]',
        'type': 'str',
        'vlan': 'int'
    }

    attribute_map = {
        'comment': 'comment',
        'description': 'description',
        'family': 'family',
        'is_from_pool': 'is_from_pool',
        'is_from_prefix': 'is_from_prefix',
        'node': 'node',
        'parent_pool': 'parent_pool',
        'pool': 'pool',
        'prefix': 'prefix',
        'prefix_length': 'prefix_length',
        'status': 'status',
        'tags': 'tags',
        'tags_list': 'tags_list',
        'type': 'type',
        'vlan': 'vlan'
    }

    def __init__(self, comment=None, description=None, family=None, is_from_pool=None, is_from_prefix=None, node=None, parent_pool=None, pool=None, prefix=None, prefix_length=None, status='assigned', tags=None, tags_list=None, type=None, vlan=None):  # noqa: E501
        """Body17 - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._description = None
        self._family = None
        self._is_from_pool = None
        self._is_from_prefix = None
        self._node = None
        self._parent_pool = None
        self._pool = None
        self._prefix = None
        self._prefix_length = None
        self._status = None
        self._tags = None
        self._tags_list = None
        self._type = None
        self._vlan = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if description is not None:
            self.description = description
        if family is not None:
            self.family = family
        if is_from_pool is not None:
            self.is_from_pool = is_from_pool
        if is_from_prefix is not None:
            self.is_from_prefix = is_from_prefix
        if node is not None:
            self.node = node
        if parent_pool is not None:
            self.parent_pool = parent_pool
        if pool is not None:
            self.pool = pool
        if prefix is not None:
            self.prefix = prefix
        if prefix_length is not None:
            self.prefix_length = prefix_length
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if tags_list is not None:
            self.tags_list = tags_list
        self.type = type
        if vlan is not None:
            self.vlan = vlan

    @property
    def comment(self):
        """Gets the comment of this Body17.  # noqa: E501


        :return: The comment of this Body17.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Body17.


        :param comment: The comment of this Body17.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def description(self):
        """Gets the description of this Body17.  # noqa: E501


        :return: The description of this Body17.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Body17.


        :param description: The description of this Body17.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def family(self):
        """Gets the family of this Body17.  # noqa: E501


        :return: The family of this Body17.  # noqa: E501
        :rtype: int
        """
        return self._family

    @family.setter
    def family(self, family):
        """Sets the family of this Body17.


        :param family: The family of this Body17.  # noqa: E501
        :type: int
        """

        self._family = family

    @property
    def is_from_pool(self):
        """Gets the is_from_pool of this Body17.  # noqa: E501


        :return: The is_from_pool of this Body17.  # noqa: E501
        :rtype: bool
        """
        return self._is_from_pool

    @is_from_pool.setter
    def is_from_pool(self, is_from_pool):
        """Sets the is_from_pool of this Body17.


        :param is_from_pool: The is_from_pool of this Body17.  # noqa: E501
        :type: bool
        """

        self._is_from_pool = is_from_pool

    @property
    def is_from_prefix(self):
        """Gets the is_from_prefix of this Body17.  # noqa: E501


        :return: The is_from_prefix of this Body17.  # noqa: E501
        :rtype: bool
        """
        return self._is_from_prefix

    @is_from_prefix.setter
    def is_from_prefix(self, is_from_prefix):
        """Sets the is_from_prefix of this Body17.


        :param is_from_prefix: The is_from_prefix of this Body17.  # noqa: E501
        :type: bool
        """

        self._is_from_prefix = is_from_prefix

    @property
    def node(self):
        """Gets the node of this Body17.  # noqa: E501


        :return: The node of this Body17.  # noqa: E501
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this Body17.


        :param node: The node of this Body17.  # noqa: E501
        :type: str
        """

        self._node = node

    @property
    def parent_pool(self):
        """Gets the parent_pool of this Body17.  # noqa: E501


        :return: The parent_pool of this Body17.  # noqa: E501
        :rtype: str
        """
        return self._parent_pool

    @parent_pool.setter
    def parent_pool(self, parent_pool):
        """Sets the parent_pool of this Body17.


        :param parent_pool: The parent_pool of this Body17.  # noqa: E501
        :type: str
        """

        self._parent_pool = parent_pool

    @property
    def pool(self):
        """Gets the pool of this Body17.  # noqa: E501


        :return: The pool of this Body17.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this Body17.


        :param pool: The pool of this Body17.  # noqa: E501
        :type: str
        """

        self._pool = pool

    @property
    def prefix(self):
        """Gets the prefix of this Body17.  # noqa: E501


        :return: The prefix of this Body17.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this Body17.


        :param prefix: The prefix of this Body17.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def prefix_length(self):
        """Gets the prefix_length of this Body17.  # noqa: E501


        :return: The prefix_length of this Body17.  # noqa: E501
        :rtype: int
        """
        return self._prefix_length

    @prefix_length.setter
    def prefix_length(self, prefix_length):
        """Sets the prefix_length of this Body17.


        :param prefix_length: The prefix_length of this Body17.  # noqa: E501
        :type: int
        """

        self._prefix_length = prefix_length

    @property
    def status(self):
        """Gets the status of this Body17.  # noqa: E501


        :return: The status of this Body17.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Body17.


        :param status: The status of this Body17.  # noqa: E501
        :type: str
        """
        allowed_values = ["assigned", "reserved", "quarantine"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this Body17.  # noqa: E501


        :return: The tags of this Body17.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Body17.


        :param tags: The tags of this Body17.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def tags_list(self):
        """Gets the tags_list of this Body17.  # noqa: E501


        :return: The tags_list of this Body17.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags_list

    @tags_list.setter
    def tags_list(self, tags_list):
        """Sets the tags_list of this Body17.


        :param tags_list: The tags_list of this Body17.  # noqa: E501
        :type: list[str]
        """

        self._tags_list = tags_list

    @property
    def type(self):
        """Gets the type of this Body17.  # noqa: E501


        :return: The type of this Body17.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Body17.


        :param type: The type of this Body17.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["reservation", "assignment", "host"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def vlan(self):
        """Gets the vlan of this Body17.  # noqa: E501


        :return: The vlan of this Body17.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this Body17.


        :param vlan: The vlan of this Body17.  # noqa: E501
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
        if issubclass(Body17, dict):
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
        if not isinstance(other, Body17):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
