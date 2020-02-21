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


class OSPFNeighborObject(object):
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
        'created_at': 'str',
        'dead': 'str',
        'device_name': 'str',
        'instance': 'str',
        'port': 'str',
        'priority': 'int',
        'state': 'str'
    }

    attribute_map = {
        'address': 'address',
        'created_at': 'created_at',
        'dead': 'dead',
        'device_name': 'device_name',
        'instance': 'instance',
        'port': 'port',
        'priority': 'priority',
        'state': 'state'
    }

    def __init__(self, address=None, created_at=None, dead=None, device_name=None, instance=None, port=None, priority=None, state=None):  # noqa: E501
        """OSPFNeighborObject - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._created_at = None
        self._dead = None
        self._device_name = None
        self._instance = None
        self._port = None
        self._priority = None
        self._state = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if created_at is not None:
            self.created_at = created_at
        if dead is not None:
            self.dead = dead
        if device_name is not None:
            self.device_name = device_name
        if instance is not None:
            self.instance = instance
        if port is not None:
            self.port = port
        if priority is not None:
            self.priority = priority
        if state is not None:
            self.state = state

    @property
    def address(self):
        """Gets the address of this OSPFNeighborObject.  # noqa: E501


        :return: The address of this OSPFNeighborObject.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this OSPFNeighborObject.


        :param address: The address of this OSPFNeighborObject.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def created_at(self):
        """Gets the created_at of this OSPFNeighborObject.  # noqa: E501


        :return: The created_at of this OSPFNeighborObject.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OSPFNeighborObject.


        :param created_at: The created_at of this OSPFNeighborObject.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def dead(self):
        """Gets the dead of this OSPFNeighborObject.  # noqa: E501


        :return: The dead of this OSPFNeighborObject.  # noqa: E501
        :rtype: str
        """
        return self._dead

    @dead.setter
    def dead(self, dead):
        """Sets the dead of this OSPFNeighborObject.


        :param dead: The dead of this OSPFNeighborObject.  # noqa: E501
        :type: str
        """

        self._dead = dead

    @property
    def device_name(self):
        """Gets the device_name of this OSPFNeighborObject.  # noqa: E501


        :return: The device_name of this OSPFNeighborObject.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this OSPFNeighborObject.


        :param device_name: The device_name of this OSPFNeighborObject.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def instance(self):
        """Gets the instance of this OSPFNeighborObject.  # noqa: E501


        :return: The instance of this OSPFNeighborObject.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this OSPFNeighborObject.


        :param instance: The instance of this OSPFNeighborObject.  # noqa: E501
        :type: str
        """

        self._instance = instance

    @property
    def port(self):
        """Gets the port of this OSPFNeighborObject.  # noqa: E501


        :return: The port of this OSPFNeighborObject.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this OSPFNeighborObject.


        :param port: The port of this OSPFNeighborObject.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def priority(self):
        """Gets the priority of this OSPFNeighborObject.  # noqa: E501


        :return: The priority of this OSPFNeighborObject.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this OSPFNeighborObject.


        :param priority: The priority of this OSPFNeighborObject.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def state(self):
        """Gets the state of this OSPFNeighborObject.  # noqa: E501


        :return: The state of this OSPFNeighborObject.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this OSPFNeighborObject.


        :param state: The state of this OSPFNeighborObject.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(OSPFNeighborObject, dict):
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
        if not isinstance(other, OSPFNeighborObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
