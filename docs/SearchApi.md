# polarisgenclient.SearchApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_search_get**](SearchApi.md#api_v01_search_get) | **GET** /api/v0.1/search | SearchRoute.get


# **api_v01_search_get**
> api_v01_search_get(search_input)

SearchRoute.get

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
api_instance = polarisgenclient.SearchApi(polarisgenclient.ApiClient(configuration))
search_input = 'search_input_example' # str | Host, IP Address, or MAC

try:
    # SearchRoute.get
    api_instance.api_v01_search_get(search_input)
except ApiException as e:
    print("Exception when calling SearchApi->api_v01_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_input** | **str**| Host, IP Address, or MAC | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

