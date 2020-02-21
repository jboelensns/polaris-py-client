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


class DnsCNAMERecordApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v01_dns_record_cname_fqdn_delete(self, fqdn, **kwargs):  # noqa: E501
        """DnsCNAMERecordRoute.delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_dns_record_cname_fqdn_delete(fqdn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fqdn: fqdn (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_dns_record_cname_fqdn_delete_with_http_info(fqdn, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_dns_record_cname_fqdn_delete_with_http_info(fqdn, **kwargs)  # noqa: E501
            return data

    def api_v01_dns_record_cname_fqdn_delete_with_http_info(self, fqdn, **kwargs):  # noqa: E501
        """DnsCNAMERecordRoute.delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_dns_record_cname_fqdn_delete_with_http_info(fqdn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fqdn: fqdn (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fqdn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_dns_record_cname_fqdn_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params or
                params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `api_v01_dns_record_cname_fqdn_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/dns/record/cname/{fqdn}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_dns_record_cname_fqdn_get(self, fqdn, canonical, **kwargs):  # noqa: E501
        """DnsCNAMERecordRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_dns_record_cname_fqdn_get(fqdn, canonical, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fqdn: fqdn (required)
        :param str canonical: canonical name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_dns_record_cname_fqdn_get_with_http_info(fqdn, canonical, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_dns_record_cname_fqdn_get_with_http_info(fqdn, canonical, **kwargs)  # noqa: E501
            return data

    def api_v01_dns_record_cname_fqdn_get_with_http_info(self, fqdn, canonical, **kwargs):  # noqa: E501
        """DnsCNAMERecordRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_dns_record_cname_fqdn_get_with_http_info(fqdn, canonical, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fqdn: fqdn (required)
        :param str canonical: canonical name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fqdn', 'canonical']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_dns_record_cname_fqdn_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params or
                params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `api_v01_dns_record_cname_fqdn_get`")  # noqa: E501
        # verify the required parameter 'canonical' is set
        if ('canonical' not in params or
                params['canonical'] is None):
            raise ValueError("Missing the required parameter `canonical` when calling `api_v01_dns_record_cname_fqdn_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']  # noqa: E501
        if 'canonical' in params:
            path_params['canonical'] = params['canonical']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/dns/record/cname/{fqdn}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_dns_record_cname_fqdn_put(self, fqdn, canonical, **kwargs):  # noqa: E501
        """DnsCNAMERecordRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_dns_record_cname_fqdn_put(fqdn, canonical, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fqdn: ip (required)
        :param str canonical: canonical (required)
        :param Body8 body: Dns object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_dns_record_cname_fqdn_put_with_http_info(fqdn, canonical, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_dns_record_cname_fqdn_put_with_http_info(fqdn, canonical, **kwargs)  # noqa: E501
            return data

    def api_v01_dns_record_cname_fqdn_put_with_http_info(self, fqdn, canonical, **kwargs):  # noqa: E501
        """DnsCNAMERecordRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_dns_record_cname_fqdn_put_with_http_info(fqdn, canonical, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fqdn: ip (required)
        :param str canonical: canonical (required)
        :param Body8 body: Dns object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fqdn', 'canonical', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_dns_record_cname_fqdn_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params or
                params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `api_v01_dns_record_cname_fqdn_put`")  # noqa: E501
        # verify the required parameter 'canonical' is set
        if ('canonical' not in params or
                params['canonical'] is None):
            raise ValueError("Missing the required parameter `canonical` when calling `api_v01_dns_record_cname_fqdn_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']  # noqa: E501
        if 'canonical' in params:
            path_params['canonical'] = params['canonical']  # noqa: E501

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
            '/api/v0.1/dns/record/cname/{fqdn}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_dns_record_cname_get(self, fqdn, canonical, **kwargs):  # noqa: E501
        """DnsCNAMERecordRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_dns_record_cname_get(fqdn, canonical, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fqdn: fqdn (required)
        :param str canonical: canonical name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_dns_record_cname_get_with_http_info(fqdn, canonical, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_dns_record_cname_get_with_http_info(fqdn, canonical, **kwargs)  # noqa: E501
            return data

    def api_v01_dns_record_cname_get_with_http_info(self, fqdn, canonical, **kwargs):  # noqa: E501
        """DnsCNAMERecordRoute.get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_dns_record_cname_get_with_http_info(fqdn, canonical, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str fqdn: fqdn (required)
        :param str canonical: canonical name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fqdn', 'canonical']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v01_dns_record_cname_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'fqdn' is set
        if ('fqdn' not in params or
                params['fqdn'] is None):
            raise ValueError("Missing the required parameter `fqdn` when calling `api_v01_dns_record_cname_get`")  # noqa: E501
        # verify the required parameter 'canonical' is set
        if ('canonical' not in params or
                params['canonical'] is None):
            raise ValueError("Missing the required parameter `canonical` when calling `api_v01_dns_record_cname_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'fqdn' in params:
            path_params['fqdn'] = params['fqdn']  # noqa: E501
        if 'canonical' in params:
            path_params['canonical'] = params['canonical']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.1/dns/record/cname', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v01_dns_record_cname_post(self, **kwargs):  # noqa: E501
        """DnsCNAMERecordRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_dns_record_cname_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body7 body: Dns CNAME object.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v01_dns_record_cname_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v01_dns_record_cname_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v01_dns_record_cname_post_with_http_info(self, **kwargs):  # noqa: E501
        """DnsCNAMERecordRoute.post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v01_dns_record_cname_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body7 body: Dns CNAME object.
        :return: None
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
                    " to method api_v01_dns_record_cname_post" % key
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
            '/api/v0.1/dns/record/cname', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
