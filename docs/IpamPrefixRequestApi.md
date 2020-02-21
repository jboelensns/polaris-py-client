# polarisgenclient.IpamPrefixRequestApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_ipam_prefix_request_post**](IpamPrefixRequestApi.md#api_v01_ipam_prefix_request_post) | **POST** /api/v0.1/ipam/prefix/request | IpamPrefixRequestRoute.post


# **api_v01_ipam_prefix_request_post**
> Prefix api_v01_ipam_prefix_request_post(body=body)

IpamPrefixRequestRoute.post

### Example
```python
from __future__ import print_function
import time
import polarisgenclient
from polarisgenclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = polarisgenclient.Configuration()
configuration.api_key['X-Polaris-Signed'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Polaris-Signed'] = 'Bearer'

# create an instance of the API class
api_instance = polarisgenclient.IpamPrefixRequestApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.Body17() # Body17 | IPAM Prefix Request object. (optional)

try:
    # IpamPrefixRequestRoute.post
    api_response = api_instance.api_v01_ipam_prefix_request_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamPrefixRequestApi->api_v01_ipam_prefix_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body17**](Body17.md)| IPAM Prefix Request object. | [optional] 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

