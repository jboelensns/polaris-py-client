# polarisgenclient.SystemImageProvisionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_image_provision_clone_post**](SystemImageProvisionApi.md#system_image_provision_clone_post) | **POST** /api/v0.1/system/image/provision/{src_name}/clone | SystemImageProvisionCloneRoute.post
[**system_image_provision_delete**](SystemImageProvisionApi.md#system_image_provision_delete) | **DELETE** /api/v0.1/system/image/provision/{name} | SystemImageProvisionRoute.delete
[**system_image_provision_get**](SystemImageProvisionApi.md#system_image_provision_get) | **GET** /api/v0.1/system/image/provision | SystemImageProvisionRoute.get
[**system_image_provision_get_by_name**](SystemImageProvisionApi.md#system_image_provision_get_by_name) | **GET** /api/v0.1/system/image/provision/{name} | SystemImageProvisionRoute.get
[**system_image_provision_post**](SystemImageProvisionApi.md#system_image_provision_post) | **POST** /api/v0.1/system/image/provision | SystemImageProvisionRoute.post
[**system_image_provision_put**](SystemImageProvisionApi.md#system_image_provision_put) | **PUT** /api/v0.1/system/image/provision/{name} | SystemImageProvisionRoute.put


# **system_image_provision_clone_post**
> SystemImageProvisionObject system_image_provision_clone_post(src_name, body=body)

SystemImageProvisionCloneRoute.post

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
api_instance = polarisgenclient.SystemImageProvisionApi(polarisgenclient.ApiClient(configuration))
src_name = 'src_name_example' # str | source name
body = polarisgenclient.Body24() # Body24 | body (optional)

try:
    # SystemImageProvisionCloneRoute.post
    api_response = api_instance.system_image_provision_clone_post(src_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageProvisionApi->system_image_provision_clone_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_name** | **str**| source name | 
 **body** | [**Body24**](Body24.md)| body | [optional] 

### Return type

[**SystemImageProvisionObject**](SystemImageProvisionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_provision_delete**
> SystemImageProvisionObject system_image_provision_delete(name)

SystemImageProvisionRoute.delete

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
api_instance = polarisgenclient.SystemImageProvisionApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | name

try:
    # SystemImageProvisionRoute.delete
    api_response = api_instance.system_image_provision_delete(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageProvisionApi->system_image_provision_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 

### Return type

[**SystemImageProvisionObject**](SystemImageProvisionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_provision_get**
> SystemImageProvisionObject system_image_provision_get()

SystemImageProvisionRoute.get

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
api_instance = polarisgenclient.SystemImageProvisionApi(polarisgenclient.ApiClient(configuration))

try:
    # SystemImageProvisionRoute.get
    api_response = api_instance.system_image_provision_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageProvisionApi->system_image_provision_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemImageProvisionObject**](SystemImageProvisionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_provision_get_by_name**
> SystemImageProvisionObject system_image_provision_get_by_name(name)

SystemImageProvisionRoute.get

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
api_instance = polarisgenclient.SystemImageProvisionApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | name

try:
    # SystemImageProvisionRoute.get
    api_response = api_instance.system_image_provision_get_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageProvisionApi->system_image_provision_get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 

### Return type

[**SystemImageProvisionObject**](SystemImageProvisionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_provision_post**
> SystemImageProvisionObject system_image_provision_post(system_provision_object=system_provision_object)

SystemImageProvisionRoute.post

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
api_instance = polarisgenclient.SystemImageProvisionApi(polarisgenclient.ApiClient(configuration))
system_provision_object = polarisgenclient.SystemImageProvisionObject() # SystemImageProvisionObject | SystemImageProvision object (optional)

try:
    # SystemImageProvisionRoute.post
    api_response = api_instance.system_image_provision_post(system_provision_object=system_provision_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageProvisionApi->system_image_provision_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_provision_object** | [**SystemImageProvisionObject**](SystemImageProvisionObject.md)| SystemImageProvision object | [optional] 

### Return type

[**SystemImageProvisionObject**](SystemImageProvisionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_image_provision_put**
> SystemImageProvisionObject system_image_provision_put(name, body=body)

SystemImageProvisionRoute.put

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
api_instance = polarisgenclient.SystemImageProvisionApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | name
body = polarisgenclient.SystemImageProvisionObject() # SystemImageProvisionObject | SystemImageProvision object (optional)

try:
    # SystemImageProvisionRoute.put
    api_response = api_instance.system_image_provision_put(name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageProvisionApi->system_image_provision_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 
 **body** | [**SystemImageProvisionObject**](SystemImageProvisionObject.md)| SystemImageProvision object | [optional] 

### Return type

[**SystemImageProvisionObject**](SystemImageProvisionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

