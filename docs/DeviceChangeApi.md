# polarisgenclient.DeviceChangeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_change_post**](DeviceChangeApi.md#device_change_post) | **POST** /api/v0.1/device/{device_name}/change | DeviceChangeRoute.post


# **device_change_post**
> DeviceChangeObject device_change_post(device_name, body=body)

DeviceChangeRoute.post

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
api_instance = polarisgenclient.DeviceChangeApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
body = polarisgenclient.DeviceChangeObject() # DeviceChangeObject | DeviceChange object (optional)

try:
    # DeviceChangeRoute.post
    api_response = api_instance.device_change_post(device_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceChangeApi->device_change_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **body** | [**DeviceChangeObject**](DeviceChangeObject.md)| DeviceChange object | [optional] 

### Return type

[**DeviceChangeObject**](DeviceChangeObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

