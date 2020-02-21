# polarisgenclient.SystemImageApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_image_delete**](SystemImageApi.md#system_image_delete) | **DELETE** /api/v0.1/system/image/{device_name} | SystemImageRoute.delete
[**system_image_get**](SystemImageApi.md#system_image_get) | **GET** /api/v0.1/system/image | SystemImageRoute.get
[**system_image_get_by_device**](SystemImageApi.md#system_image_get_by_device) | **GET** /api/v0.1/system/image/{device_name} | SystemImageRoute.get
[**system_image_post**](SystemImageApi.md#system_image_post) | **POST** /api/v0.1/system/image | SystemImageRoute.post
[**system_image_put**](SystemImageApi.md#system_image_put) | **PUT** /api/v0.1/system/image/{device_name} | SystemImageRoute.put


# **system_image_delete**
> SystemImageObject system_image_delete(device_name)

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
    api_response = api_instance.system_image_delete(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageApi->system_image_delete: %s\n" % e)
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

# **system_image_get**
> SystemImageObject system_image_get()

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

try:
    # SystemImageRoute.get
    api_response = api_instance.system_image_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageApi->system_image_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemImageObject**](SystemImageObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_get_by_device**
> SystemImageObject system_image_get_by_device(device_name)

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
    api_response = api_instance.system_image_get_by_device(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageApi->system_image_get_by_device: %s\n" % e)
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

# **system_image_post**
> SystemImageObject system_image_post(body=body)

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
    api_response = api_instance.system_image_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageApi->system_image_post: %s\n" % e)
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

# **system_image_put**
> SystemImageObject system_image_put(device_name, body=body)

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
    api_response = api_instance.system_image_put(device_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageApi->system_image_put: %s\n" % e)
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

