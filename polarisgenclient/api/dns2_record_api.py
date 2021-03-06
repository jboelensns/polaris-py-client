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


class Dns2RecordApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def dns2_record_post(self, zone, name, **kwargs):  # noqa: E501
        """Dns2RecordRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dns2_record_post(zone, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zone: (required)
        :param str name: (required)
        :return: DnsRecordObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dns2_record_post_with_http_info(zone, name, **kwargs)  # noqa: E501
        else:
            (data) = self.dns2_record_post_with_http_info(zone, name, **kwargs)  # noqa: E501
            return data

    def dns2_record_post_with_http_info(self, zone, name, **kwargs):  # noqa: E501
        """Dns2RecordRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dns2_record_post_with_http_info(zone, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str zone: (required)
        :param str name: (required)
        :return: DnsRecordObject
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['zone', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dns2_record_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'zone' is set
        if ('zone' not in params or
                params['zone'] is None):
            raise ValueError("Missing the required parameter `zone` when calling `dns2_record_post`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `dns2_record_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'zone' in params:
            path_params['zone'] = params['zone']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

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
            '/api/v0.1/dns2/record/{zone}/{name}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DnsRecordObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
