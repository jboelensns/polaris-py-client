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


class DhcpHelperProcessApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def dhcp_helper_process_delete(self, device_name, port, dst_ipv4_address, **kwargs):  # noqa: E501
        """DhcpHelperProcessRoute.delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dhcp_helper_process_delete(device_name, port, dst_ipv4_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: DhcpHelperProcess device_name (required)
        :param str port: DhcpHelperProcess port (required)
        :param str dst_ipv4_address: DhcpHelperProcess dst_ipv4_address (required)
        :return: DhcpHelperProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dhcp_helper_process_delete_with_http_info(device_name, port, dst_ipv4_address, **kwargs)  # noqa: E501
        else:
            (data) = self.dhcp_helper_process_delete_with_http_info(device_name, port, dst_ipv4_address, **kwargs)  # noqa: E501
            return data

    def dhcp_helper_process_delete_with_http_info(self, device_name, port, dst_ipv4_address, **kwargs):  # noqa: E501
        """DhcpHelperProcessRoute.delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dhcp_helper_process_delete_with_http_info(device_name, port, dst_ipv4_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: DhcpHelperProcess device_name (required)
        :param str port: DhcpHelperProcess port (required)
        :param str dst_ipv4_address: DhcpHelperProcess dst_ipv4_address (required)
        :return: DhcpHelperProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_name', 'port', 'dst_ipv4_address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dhcp_helper_process_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_name' is set
        if ('device_name' not in params or
                params['device_name'] is None):
            raise ValueError("Missing the required parameter `device_name` when calling `dhcp_helper_process_delete`")  # noqa: E501
        # verify the required parameter 'port' is set
        if ('port' not in params or
                params['port'] is None):
            raise ValueError("Missing the required parameter `port` when calling `dhcp_helper_process_delete`")  # noqa: E501
        # verify the required parameter 'dst_ipv4_address' is set
        if ('dst_ipv4_address' not in params or
                params['dst_ipv4_address'] is None):
            raise ValueError("Missing the required parameter `dst_ipv4_address` when calling `dhcp_helper_process_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_name' in params:
            path_params['device_name'] = params['device_name']  # noqa: E501

        query_params = []
        if 'port' in params:
            query_params.append(('port', params['port']))  # noqa: E501
        if 'dst_ipv4_address' in params:
            query_params.append(('dst_ipv4_address', params['dst_ipv4_address']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/device/{device_name}/dhcp/helper', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DhcpHelperProcessObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dhcp_helper_process_get(self, **kwargs):  # noqa: E501
        """DhcpHelperProcessRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dhcp_helper_process_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DhcpHelperProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dhcp_helper_process_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.dhcp_helper_process_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def dhcp_helper_process_get_with_http_info(self, **kwargs):  # noqa: E501
        """DhcpHelperProcessRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dhcp_helper_process_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DhcpHelperProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dhcp_helper_process_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/dhcp/helper', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DhcpHelperProcessObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dhcp_helper_process_get_by_device(self, device_name, **kwargs):  # noqa: E501
        """DhcpHelperProcessRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dhcp_helper_process_get_by_device(device_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: DhcpHelperProcess device_name (required)
        :return: DhcpHelperProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dhcp_helper_process_get_by_device_with_http_info(device_name, **kwargs)  # noqa: E501
        else:
            (data) = self.dhcp_helper_process_get_by_device_with_http_info(device_name, **kwargs)  # noqa: E501
            return data

    def dhcp_helper_process_get_by_device_with_http_info(self, device_name, **kwargs):  # noqa: E501
        """DhcpHelperProcessRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dhcp_helper_process_get_by_device_with_http_info(device_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: DhcpHelperProcess device_name (required)
        :return: DhcpHelperProcessObject
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
                    " to method dhcp_helper_process_get_by_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_name' is set
        if ('device_name' not in params or
                params['device_name'] is None):
            raise ValueError("Missing the required parameter `device_name` when calling `dhcp_helper_process_get_by_device`")  # noqa: E501

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
            '/api/v0.1/device/{device_name}/dhcp/helper', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DhcpHelperProcessObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dhcp_helper_process_post(self, **kwargs):  # noqa: E501
        """DhcpHelperProcessRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dhcp_helper_process_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DhcpHelperProcessObject body: DhcpHelperProcess object
        :return: DhcpHelperProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dhcp_helper_process_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.dhcp_helper_process_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def dhcp_helper_process_post_with_http_info(self, **kwargs):  # noqa: E501
        """DhcpHelperProcessRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dhcp_helper_process_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DhcpHelperProcessObject body: DhcpHelperProcess object
        :return: DhcpHelperProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dhcp_helper_process_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/dhcp/helper', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DhcpHelperProcessObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dhcp_helper_process_put(self, device_name, **kwargs):  # noqa: E501
        """DhcpHelperProcessRoute.put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dhcp_helper_process_put(device_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: DhcpHelperProcess device_name (required)
        :param DhcpHelperProcessObject body: DhcpHelperProcess object
        :return: DhcpHelperProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dhcp_helper_process_put_with_http_info(device_name, **kwargs)  # noqa: E501
        else:
            (data) = self.dhcp_helper_process_put_with_http_info(device_name, **kwargs)  # noqa: E501
            return data

    def dhcp_helper_process_put_with_http_info(self, device_name, **kwargs):  # noqa: E501
        """DhcpHelperProcessRoute.put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dhcp_helper_process_put_with_http_info(device_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: DhcpHelperProcess device_name (required)
        :param DhcpHelperProcessObject body: DhcpHelperProcess object
        :return: DhcpHelperProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_name', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dhcp_helper_process_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_name' is set
        if ('device_name' not in params or
                params['device_name'] is None):
            raise ValueError("Missing the required parameter `device_name` when calling `dhcp_helper_process_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_name' in params:
            path_params['device_name'] = params['device_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/device/{device_name}/dhcp/helper', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DhcpHelperProcessObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
