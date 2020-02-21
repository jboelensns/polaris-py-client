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


class Body12(object):
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
        'fqdn': 'str',
        'ip': 'str',
        'view': 'str'
    }

    attribute_map = {
        'comment': 'comment',
        'fqdn': 'fqdn',
        'ip': 'ip',
        'view': 'view'
    }

    def __init__(self, comment=None, fqdn=None, ip=None, view=None):  # noqa: E501
        """Body12 - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._fqdn = None
        self._ip = None
        self._view = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if fqdn is not None:
            self.fqdn = fqdn
        if ip is not None:
            self.ip = ip
        if view is not None:
            self.view = view

    @property
    def comment(self):
        """Gets the comment of this Body12.  # noqa: E501


        :return: The comment of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Body12.


        :param comment: The comment of this Body12.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def fqdn(self):
        """Gets the fqdn of this Body12.  # noqa: E501


        :return: The fqdn of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """Sets the fqdn of this Body12.


        :param fqdn: The fqdn of this Body12.  # noqa: E501
        :type: str
        """

        self._fqdn = fqdn

    @property
    def ip(self):
        """Gets the ip of this Body12.  # noqa: E501


        :return: The ip of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Body12.


        :param ip: The ip of this Body12.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def view(self):
        """Gets the view of this Body12.  # noqa: E501


        :return: The view of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this Body12.


        :param view: The view of this Body12.  # noqa: E501
        :type: str
        """

        self._view = view

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
        if issubclass(Body12, dict):
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
        if not isinstance(other, Body12):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
