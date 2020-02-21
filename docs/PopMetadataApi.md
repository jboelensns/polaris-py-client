# polarisgenclient.PopMetadataApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pop_metadata_delete**](PopMetadataApi.md#pop_metadata_delete) | **DELETE** /api/v0.1/pop/{name}/metadata | PopMetadataRoute.delete
[**pop_metadata_get**](PopMetadataApi.md#pop_metadata_get) | **GET** /api/v0.1/pop/{name}/metadata | PopMetadataRoute.get
[**pop_metadata_post**](PopMetadataApi.md#pop_metadata_post) | **POST** /api/v0.1/pop/{name}/metadata | PopMetadataRoute.post
[**pop_metadata_put**](PopMetadataApi.md#pop_metadata_put) | **PUT** /api/v0.1/pop/{name}/metadata | PopMetadataRoute.put


# **pop_metadata_delete**
> pop_metadata_delete(name)

PopMetadataRoute.delete

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
api_instance = polarisgenclient.PopMetadataApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Pop name

try:
    # PopMetadataRoute.delete
    api_instance.pop_metadata_delete(name)
except ApiException as e:
    print("Exception when calling PopMetadataApi->pop_metadata_delete: %s\n" % e)
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

# **pop_metadata_get**
> pop_metadata_get(name)

PopMetadataRoute.get

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
api_instance = polarisgenclient.PopMetadataApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Pop name

try:
    # PopMetadataRoute.get
    api_instance.pop_metadata_get(name)
except ApiException as e:
    print("Exception when calling PopMetadataApi->pop_metadata_get: %s\n" % e)
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

# **pop_metadata_post**
> pop_metadata_post(name, pop_parameters=pop_parameters)

PopMetadataRoute.post

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
api_instance = polarisgenclient.PopMetadataApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Pop name
pop_parameters = polarisgenclient.PopParameters() # PopParameters | Pop metadata object. (optional)

try:
    # PopMetadataRoute.post
    api_instance.pop_metadata_post(name, pop_parameters=pop_parameters)
except ApiException as e:
    print("Exception when calling PopMetadataApi->pop_metadata_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Pop name | 
 **pop_parameters** | [**PopParameters**](PopParameters.md)| Pop metadata object. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pop_metadata_put**
> pop_metadata_put(name, body=body)

PopMetadataRoute.put

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
api_instance = polarisgenclient.PopMetadataApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Pop name
body = polarisgenclient.Body21() # Body21 | Pop metadata object. (optional)

try:
    # PopMetadataRoute.put
    api_instance.pop_metadata_put(name, body=body)
except ApiException as e:
    print("Exception when calling PopMetadataApi->pop_metadata_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Pop name | 
 **body** | [**Body21**](Body21.md)| Pop metadata object. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

