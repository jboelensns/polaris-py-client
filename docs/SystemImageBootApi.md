# polarisgenclient.SystemImageBootApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_system_image_boot_mac_address_get**](SystemImageBootApi.md#api_v01_system_image_boot_mac_address_get) | **GET** /api/v0.1/system/image/boot/{mac_address} | SystemImageBootRoute.get


# **api_v01_system_image_boot_mac_address_get**
> SystemImageBootObject api_v01_system_image_boot_mac_address_get(mac_address)

SystemImageBootRoute.get

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
api_instance = polarisgenclient.SystemImageBootApi(polarisgenclient.ApiClient(configuration))
mac_address = 'mac_address_example' # str | mac address

try:
    # SystemImageBootRoute.get
    api_response = api_instance.api_v01_system_image_boot_mac_address_get(mac_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageBootApi->api_v01_system_image_boot_mac_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac_address** | **str**| mac address | 

### Return type

[**SystemImageBootObject**](SystemImageBootObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

