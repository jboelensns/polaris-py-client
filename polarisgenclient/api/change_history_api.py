# coding: utf-8

"""
    Polaris API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from polarisgenclient.api_client import ApiClient


class ChangeHistoryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v01_change_history_get(self, device_name, **kwargs):  # noqa: E501
        """ChangeHistoryRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_change_history_get(device_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: Device name (required)
        :return: list[ChangeHistoryObject]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_change_history_get_with_http_info(device_name, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_change_history_get_with_http_info(device_name, **kwargs)  # noqa: E501
            return data

    def api_v01_change_history_get_with_http_info(self, device_name, **kwargs):  # noqa: E501
        """ChangeHistoryRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_change_history_get_with_http_info(device_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: Device name (required)
        :return: list[ChangeHistoryObject]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_change_history_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_name' is set
        if ('device_name' not in params or
                params['device_name'] is None):
            raise ValueError("Missing the required parameter `device_name` when calling `api_v01_change_history_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_name' in params:
            path_params['device_name'] = params['device_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/change/history', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ChangeHistoryObject]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_device_device_name_change_history_get(self, device_name, **kwargs):  # noqa: E501
        """ChangeHistoryRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_device_device_name_change_history_get(device_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: Device name (required)
        :return: list[ChangeHistoryObject]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_device_device_name_change_history_get_with_http_info(device_name, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_device_device_name_change_history_get_with_http_info(device_name, **kwargs)  # noqa: E501
            return data

    def api_v01_device_device_name_change_history_get_with_http_info(self, device_name, **kwargs):  # noqa: E501
        """ChangeHistoryRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_device_device_name_change_history_get_with_http_info(device_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: Device name (required)
        :return: list[ChangeHistoryObject]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_device_device_name_change_history_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_name' is set
        if ('device_name' not in params or
                params['device_name'] is None):
            raise ValueError("Missing the required parameter `device_name` when calling `api_v01_device_device_name_change_history_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_name' in params:
            path_params['device_name'] = params['device_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/device/{device_name}/change/history', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ChangeHistoryObject]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
