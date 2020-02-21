# polarisgenclient.IpamUtilizationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_ipam_prefix_utilization_get**](IpamUtilizationApi.md#api_v01_ipam_prefix_utilization_get) | **GET** /api/v0.1/ipam/prefix/utilization | IpamUtilizationRoute.post


# **api_v01_ipam_prefix_utilization_get**
> IpamUtilizationObject api_v01_ipam_prefix_utilization_get(prefix=prefix)

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
    api_response = api_instance.api_v01_ipam_prefix_utilization_get(prefix=prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamUtilizationApi->api_v01_ipam_prefix_utilization_get: %s\n" % e)
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

