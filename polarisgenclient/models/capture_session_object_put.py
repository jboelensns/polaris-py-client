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


class CaptureSessionObjectPut(object):
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
        'agent_capture_exit_code': 'int',
        'agent_response_code': 'int',
        'agent_response_message': 'str',
        'agent_status': 'str',
        'agent_status_id': 'int',
        'description': 'str',
        'pid': 'int',
        'size': 'int',
        'size_limit_bytes': 'int',
        'tenant_id': 'str',
        'ticket_id': 'str',
        'time_limit_sec': 'int'
    }

    attribute_map = {
        'agent_capture_exit_code': 'agent_capture_exit_code',
        'agent_response_code': 'agent_response_code',
        'agent_response_message': 'agent_response_message',
        'agent_status': 'agent_status',
        'agent_status_id': 'agent_status_id',
        'description': 'description',
        'pid': 'pid',
        'size': 'size',
        'size_limit_bytes': 'size_limit_bytes',
        'tenant_id': 'tenant_id',
        'ticket_id': 'ticket_id',
        'time_limit_sec': 'time_limit_sec'
    }

    def __init__(self, agent_capture_exit_code=None, agent_response_code=None, agent_response_message=None, agent_status=None, agent_status_id=None, description=None, pid=None, size=None, size_limit_bytes=None, tenant_id=None, ticket_id=None, time_limit_sec=None):  # noqa: E501
        """CaptureSessionObjectPut - a model defined in Swagger"""  # noqa: E501

        self._agent_capture_exit_code = None
        self._agent_response_code = None
        self._agent_response_message = None
        self._agent_status = None
        self._agent_status_id = None
        self._description = None
        self._pid = None
        self._size = None
        self._size_limit_bytes = None
        self._tenant_id = None
        self._ticket_id = None
        self._time_limit_sec = None
        self.discriminator = None

        if agent_capture_exit_code is not None:
            self.agent_capture_exit_code = agent_capture_exit_code
        if agent_response_code is not None:
            self.agent_response_code = agent_response_code
        if agent_response_message is not None:
            self.agent_response_message = agent_response_message
        if agent_status is not None:
            self.agent_status = agent_status
        if agent_status_id is not None:
            self.agent_status_id = agent_status_id
        if description is not None:
            self.description = description
        if pid is not None:
            self.pid = pid
        if size is not None:
            self.size = size
        if size_limit_bytes is not None:
            self.size_limit_bytes = size_limit_bytes
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if ticket_id is not None:
            self.ticket_id = ticket_id
        if time_limit_sec is not None:
            self.time_limit_sec = time_limit_sec

    @property
    def agent_capture_exit_code(self):
        """Gets the agent_capture_exit_code of this CaptureSessionObjectPut.  # noqa: E501


        :return: The agent_capture_exit_code of this CaptureSessionObjectPut.  # noqa: E501
        :rtype: int
        """
        return self._agent_capture_exit_code

    @agent_capture_exit_code.setter
    def agent_capture_exit_code(self, agent_capture_exit_code):
        """Sets the agent_capture_exit_code of this CaptureSessionObjectPut.


        :param agent_capture_exit_code: The agent_capture_exit_code of this CaptureSessionObjectPut.  # noqa: E501
        :type: int
        """

        self._agent_capture_exit_code = agent_capture_exit_code

    @property
    def agent_response_code(self):
        """Gets the agent_response_code of this CaptureSessionObjectPut.  # noqa: E501


        :return: The agent_response_code of this CaptureSessionObjectPut.  # noqa: E501
        :rtype: int
        """
        return self._agent_response_code

    @agent_response_code.setter
    def agent_response_code(self, agent_response_code):
        """Sets the agent_response_code of this CaptureSessionObjectPut.


        :param agent_response_code: The agent_response_code of this CaptureSessionObjectPut.  # noqa: E501
        :type: int
        """

        self._agent_response_code = agent_response_code

    @property
    def agent_response_message(self):
        """Gets the agent_response_message of this CaptureSessionObjectPut.  # noqa: E501


        :return: The agent_response_message of this CaptureSessionObjectPut.  # noqa: E501
        :rtype: str
        """
        return self._agent_response_message

    @agent_response_message.setter
    def agent_response_message(self, agent_response_message):
        """Sets the agent_response_message of this CaptureSessionObjectPut.


        :param agent_response_message: The agent_response_message of this CaptureSessionObjectPut.  # noqa: E501
        :type: str
        """

        self._agent_response_message = agent_response_message

    @property
    def agent_status(self):
        """Gets the agent_status of this CaptureSessionObjectPut.  # noqa: E501


        :return: The agent_status of this CaptureSessionObjectPut.  # noqa: E501
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this CaptureSessionObjectPut.


        :param agent_status: The agent_status of this CaptureSessionObjectPut.  # noqa: E501
        :type: str
        """

        self._agent_status = agent_status

    @property
    def agent_status_id(self):
        """Gets the agent_status_id of this CaptureSessionObjectPut.  # noqa: E501


        :return: The agent_status_id of this CaptureSessionObjectPut.  # noqa: E501
        :rtype: int
        """
        return self._agent_status_id

    @agent_status_id.setter
    def agent_status_id(self, agent_status_id):
        """Sets the agent_status_id of this CaptureSessionObjectPut.


        :param agent_status_id: The agent_status_id of this CaptureSessionObjectPut.  # noqa: E501
        :type: int
        """

        self._agent_status_id = agent_status_id

    @property
    def description(self):
        """Gets the description of this CaptureSessionObjectPut.  # noqa: E501


        :return: The description of this CaptureSessionObjectPut.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CaptureSessionObjectPut.


        :param description: The description of this CaptureSessionObjectPut.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def pid(self):
        """Gets the pid of this CaptureSessionObjectPut.  # noqa: E501


        :return: The pid of this CaptureSessionObjectPut.  # noqa: E501
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this CaptureSessionObjectPut.


        :param pid: The pid of this CaptureSessionObjectPut.  # noqa: E501
        :type: int
        """

        self._pid = pid

    @property
    def size(self):
        """Gets the size of this CaptureSessionObjectPut.  # noqa: E501


        :return: The size of this CaptureSessionObjectPut.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CaptureSessionObjectPut.


        :param size: The size of this CaptureSessionObjectPut.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def size_limit_bytes(self):
        """Gets the size_limit_bytes of this CaptureSessionObjectPut.  # noqa: E501


        :return: The size_limit_bytes of this CaptureSessionObjectPut.  # noqa: E501
        :rtype: int
        """
        return self._size_limit_bytes

    @size_limit_bytes.setter
    def size_limit_bytes(self, size_limit_bytes):
        """Sets the size_limit_bytes of this CaptureSessionObjectPut.


        :param size_limit_bytes: The size_limit_bytes of this CaptureSessionObjectPut.  # noqa: E501
        :type: int
        """

        self._size_limit_bytes = size_limit_bytes

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CaptureSessionObjectPut.  # noqa: E501


        :return: The tenant_id of this CaptureSessionObjectPut.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CaptureSessionObjectPut.


        :param tenant_id: The tenant_id of this CaptureSessionObjectPut.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def ticket_id(self):
        """Gets the ticket_id of this CaptureSessionObjectPut.  # noqa: E501


        :return: The ticket_id of this CaptureSessionObjectPut.  # noqa: E501
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        """Sets the ticket_id of this CaptureSessionObjectPut.


        :param ticket_id: The ticket_id of this CaptureSessionObjectPut.  # noqa: E501
        :type: str
        """

        self._ticket_id = ticket_id

    @property
    def time_limit_sec(self):
        """Gets the time_limit_sec of this CaptureSessionObjectPut.  # noqa: E501


        :return: The time_limit_sec of this CaptureSessionObjectPut.  # noqa: E501
        :rtype: int
        """
        return self._time_limit_sec

    @time_limit_sec.setter
    def time_limit_sec(self, time_limit_sec):
        """Sets the time_limit_sec of this CaptureSessionObjectPut.


        :param time_limit_sec: The time_limit_sec of this CaptureSessionObjectPut.  # noqa: E501
        :type: int
        """

        self._time_limit_sec = time_limit_sec

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
        if issubclass(CaptureSessionObjectPut, dict):
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
        if not isinstance(other, CaptureSessionObjectPut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
