# polarisgenclient.IpamUtilizationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipam_utilization_post**](IpamUtilizationApi.md#ipam_utilization_post) | **GET** /api/v0.1/ipam/prefix/utilization | IpamUtilizationRoute.post


# **ipam_utilization_post**
> IpamUtilizationObject ipam_utilization_post(prefix=prefix)

IpamUtilizationRoute.post

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
api_instance = polarisgenclient.IpamUtilizationApi(polarisgenclient.ApiClient(configuration))
prefix = 'prefix_example' # str |  (optional)

try:
    # IpamUtilizationRoute.post
    api_response = api_instance.ipam_utilization_post(prefix=prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamUtilizationApi->ipam_utilization_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**|  | [optional] 

### Return type

[**IpamUtilizationObject**](IpamUtilizationObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

