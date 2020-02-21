# polarisgenclient.ChangeHistoryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_history_get**](ChangeHistoryApi.md#change_history_get) | **GET** /api/v0.1/change/history | ChangeHistoryRoute.get
[**change_history_get_by_device_by_device**](ChangeHistoryApi.md#change_history_get_by_device_by_device) | **GET** /api/v0.1/device/{device_name}/change/history | ChangeHistoryRoute.get


# **change_history_get**
> list[ChangeHistoryObject] change_history_get()

ChangeHistoryRoute.get

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
api_instance = polarisgenclient.ChangeHistoryApi(polarisgenclient.ApiClient(configuration))

try:
    # ChangeHistoryRoute.get
    api_response = api_instance.change_history_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChangeHistoryApi->change_history_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ChangeHistoryObject]**](ChangeHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_history_get_by_device_by_device**
> list[ChangeHistoryObject] change_history_get_by_device_by_device(device_name)

ChangeHistoryRoute.get

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
api_instance = polarisgenclient.ChangeHistoryApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name

try:
    # ChangeHistoryRoute.get
    api_response = api_instance.change_history_get_by_device_by_device(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChangeHistoryApi->change_history_get_by_device_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 

### Return type

[**list[ChangeHistoryObject]**](ChangeHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

