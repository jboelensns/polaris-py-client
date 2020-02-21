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


class BgpRouteMapApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v01_routemap_bgp_get(self, route_map_id, **kwargs):  # noqa: E501
        """BgpRouteMapRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_routemap_bgp_get(route_map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str route_map_id: RouteMap id (required)
        :return: BgpRouteMapObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_routemap_bgp_get_with_http_info(route_map_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_routemap_bgp_get_with_http_info(route_map_id, **kwargs)  # noqa: E501
            return data

    def api_v01_routemap_bgp_get_with_http_info(self, route_map_id, **kwargs):  # noqa: E501
        """BgpRouteMapRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_routemap_bgp_get_with_http_info(route_map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str route_map_id: RouteMap id (required)
        :return: BgpRouteMapObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['route_map_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_routemap_bgp_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'route_map_id' is set
        if ('route_map_id' not in params or
                params['route_map_id'] is None):
            raise ValueError("Missing the required parameter `route_map_id` when calling `api_v01_routemap_bgp_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'route_map_id' in params:
            path_params['route_map_id'] = params['route_map_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/routemap/bgp', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BgpRouteMapObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_routemap_bgp_post(self, **kwargs):  # noqa: E501
        """BgpRouteMapRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_routemap_bgp_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BgpRouteMapObject body: BgpRouteMap object
        :return: BgpRouteMapObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_routemap_bgp_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_routemap_bgp_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v01_routemap_bgp_post_with_http_info(self, **kwargs):  # noqa: E501
        """BgpRouteMapRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_routemap_bgp_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BgpRouteMapObject body: BgpRouteMap object
        :return: BgpRouteMapObject
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
                    " to method api_v01_routemap_bgp_post" % key
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
            '/api/v0.1/routemap/bgp', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BgpRouteMapObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_routemap_route_map_id_bgp_get(self, route_map_id, **kwargs):  # noqa: E501
        """BgpRouteMapRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_routemap_route_map_id_bgp_get(route_map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str route_map_id: RouteMap id (required)
        :return: BgpRouteMapObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_routemap_route_map_id_bgp_get_with_http_info(route_map_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_routemap_route_map_id_bgp_get_with_http_info(route_map_id, **kwargs)  # noqa: E501
            return data

    def api_v01_routemap_route_map_id_bgp_get_with_http_info(self, route_map_id, **kwargs):  # noqa: E501
        """BgpRouteMapRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_routemap_route_map_id_bgp_get_with_http_info(route_map_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str route_map_id: RouteMap id (required)
        :return: BgpRouteMapObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['route_map_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_routemap_route_map_id_bgp_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'route_map_id' is set
        if ('route_map_id' not in params or
                params['route_map_id'] is None):
            raise ValueError("Missing the required parameter `route_map_id` when calling `api_v01_routemap_route_map_id_bgp_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'route_map_id' in params:
            path_params['route_map_id'] = params['route_map_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/routemap/{route_map_id}/bgp', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BgpRouteMapObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_routemap_route_map_id_bgp_id_seq_seq_delete(self, route_map_id, id, seq, **kwargs):  # noqa: E501
        """BgpRouteMapRoute.delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_routemap_route_map_id_bgp_id_seq_seq_delete(route_map_id, id, seq, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str route_map_id: RouteMap id (required)
        :param str id: UUID1 string (required)
        :param int seq: seq (required)
        :return: BgpRouteMapObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_routemap_route_map_id_bgp_id_seq_seq_delete_with_http_info(route_map_id, id, seq, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_routemap_route_map_id_bgp_id_seq_seq_delete_with_http_info(route_map_id, id, seq, **kwargs)  # noqa: E501
            return data

    def api_v01_routemap_route_map_id_bgp_id_seq_seq_delete_with_http_info(self, route_map_id, id, seq, **kwargs):  # noqa: E501
        """BgpRouteMapRoute.delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_routemap_route_map_id_bgp_id_seq_seq_delete_with_http_info(route_map_id, id, seq, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str route_map_id: RouteMap id (required)
        :param str id: UUID1 string (required)
        :param int seq: seq (required)
        :return: BgpRouteMapObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['route_map_id', 'id', 'seq']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_routemap_route_map_id_bgp_id_seq_seq_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'route_map_id' is set
        if ('route_map_id' not in params or
                params['route_map_id'] is None):
            raise ValueError("Missing the required parameter `route_map_id` when calling `api_v01_routemap_route_map_id_bgp_id_seq_seq_delete`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_v01_routemap_route_map_id_bgp_id_seq_seq_delete`")  # noqa: E501
        # verify the required parameter 'seq' is set
        if ('seq' not in params or
                params['seq'] is None):
            raise ValueError("Missing the required parameter `seq` when calling `api_v01_routemap_route_map_id_bgp_id_seq_seq_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'route_map_id' in params:
            path_params['route_map_id'] = params['route_map_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'seq' in params:
            path_params['seq'] = params['seq']  # noqa: E501

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
            '/api/v0.1/routemap/{route_map_id}/bgp/{id}/seq/{seq}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BgpRouteMapObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_routemap_route_map_id_bgp_id_seq_seq_put(self, route_map_id, id, seq, **kwargs):  # noqa: E501
        """BgpRouteMapRoute.put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_routemap_route_map_id_bgp_id_seq_seq_put(route_map_id, id, seq, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str route_map_id: RouteMap id (required)
        :param str id: UUID1 string (required)
        :param int seq: seq (required)
        :param BgpRouteMapObject body: BgpRouteMap object
        :return: BgpRouteMapObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_routemap_route_map_id_bgp_id_seq_seq_put_with_http_info(route_map_id, id, seq, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_routemap_route_map_id_bgp_id_seq_seq_put_with_http_info(route_map_id, id, seq, **kwargs)  # noqa: E501
            return data

    def api_v01_routemap_route_map_id_bgp_id_seq_seq_put_with_http_info(self, route_map_id, id, seq, **kwargs):  # noqa: E501
        """BgpRouteMapRoute.put  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_routemap_route_map_id_bgp_id_seq_seq_put_with_http_info(route_map_id, id, seq, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str route_map_id: RouteMap id (required)
        :param str id: UUID1 string (required)
        :param int seq: seq (required)
        :param BgpRouteMapObject body: BgpRouteMap object
        :return: BgpRouteMapObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['route_map_id', 'id', 'seq', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_routemap_route_map_id_bgp_id_seq_seq_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'route_map_id' is set
        if ('route_map_id' not in params or
                params['route_map_id'] is None):
            raise ValueError("Missing the required parameter `route_map_id` when calling `api_v01_routemap_route_map_id_bgp_id_seq_seq_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `api_v01_routemap_route_map_id_bgp_id_seq_seq_put`")  # noqa: E501
        # verify the required parameter 'seq' is set
        if ('seq' not in params or
                params['seq'] is None):
            raise ValueError("Missing the required parameter `seq` when calling `api_v01_routemap_route_map_id_bgp_id_seq_seq_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'route_map_id' in params:
            path_params['route_map_id'] = params['route_map_id']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'seq' in params:
            path_params['seq'] = params['seq']  # noqa: E501

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
            '/api/v0.1/routemap/{route_map_id}/bgp/{id}/seq/{seq}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BgpRouteMapObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
