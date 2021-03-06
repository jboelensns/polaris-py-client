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


class CaptureGroupObject(object):
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
        'devices': 'list[object]',
        'session_id': 'str',
        'steering_method': 'str',
        'tenant_id': 'str',
        'ticket_id': 'str'
    }

    attribute_map = {
        'description': 'description',
        'devices': 'devices',
        'session_id': 'session_id',
        'steering_method': 'steering_method',
        'tenant_id': 'tenant_id',
        'ticket_id': 'ticket_id'
    }

    def __init__(self, description=None, devices=None, session_id=None, steering_method=None, tenant_id=None, ticket_id=None):  # noqa: E501
        """CaptureGroupObject - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._devices = None
        self._session_id = None
        self._steering_method = None
        self._tenant_id = None
        self._ticket_id = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.devices = devices
        self.session_id = session_id
        self.steering_method = steering_method
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if ticket_id is not None:
            self.ticket_id = ticket_id

    @property
    def description(self):
        """Gets the description of this CaptureGroupObject.  # noqa: E501


        :return: The description of this CaptureGroupObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CaptureGroupObject.


        :param description: The description of this CaptureGroupObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def devices(self):
        """Gets the devices of this CaptureGroupObject.  # noqa: E501


        :return: The devices of this CaptureGroupObject.  # noqa: E501
        :rtype: list[object]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this CaptureGroupObject.


        :param devices: The devices of this CaptureGroupObject.  # noqa: E501
        :type: list[object]
        """
        if devices is None:
            raise ValueError("Invalid value for `devices`, must not be `None`")  # noqa: E501

        self._devices = devices

    @property
    def session_id(self):
        """Gets the session_id of this CaptureGroupObject.  # noqa: E501

        UUIDv1 session id  # noqa: E501

        :return: The session_id of this CaptureGroupObject.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this CaptureGroupObject.

        UUIDv1 session id  # noqa: E501

        :param session_id: The session_id of this CaptureGroupObject.  # noqa: E501
        :type: str
        """
        if session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

    @property
    def steering_method(self):
        """Gets the steering_method of this CaptureGroupObject.  # noqa: E501


        :return: The steering_method of this CaptureGroupObject.  # noqa: E501
        :rtype: str
        """
        return self._steering_method

    @steering_method.setter
    def steering_method(self, steering_method):
        """Sets the steering_method of this CaptureGroupObject.


        :param steering_method: The steering_method of this CaptureGroupObject.  # noqa: E501
        :type: str
        """
        if steering_method is None:
            raise ValueError("Invalid value for `steering_method`, must not be `None`")  # noqa: E501
        allowed_values = ["IPSec", "GRE", "PXC", "NSClient"]  # noqa: E501
        if steering_method not in allowed_values:
            raise ValueError(
                "Invalid value for `steering_method` ({0}), must be one of {1}"  # noqa: E501
                .format(steering_method, allowed_values)
            )

        self._steering_method = steering_method

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CaptureGroupObject.  # noqa: E501


        :return: The tenant_id of this CaptureGroupObject.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CaptureGroupObject.


        :param tenant_id: The tenant_id of this CaptureGroupObject.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def ticket_id(self):
        """Gets the ticket_id of this CaptureGroupObject.  # noqa: E501


        :return: The ticket_id of this CaptureGroupObject.  # noqa: E501
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        """Sets the ticket_id of this CaptureGroupObject.


        :param ticket_id: The ticket_id of this CaptureGroupObject.  # noqa: E501
        :type: str
        """

        self._ticket_id = ticket_id

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
        if issubclass(CaptureGroupObject, dict):
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
        if not isinstance(other, CaptureGroupObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
