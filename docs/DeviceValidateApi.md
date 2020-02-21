# polarisgenclient.DeviceValidateApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_validate_get**](DeviceValidateApi.md#device_validate_get) | **GET** /api/v0.1/device/{device_name}/validate/{validate_name} | DeviceValidateRoute.get


# **device_validate_get**
> DeviceValidateObject device_validate_get(device_name, validate_name)

DeviceValidateRoute.get

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
api_instance = polarisgenclient.DeviceValidateApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
validate_name = 'validate_name_example' # str | Validation name

try:
    # DeviceValidateRoute.get
    api_response = api_instance.device_validate_get(device_name, validate_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceValidateApi->device_validate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **validate_name** | **str**| Validation name | 

### Return type

[**DeviceValidateObject**](DeviceValidateObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

