# polarisgenclient.IpamNextIPApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_ipam_prefix_request_nextip_post**](IpamNextIPApi.md#api_v01_ipam_prefix_request_nextip_post) | **POST** /api/v0.1/ipam/prefix/request/nextip | IpamRequestNextIPRoute.post


# **api_v01_ipam_prefix_request_nextip_post**
> Prefix api_v01_ipam_prefix_request_nextip_post(next_ip_request=next_ip_request)

IpamRequestNextIPRoute.post

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
api_instance = polarisgenclient.IpamNextIPApi(polarisgenclient.ApiClient(configuration))
next_ip_request = polarisgenclient.NextIpRequest() # NextIpRequest | IPAM Request Next IP object. (optional)

try:
    # IpamRequestNextIPRoute.post
    api_response = api_instance.api_v01_ipam_prefix_request_nextip_post(next_ip_request=next_ip_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamNextIPApi->api_v01_ipam_prefix_request_nextip_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **next_ip_request** | [**NextIpRequest**](NextIpRequest.md)| IPAM Request Next IP object. | [optional] 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

