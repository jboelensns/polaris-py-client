# polarisgenclient.PopApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_pop_get**](PopApi.md#api_v01_pop_get) | **GET** /api/v0.1/pop | PopRoute.get
[**api_v01_pop_name_delete**](PopApi.md#api_v01_pop_name_delete) | **DELETE** /api/v0.1/pop/{name} | PopRoute.delete
[**api_v01_pop_name_get**](PopApi.md#api_v01_pop_name_get) | **GET** /api/v0.1/pop/{name} | PopRoute.get
[**api_v01_pop_name_put**](PopApi.md#api_v01_pop_name_put) | **PUT** /api/v0.1/pop/{name} | PopRoute.put
[**api_v01_pop_post**](PopApi.md#api_v01_pop_post) | **POST** /api/v0.1/pop | PopRoute.post


# **api_v01_pop_get**
> list[Pop] api_v01_pop_get()

PopRoute.get

### Example
```python
from __future__ import print_function
import time
import polarisgenclient
from polarisgenclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = polarisgenclient.PopApi()

try:
    # PopRoute.get
    api_response = api_instance.api_v01_pop_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PopApi->api_v01_pop_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Pop]**](Pop.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_pop_name_delete**
> api_v01_pop_name_delete(name)

PopRoute.delete

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
api_instance = polarisgenclient.PopApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Pop name

try:
    # PopRoute.delete
    api_instance.api_v01_pop_name_delete(name)
except ApiException as e:
    print("Exception when calling PopApi->api_v01_pop_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Pop name | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_pop_name_get**
> list[Pop] api_v01_pop_name_get(name)

PopRoute.get

### Example
```python
from __future__ import print_function
import time
import polarisgenclient
from polarisgenclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = polarisgenclient.PopApi()
name = 'name_example' # str | Pop name

try:
    # PopRoute.get
    api_response = api_instance.api_v01_pop_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PopApi->api_v01_pop_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Pop name | 

### Return type

[**list[Pop]**](Pop.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_pop_name_put**
> api_v01_pop_name_put(name, body=body)

PopRoute.put

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
api_instance = polarisgenclient.PopApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Pop name
body = polarisgenclient.Pop() # Pop | Pop object. (optional)

try:
    # PopRoute.put
    api_instance.api_v01_pop_name_put(name, body=body)
except ApiException as e:
    print("Exception when calling PopApi->api_v01_pop_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Pop name | 
 **body** | [**Pop**](Pop.md)| Pop object. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_pop_post**
> api_v01_pop_post(pop=pop)

PopRoute.post

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
api_instance = polarisgenclient.PopApi(polarisgenclient.ApiClient(configuration))
pop = polarisgenclient.Pop1() # Pop1 | Pop object. (optional)

try:
    # PopRoute.post
    api_instance.api_v01_pop_post(pop=pop)
except ApiException as e:
    print("Exception when calling PopApi->api_v01_pop_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pop** | [**Pop1**](Pop1.md)| Pop object. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

