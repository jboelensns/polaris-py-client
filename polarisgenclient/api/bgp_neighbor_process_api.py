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


class BgpNeighborProcessApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v01_bgp_neighbor_process_get(self, device_name, as_number, ip_address, **kwargs):  # noqa: E501
        """BgpNeighborProcessRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_bgp_neighbor_process_get(device_name, as_number, ip_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: BgpNeighborProcess device_name (required)
        :param int as_number: BgpNeighborProcess as_number (required)
        :param str ip_address: BgpNeighborProcess ip address (required)
        :return: BgpNeighborProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_bgp_neighbor_process_get_with_http_info(device_name, as_number, ip_address, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_bgp_neighbor_process_get_with_http_info(device_name, as_number, ip_address, **kwargs)  # noqa: E501
            return data

    def api_v01_bgp_neighbor_process_get_with_http_info(self, device_name, as_number, ip_address, **kwargs):  # noqa: E501
        """BgpNeighborProcessRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_bgp_neighbor_process_get_with_http_info(device_name, as_number, ip_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: BgpNeighborProcess device_name (required)
        :param int as_number: BgpNeighborProcess as_number (required)
        :param str ip_address: BgpNeighborProcess ip address (required)
        :return: BgpNeighborProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_name', 'as_number', 'ip_address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_bgp_neighbor_process_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_name' is set
        if ('device_name' not in params or
                params['device_name'] is None):
            raise ValueError("Missing the required parameter `device_name` when calling `api_v01_bgp_neighbor_process_get`")  # noqa: E501
        # verify the required parameter 'as_number' is set
        if ('as_number' not in params or
                params['as_number'] is None):
            raise ValueError("Missing the required parameter `as_number` when calling `api_v01_bgp_neighbor_process_get`")  # noqa: E501
        # verify the required parameter 'ip_address' is set
        if ('ip_address' not in params or
                params['ip_address'] is None):
            raise ValueError("Missing the required parameter `ip_address` when calling `api_v01_bgp_neighbor_process_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_name' in params:
            path_params['device_name'] = params['device_name']  # noqa: E501
        if 'as_number' in params:
            path_params['as_number'] = params['as_number']  # noqa: E501
        if 'ip_address' in params:
            path_params['ip_address'] = params['ip_address']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/bgp/neighbor/process', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BgpNeighborProcessObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_bgp_neighbor_process_post(self, **kwargs):  # noqa: E501
        """BgpNeighborProcessRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_bgp_neighbor_process_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BgpNeighborProcessObject body: BgpNeighborProcess object
        :return: BgpNeighborProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_bgp_neighbor_process_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_bgp_neighbor_process_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v01_bgp_neighbor_process_post_with_http_info(self, **kwargs):  # noqa: E501
        """BgpNeighborProcessRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_bgp_neighbor_process_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BgpNeighborProcessObject body: BgpNeighborProcess object
        :return: BgpNeighborProcessObject
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
                    " to method api_v01_bgp_neighbor_process_post" % key
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
            '/api/v0.1/bgp/neighbor/process', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BgpNeighborProcessObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_delete(self, device_name, as_number, ip_address, **kwargs):  # noqa: E501
        """BgpNeighborProcessRoute.delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_delete(device_name, as_number, ip_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: BgpNeighborProcess device_name (required)
        :param int as_number: BgpNeighborProcess as_number (required)
        :param str ip_address: BgpNeighborProcess ip_address (required)
        :return: BgpNeighborProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_delete_with_http_info(device_name, as_number, ip_address, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_delete_with_http_info(device_name, as_number, ip_address, **kwargs)  # noqa: E501
            return data

    def api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_delete_with_http_info(self, device_name, as_number, ip_address, **kwargs):  # noqa: E501
        """BgpNeighborProcessRoute.delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_delete_with_http_info(device_name, as_number, ip_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: BgpNeighborProcess device_name (required)
        :param int as_number: BgpNeighborProcess as_number (required)
        :param str ip_address: BgpNeighborProcess ip_address (required)
        :return: BgpNeighborProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_name', 'as_number', 'ip_address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_name' is set
        if ('device_name' not in params or
                params['device_name'] is None):
            raise ValueError("Missing the required parameter `device_name` when calling `api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_delete`")  # noqa: E501
        # verify the required parameter 'as_number' is set
        if ('as_number' not in params or
                params['as_number'] is None):
            raise ValueError("Missing the required parameter `as_number` when calling `api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_delete`")  # noqa: E501
        # verify the required parameter 'ip_address' is set
        if ('ip_address' not in params or
                params['ip_address'] is None):
            raise ValueError("Missing the required parameter `ip_address` when calling `api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_name' in params:
            path_params['device_name'] = params['device_name']  # noqa: E501
        if 'as_number' in params:
            path_params['as_number'] = params['as_number']  # noqa: E501
        if 'ip_address' in params:
            path_params['ip_address'] = params['ip_address']  # noqa: E501

        query_params = []

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
            '/api/v0.1/device/{device_name}/bgp/{as_number}/neighbor/{ip_address}/process', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BgpNeighborProcessObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_get(self, device_name, as_number, ip_address, **kwargs):  # noqa: E501
        """BgpNeighborProcessRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_get(device_name, as_number, ip_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: BgpNeighborProcess device_name (required)
        :param int as_number: BgpNeighborProcess as_number (required)
        :param str ip_address: BgpNeighborProcess ip address (required)
        :return: BgpNeighborProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_get_with_http_info(device_name, as_number, ip_address, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_get_with_http_info(device_name, as_number, ip_address, **kwargs)  # noqa: E501
            return data

    def api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_get_with_http_info(self, device_name, as_number, ip_address, **kwargs):  # noqa: E501
        """BgpNeighborProcessRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_get_with_http_info(device_name, as_number, ip_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: BgpNeighborProcess device_name (required)
        :param int as_number: BgpNeighborProcess as_number (required)
        :param str ip_address: BgpNeighborProcess ip address (required)
        :return: BgpNeighborProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_name', 'as_number', 'ip_address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_name' is set
        if ('device_name' not in params or
                params['device_name'] is None):
            raise ValueError("Missing the required parameter `device_name` when calling `api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_get`")  # noqa: E501
        # verify the required parameter 'as_number' is set
        if ('as_number' not in params or
                params['as_number'] is None):
            raise ValueError("Missing the required parameter `as_number` when calling `api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_get`")  # noqa: E501
        # verify the required parameter 'ip_address' is set
        if ('ip_address' not in params or
                params['ip_address'] is None):
            raise ValueError("Missing the required parameter `ip_address` when calling `api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_name' in params:
            path_params['device_name'] = params['device_name']  # noqa: E501
        if 'as_number' in params:
            path_params['as_number'] = params['as_number']  # noqa: E501
        if 'ip_address' in params:
            path_params['ip_address'] = params['ip_address']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/device/{device_name}/bgp/{as_number}/neighbor/{ip_address}/process', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BgpNeighborProcessObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_put(self, device_name, as_number, ip_address, **kwargs):  # noqa: E501
        """BgpNeighborProcessRoute.put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_put(device_name, as_number, ip_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: BgpNeighborProcess device_name (required)
        :param int as_number: BgpNeighborProcess as_number (required)
        :param str ip_address: BgpNeighborProcess ip_address (required)
        :param BgpNeighborProcessObject body: BgpNeighborProcess object
        :return: BgpNeighborProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_put_with_http_info(device_name, as_number, ip_address, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_put_with_http_info(device_name, as_number, ip_address, **kwargs)  # noqa: E501
            return data

    def api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_put_with_http_info(self, device_name, as_number, ip_address, **kwargs):  # noqa: E501
        """BgpNeighborProcessRoute.put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_put_with_http_info(device_name, as_number, ip_address, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_name: BgpNeighborProcess device_name (required)
        :param int as_number: BgpNeighborProcess as_number (required)
        :param str ip_address: BgpNeighborProcess ip_address (required)
        :param BgpNeighborProcessObject body: BgpNeighborProcess object
        :return: BgpNeighborProcessObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_name', 'as_number', 'ip_address', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_name' is set
        if ('device_name' not in params or
                params['device_name'] is None):
            raise ValueError("Missing the required parameter `device_name` when calling `api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_put`")  # noqa: E501
        # verify the required parameter 'as_number' is set
        if ('as_number' not in params or
                params['as_number'] is None):
            raise ValueError("Missing the required parameter `as_number` when calling `api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_put`")  # noqa: E501
        # verify the required parameter 'ip_address' is set
        if ('ip_address' not in params or
                params['ip_address'] is None):
            raise ValueError("Missing the required parameter `ip_address` when calling `api_v01_device_device_name_bgp_as_number_neighbor_ip_address_process_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_name' in params:
            path_params['device_name'] = params['device_name']  # noqa: E501
        if 'as_number' in params:
            path_params['as_number'] = params['as_number']  # noqa: E501
        if 'ip_address' in params:
            path_params['ip_address'] = params['ip_address']  # noqa: E501

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
            '/api/v0.1/device/{device_name}/bgp/{as_number}/neighbor/{ip_address}/process', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BgpNeighborProcessObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
