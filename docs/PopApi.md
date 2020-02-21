# polarisgenclient.PopApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pop_delete**](PopApi.md#pop_delete) | **DELETE** /api/v0.1/pop/{name} | PopRoute.delete
[**pop_get**](PopApi.md#pop_get) | **GET** /api/v0.1/pop | PopRoute.get
[**pop_get_by_name**](PopApi.md#pop_get_by_name) | **GET** /api/v0.1/pop/{name} | PopRoute.get
[**pop_post**](PopApi.md#pop_post) | **POST** /api/v0.1/pop | PopRoute.post
[**pop_put**](PopApi.md#pop_put) | **PUT** /api/v0.1/pop/{name} | PopRoute.put


# **pop_delete**
> pop_delete(name)

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
    api_instance.pop_delete(name)
except ApiException as e:
    print("Exception when calling PopApi->pop_delete: %s\n" % e)
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

# **pop_get**
> list[Pop] pop_get()

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
    api_response = api_instance.pop_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PopApi->pop_get: %s\n" % e)
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

# **pop_get_by_name**
> list[Pop] pop_get_by_name(name)

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
    api_response = api_instance.pop_get_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PopApi->pop_get_by_name: %s\n" % e)
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

# **pop_post**
> pop_post(pop=pop)

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
    api_instance.pop_post(pop=pop)
except ApiException as e:
    print("Exception when calling PopApi->pop_post: %s\n" % e)
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

# **pop_put**
> pop_put(name, body=body)

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
    api_instance.pop_put(name, body=body)
except ApiException as e:
    print("Exception when calling PopApi->pop_put: %s\n" % e)
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

