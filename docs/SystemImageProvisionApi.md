# polarisgenclient.SystemImageProvisionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_system_image_provision_get**](SystemImageProvisionApi.md#api_v01_system_image_provision_get) | **GET** /api/v0.1/system/image/provision | SystemImageProvisionRoute.get
[**api_v01_system_image_provision_name_delete**](SystemImageProvisionApi.md#api_v01_system_image_provision_name_delete) | **DELETE** /api/v0.1/system/image/provision/{name} | SystemImageProvisionRoute.delete
[**api_v01_system_image_provision_name_get**](SystemImageProvisionApi.md#api_v01_system_image_provision_name_get) | **GET** /api/v0.1/system/image/provision/{name} | SystemImageProvisionRoute.get
[**api_v01_system_image_provision_name_put**](SystemImageProvisionApi.md#api_v01_system_image_provision_name_put) | **PUT** /api/v0.1/system/image/provision/{name} | SystemImageProvisionRoute.put
[**api_v01_system_image_provision_post**](SystemImageProvisionApi.md#api_v01_system_image_provision_post) | **POST** /api/v0.1/system/image/provision | SystemImageProvisionRoute.post
[**api_v01_system_image_provision_src_name_clone_post**](SystemImageProvisionApi.md#api_v01_system_image_provision_src_name_clone_post) | **POST** /api/v0.1/system/image/provision/{src_name}/clone | SystemImageProvisionCloneRoute.post


# **api_v01_system_image_provision_get**
> SystemImageProvisionObject api_v01_system_image_provision_get(name)

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
    api_response = api_instance.api_v01_system_image_provision_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageProvisionApi->api_v01_system_image_provision_get: %s\n" % e)
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

# **api_v01_system_image_provision_name_delete**
> SystemImageProvisionObject api_v01_system_image_provision_name_delete(name)

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
    api_response = api_instance.api_v01_system_image_provision_name_delete(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageProvisionApi->api_v01_system_image_provision_name_delete: %s\n" % e)
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

# **api_v01_system_image_provision_name_get**
> SystemImageProvisionObject api_v01_system_image_provision_name_get(name)

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
    api_response = api_instance.api_v01_system_image_provision_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageProvisionApi->api_v01_system_image_provision_name_get: %s\n" % e)
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

# **api_v01_system_image_provision_name_put**
> SystemImageProvisionObject api_v01_system_image_provision_name_put(name, body=body)

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
    api_response = api_instance.api_v01_system_image_provision_name_put(name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageProvisionApi->api_v01_system_image_provision_name_put: %s\n" % e)
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

# **api_v01_system_image_provision_post**
> SystemImageProvisionObject api_v01_system_image_provision_post(system_provision_object=system_provision_object)

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
    api_response = api_instance.api_v01_system_image_provision_post(system_provision_object=system_provision_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageProvisionApi->api_v01_system_image_provision_post: %s\n" % e)
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

# **api_v01_system_image_provision_src_name_clone_post**
> SystemImageProvisionObject api_v01_system_image_provision_src_name_clone_post(src_name, body=body)

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
    api_response = api_instance.api_v01_system_image_provision_src_name_clone_post(src_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemImageProvisionApi->api_v01_system_image_provision_src_name_clone_post: %s\n" % e)
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

