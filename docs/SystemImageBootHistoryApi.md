# polarisgenclient.SystemImageBootHistoryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_image_boot_history_delete**](SystemImageBootHistoryApi.md#system_image_boot_history_delete) | **DELETE** /api/v0.1/system/image/boot/history/{device_name} | SystemImageBootHistoryRoute.delete
[**system_image_boot_history_get**](SystemImageBootHistoryApi.md#system_image_boot_history_get) | **GET** /api/v0.1/system/image/boot/history | SystemImageBootHistoryRoute.get
[**system_image_boot_history_get_by_device**](SystemImageBootHistoryApi.md#system_image_boot_history_get_by_device) | **GET** /api/v0.1/system/image/boot/history/{device_name} | SystemImageBootHistoryRoute.get
[**system_image_boot_history_get_by_id**](SystemImageBootHistoryApi.md#system_image_boot_history_get_by_id) | **GET** /api/v0.1/system/image/boot/history/{device_name}/id/{id} | SystemImageBootHistoryRoute.get
[**system_image_boot_history_post**](SystemImageBootHistoryApi.md#system_image_boot_history_post) | **POST** /api/v0.1/system/image/boot/history | SystemImageBootHistoryRoute.post


# **system_image_boot_history_delete**
> SystemImageBootHistoryObject system_image_boot_history_delete(device_name, id)

SystemImageBootHistoryRoute.delete

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
api_instance = polarisgenclient.SystemImageBootHistoryApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | name
id = 'id_example' # str | id

try:
    # SystemImageBootHistoryRoute.delete
    api_response = api_instance.system_image_boot_history_delete(device_name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageBootHistoryApi->system_image_boot_history_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| name | 
 **id** | **str**| id | 

### Return type

[**SystemImageBootHistoryObject**](SystemImageBootHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_boot_history_get**
> SystemImageBootHistoryObject system_image_boot_history_get()

SystemImageBootHistoryRoute.get

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
api_instance = polarisgenclient.SystemImageBootHistoryApi(polarisgenclient.ApiClient(configuration))

try:
    # SystemImageBootHistoryRoute.get
    api_response = api_instance.system_image_boot_history_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageBootHistoryApi->system_image_boot_history_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemImageBootHistoryObject**](SystemImageBootHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_boot_history_get_by_device**
> SystemImageBootHistoryObject system_image_boot_history_get_by_device(device_name)

SystemImageBootHistoryRoute.get

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
api_instance = polarisgenclient.SystemImageBootHistoryApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | name

try:
    # SystemImageBootHistoryRoute.get
    api_response = api_instance.system_image_boot_history_get_by_device(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageBootHistoryApi->system_image_boot_history_get_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| name | 

### Return type

[**SystemImageBootHistoryObject**](SystemImageBootHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_boot_history_get_by_id**
> SystemImageBootHistoryObject system_image_boot_history_get_by_id(device_name, id)

SystemImageBootHistoryRoute.get

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
api_instance = polarisgenclient.SystemImageBootHistoryApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | name
id = 'id_example' # str | id

try:
    # SystemImageBootHistoryRoute.get
    api_response = api_instance.system_image_boot_history_get_by_id(device_name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageBootHistoryApi->system_image_boot_history_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| name | 
 **id** | **str**| id | 

### Return type

[**SystemImageBootHistoryObject**](SystemImageBootHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_boot_history_post**
> SystemImageBootHistoryObject system_image_boot_history_post(body=body)

SystemImageBootHistoryRoute.post

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
api_instance = polarisgenclient.SystemImageBootHistoryApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.SystemImageBootHistoryObject() # SystemImageBootHistoryObject | SystemImageBootHistory object (optional)

try:
    # SystemImageBootHistoryRoute.post
    api_response = api_instance.system_image_boot_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageBootHistoryApi->system_image_boot_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemImageBootHistoryObject**](SystemImageBootHistoryObject.md)| SystemImageBootHistory object | [optional] 

### Return type

[**SystemImageBootHistoryObject**](SystemImageBootHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

