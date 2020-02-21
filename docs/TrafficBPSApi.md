# polarisgenclient.TrafficBPSApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**traffice_bps_get**](TrafficBPSApi.md#traffice_bps_get) | **GET** /api/v0.1/traffic/bps/pop/{pop_name} | TrafficBPSRoute.get


# **traffice_bps_get**
> traffice_bps_get(pop_name)

TrafficBPSRoute.get

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
api_instance = polarisgenclient.TrafficBPSApi(polarisgenclient.ApiClient(configuration))
pop_name = 'pop_name_example' # str | pop name

try:
    # TrafficBPSRoute.get
    api_instance.traffice_bps_get(pop_name)
except ApiException as e:
    print("Exception when calling TrafficBPSApi->traffice_bps_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pop_name** | **str**| pop name | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

