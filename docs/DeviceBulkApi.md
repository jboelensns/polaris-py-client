# polarisgenclient.DeviceBulkApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_device_device_name_bulk_sync_post**](DeviceBulkApi.md#api_v01_device_device_name_bulk_sync_post) | **POST** /api/v0.1/device/{device_name}/bulk/sync | DeviceBulkSyncRoute.post


# **api_v01_device_device_name_bulk_sync_post**
> api_v01_device_device_name_bulk_sync_post(device_name)

DeviceBulkSyncRoute.post

Dispatch real time bulk Device scan

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
api_instance = polarisgenclient.DeviceBulkApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN

try:
    # DeviceBulkSyncRoute.post
    api_instance.api_v01_device_device_name_bulk_sync_post(device_name)
except ApiException as e:
    print("Exception when calling DeviceBulkApi->api_v01_device_device_name_bulk_sync_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

