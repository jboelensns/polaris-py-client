# polarisgenclient.ValidationHistoryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validation_history_get**](ValidationHistoryApi.md#validation_history_get) | **GET** /api/v0.1/validation/history | ValidationHistoryRoute.get
[**validation_history_get_by_device**](ValidationHistoryApi.md#validation_history_get_by_device) | **GET** /api/v0.1/device/{device_name}/validation/history | ValidationHistoryRoute.get
[**validation_history_get_by_username**](ValidationHistoryApi.md#validation_history_get_by_username) | **GET** /api/v0.1/user/{username}/validation/history | ValidationHistoryRoute.get


# **validation_history_get**
> list[ValidationHistoryObject] validation_history_get()

ValidationHistoryRoute.get

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
api_instance = polarisgenclient.ValidationHistoryApi(polarisgenclient.ApiClient(configuration))

try:
    # ValidationHistoryRoute.get
    api_response = api_instance.validation_history_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidationHistoryApi->validation_history_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ValidationHistoryObject]**](ValidationHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validation_history_get_by_device**
> list[ValidationHistoryObject] validation_history_get_by_device(device_name)

ValidationHistoryRoute.get

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
api_instance = polarisgenclient.ValidationHistoryApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name

try:
    # ValidationHistoryRoute.get
    api_response = api_instance.validation_history_get_by_device(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidationHistoryApi->validation_history_get_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 

### Return type

[**list[ValidationHistoryObject]**](ValidationHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validation_history_get_by_username**
> list[ValidationHistoryObject] validation_history_get_by_username(username)

ValidationHistoryRoute.get

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
api_instance = polarisgenclient.ValidationHistoryApi(polarisgenclient.ApiClient(configuration))
username = 'username_example' # str | username

try:
    # ValidationHistoryRoute.get
    api_response = api_instance.validation_history_get_by_username(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidationHistoryApi->validation_history_get_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username | 

### Return type

[**list[ValidationHistoryObject]**](ValidationHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

