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


class SystemImageProvisionObject(object):
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
        'cmdline': 'str',
        'description': 'str',
        'hardware_generation': 'str',
        'initrd': 'list[object]',
        'is_enabled': 'bool',
        'is_vm': 'bool',
        'kernel': 'str',
        'name': 'str',
        'preseed': 'str'
    }

    attribute_map = {
        'cmdline': 'cmdline',
        'description': 'description',
        'hardware_generation': 'hardware_generation',
        'initrd': 'initrd',
        'is_enabled': 'is_enabled',
        'is_vm': 'is_vm',
        'kernel': 'kernel',
        'name': 'name',
        'preseed': 'preseed'
    }

    def __init__(self, cmdline=None, description=None, hardware_generation=None, initrd=None, is_enabled=None, is_vm=None, kernel=None, name=None, preseed=None):  # noqa: E501
        """SystemImageProvisionObject - a model defined in Swagger"""  # noqa: E501

        self._cmdline = None
        self._description = None
        self._hardware_generation = None
        self._initrd = None
        self._is_enabled = None
        self._is_vm = None
        self._kernel = None
        self._name = None
        self._preseed = None
        self.discriminator = None

        if cmdline is not None:
            self.cmdline = cmdline
        if description is not None:
            self.description = description
        if hardware_generation is not None:
            self.hardware_generation = hardware_generation
        if initrd is not None:
            self.initrd = initrd
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if is_vm is not None:
            self.is_vm = is_vm
        self.kernel = kernel
        self.name = name
        if preseed is not None:
            self.preseed = preseed

    @property
    def cmdline(self):
        """Gets the cmdline of this SystemImageProvisionObject.  # noqa: E501


        :return: The cmdline of this SystemImageProvisionObject.  # noqa: E501
        :rtype: str
        """
        return self._cmdline

    @cmdline.setter
    def cmdline(self, cmdline):
        """Sets the cmdline of this SystemImageProvisionObject.


        :param cmdline: The cmdline of this SystemImageProvisionObject.  # noqa: E501
        :type: str
        """

        self._cmdline = cmdline

    @property
    def description(self):
        """Gets the description of this SystemImageProvisionObject.  # noqa: E501


        :return: The description of this SystemImageProvisionObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SystemImageProvisionObject.


        :param description: The description of this SystemImageProvisionObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hardware_generation(self):
        """Gets the hardware_generation of this SystemImageProvisionObject.  # noqa: E501


        :return: The hardware_generation of this SystemImageProvisionObject.  # noqa: E501
        :rtype: str
        """
        return self._hardware_generation

    @hardware_generation.setter
    def hardware_generation(self, hardware_generation):
        """Sets the hardware_generation of this SystemImageProvisionObject.


        :param hardware_generation: The hardware_generation of this SystemImageProvisionObject.  # noqa: E501
        :type: str
        """

        self._hardware_generation = hardware_generation

    @property
    def initrd(self):
        """Gets the initrd of this SystemImageProvisionObject.  # noqa: E501


        :return: The initrd of this SystemImageProvisionObject.  # noqa: E501
        :rtype: list[object]
        """
        return self._initrd

    @initrd.setter
    def initrd(self, initrd):
        """Sets the initrd of this SystemImageProvisionObject.


        :param initrd: The initrd of this SystemImageProvisionObject.  # noqa: E501
        :type: list[object]
        """

        self._initrd = initrd

    @property
    def is_enabled(self):
        """Gets the is_enabled of this SystemImageProvisionObject.  # noqa: E501


        :return: The is_enabled of this SystemImageProvisionObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this SystemImageProvisionObject.


        :param is_enabled: The is_enabled of this SystemImageProvisionObject.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def is_vm(self):
        """Gets the is_vm of this SystemImageProvisionObject.  # noqa: E501


        :return: The is_vm of this SystemImageProvisionObject.  # noqa: E501
        :rtype: bool
        """
        return self._is_vm

    @is_vm.setter
    def is_vm(self, is_vm):
        """Sets the is_vm of this SystemImageProvisionObject.


        :param is_vm: The is_vm of this SystemImageProvisionObject.  # noqa: E501
        :type: bool
        """

        self._is_vm = is_vm

    @property
    def kernel(self):
        """Gets the kernel of this SystemImageProvisionObject.  # noqa: E501


        :return: The kernel of this SystemImageProvisionObject.  # noqa: E501
        :rtype: str
        """
        return self._kernel

    @kernel.setter
    def kernel(self, kernel):
        """Sets the kernel of this SystemImageProvisionObject.


        :param kernel: The kernel of this SystemImageProvisionObject.  # noqa: E501
        :type: str
        """
        if kernel is None:
            raise ValueError("Invalid value for `kernel`, must not be `None`")  # noqa: E501

        self._kernel = kernel

    @property
    def name(self):
        """Gets the name of this SystemImageProvisionObject.  # noqa: E501


        :return: The name of this SystemImageProvisionObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SystemImageProvisionObject.


        :param name: The name of this SystemImageProvisionObject.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def preseed(self):
        """Gets the preseed of this SystemImageProvisionObject.  # noqa: E501


        :return: The preseed of this SystemImageProvisionObject.  # noqa: E501
        :rtype: str
        """
        return self._preseed

    @preseed.setter
    def preseed(self, preseed):
        """Sets the preseed of this SystemImageProvisionObject.


        :param preseed: The preseed of this SystemImageProvisionObject.  # noqa: E501
        :type: str
        """

        self._preseed = preseed

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
        if issubclass(SystemImageProvisionObject, dict):
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
        if not isinstance(other, SystemImageProvisionObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
