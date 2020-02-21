# polarisgenclient.ApiHistoryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_history_get**](ApiHistoryApi.md#api_history_get) | **GET** /api/v0.1/admin/api/history | ApiHistoryRoute.post


# **api_history_get**
> ApiHistoryObject api_history_get(ip_address=ip_address, id=id)

ApiHistoryRoute.post

Returns a list of api events<br/>

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
api_instance = polarisgenclient.ApiHistoryApi(polarisgenclient.ApiClient(configuration))
ip_address = 'ip_address_example' # str | IP Address (optional)
id = 'id_example' # str | UUID1 str (optional)

try:
    # ApiHistoryRoute.post
    api_response = api_instance.api_history_get(ip_address=ip_address, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiHistoryApi->api_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| IP Address | [optional] 
 **id** | **str**| UUID1 str | [optional] 

### Return type

[**ApiHistoryObject**](ApiHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

