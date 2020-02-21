# polarisgenclient.SystemImageApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_system_image_device_name_delete**](SystemImageApi.md#api_v01_system_image_device_name_delete) | **DELETE** /api/v0.1/system/image/{device_name} | SystemImageRoute.delete
[**api_v01_system_image_device_name_get**](SystemImageApi.md#api_v01_system_image_device_name_get) | **GET** /api/v0.1/system/image/{device_name} | SystemImageRoute.get
[**api_v01_system_image_device_name_put**](SystemImageApi.md#api_v01_system_image_device_name_put) | **PUT** /api/v0.1/system/image/{device_name} | SystemImageRoute.put
[**api_v01_system_image_get**](SystemImageApi.md#api_v01_system_image_get) | **GET** /api/v0.1/system/image | SystemImageRoute.get
[**api_v01_system_image_post**](SystemImageApi.md#api_v01_system_image_post) | **POST** /api/v0.1/system/image | SystemImageRoute.post


# **api_v01_system_image_device_name_delete**
> SystemImageObject api_v01_system_image_device_name_delete(device_name)

SystemImageRoute.delete

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
api_instance = polarisgenclient.SystemImageApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name

try:
    # SystemImageRoute.delete
    api_response = api_instance.api_v01_system_image_device_name_delete(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageApi->api_v01_system_image_device_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 

### Return type

[**SystemImageObject**](SystemImageObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_system_image_device_name_get**
> SystemImageObject api_v01_system_image_device_name_get(device_name)

SystemImageRoute.get

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
api_instance = polarisgenclient.SystemImageApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name

try:
    # SystemImageRoute.get
    api_response = api_instance.api_v01_system_image_device_name_get(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageApi->api_v01_system_image_device_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 

### Return type

[**SystemImageObject**](SystemImageObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_system_image_device_name_put**
> SystemImageObject api_v01_system_image_device_name_put(device_name, body=body)

SystemImageRoute.put

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
api_instance = polarisgenclient.SystemImageApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
body = polarisgenclient.SystemImageObject() # SystemImageObject | SystemImage object (optional)

try:
    # SystemImageRoute.put
    api_response = api_instance.api_v01_system_image_device_name_put(device_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageApi->api_v01_system_image_device_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **body** | [**SystemImageObject**](SystemImageObject.md)| SystemImage object | [optional] 

### Return type

[**SystemImageObject**](SystemImageObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_system_image_get**
> SystemImageObject api_v01_system_image_get(device_name)

SystemImageRoute.get

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
api_instance = polarisgenclient.SystemImageApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name

try:
    # SystemImageRoute.get
    api_response = api_instance.api_v01_system_image_get(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageApi->api_v01_system_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 

### Return type

[**SystemImageObject**](SystemImageObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_system_image_post**
> SystemImageObject api_v01_system_image_post(body=body)

SystemImageRoute.post

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
api_instance = polarisgenclient.SystemImageApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.SystemImageObject() # SystemImageObject | SystemImage object (optional)

try:
    # SystemImageRoute.post
    api_response = api_instance.api_v01_system_image_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageApi->api_v01_system_image_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemImageObject**](SystemImageObject.md)| SystemImage object | [optional] 

### Return type

[**SystemImageObject**](SystemImageObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

