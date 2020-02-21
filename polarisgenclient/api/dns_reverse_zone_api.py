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


class DnsReverseZoneApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def dns_reverse_zone_delete(self, **kwargs):  # noqa: E501
        """DnsReverseZoneRoute.delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dns_reverse_zone_delete(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DnsZoneResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dns_reverse_zone_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.dns_reverse_zone_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def dns_reverse_zone_delete_with_http_info(self, **kwargs):  # noqa: E501
        """DnsReverseZoneRoute.delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dns_reverse_zone_delete_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[DnsZoneResponse]
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
                    " to method dns_reverse_zone_delete" % key
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
            '/api/v0.1/dns/zone/reverse', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DnsZoneResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dns_reverse_zone_delete_by_cidr(self, cidr, **kwargs):  # noqa: E501
        """DnsReverseZoneRoute.delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dns_reverse_zone_delete_by_cidr(cidr, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cidr: fqdn (required)
        :return: list[DnsZoneResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dns_reverse_zone_delete_by_cidr_with_http_info(cidr, **kwargs)  # noqa: E501
        else:
            (data) = self.dns_reverse_zone_delete_by_cidr_with_http_info(cidr, **kwargs)  # noqa: E501
            return data

    def dns_reverse_zone_delete_by_cidr_with_http_info(self, cidr, **kwargs):  # noqa: E501
        """DnsReverseZoneRoute.delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dns_reverse_zone_delete_by_cidr_with_http_info(cidr, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str cidr: fqdn (required)
        :return: list[DnsZoneResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cidr']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dns_reverse_zone_delete_by_cidr" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cidr' is set
        if ('cidr' not in params or
                params['cidr'] is None):
            raise ValueError("Missing the required parameter `cidr` when calling `dns_reverse_zone_delete_by_cidr`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'cidr' in params:
            path_params['cidr'] = params['cidr']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/dns/zone/reverse/{cidr}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DnsZoneResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dns_reverse_zone_post(self, **kwargs):  # noqa: E501
        """DnsReverseZoneRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dns_reverse_zone_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body13 body: Dns HOST object.
        :return: list[DnsZoneResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dns_reverse_zone_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.dns_reverse_zone_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def dns_reverse_zone_post_with_http_info(self, **kwargs):  # noqa: E501
        """DnsReverseZoneRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dns_reverse_zone_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body13 body: Dns HOST object.
        :return: list[DnsZoneResponse]
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
                    " to method dns_reverse_zone_post" % key
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
            '/api/v0.1/dns/zone/reverse', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DnsZoneResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
