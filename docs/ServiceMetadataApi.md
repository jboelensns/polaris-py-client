# polarisgenclient.ServiceMetadataApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_metadata_delete**](ServiceMetadataApi.md#service_metadata_delete) | **DELETE** /api/v0.1/service/{name}/id/{id}/metadata | ServiceMetadataRoute.delete
[**service_metadata_get**](ServiceMetadataApi.md#service_metadata_get) | **GET** /api/v0.1/service/{name}/id/{id}/metadata | ServiceMetadataRoute.get
[**service_metadata_post**](ServiceMetadataApi.md#service_metadata_post) | **POST** /api/v0.1/service/{name}/id/{id}/metadata | ServiceMetadataRoute.post
[**service_metadata_put**](ServiceMetadataApi.md#service_metadata_put) | **PUT** /api/v0.1/service/{name}/id/{id}/metadata | ServiceMetadataRoute.put


# **service_metadata_delete**
> list[ServiceMetadataObject] service_metadata_delete(name, id)

ServiceMetadataRoute.delete

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
api_instance = polarisgenclient.ServiceMetadataApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Service name
id = 'id_example' # str | UUID1 str

try:
    # ServiceMetadataRoute.delete
    api_response = api_instance.service_metadata_delete(name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceMetadataApi->service_metadata_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Service name | 
 **id** | **str**| UUID1 str | 

### Return type

[**list[ServiceMetadataObject]**](ServiceMetadataObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_metadata_get**
> list[ServiceMetadataObject] service_metadata_get(name, id)

ServiceMetadataRoute.get

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
api_instance = polarisgenclient.ServiceMetadataApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Service name
id = 'id_example' # str | UUID1 string

try:
    # ServiceMetadataRoute.get
    api_response = api_instance.service_metadata_get(name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceMetadataApi->service_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Service name | 
 **id** | **str**| UUID1 string | 

### Return type

[**list[ServiceMetadataObject]**](ServiceMetadataObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_metadata_post**
> list[ServiceMetadataObject] service_metadata_post(name, id, body=body)

ServiceMetadataRoute.post

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
api_instance = polarisgenclient.ServiceMetadataApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Service name
id = 'id_example' # str | UUID1 str
body = polarisgenclient.Body23() # Body23 | Service metadata object. (optional)

try:
    # ServiceMetadataRoute.post
    api_response = api_instance.service_metadata_post(name, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceMetadataApi->service_metadata_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Service name | 
 **id** | **str**| UUID1 str | 
 **body** | [**Body23**](Body23.md)| Service metadata object. | [optional] 

### Return type

[**list[ServiceMetadataObject]**](ServiceMetadataObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_metadata_put**
> list[ServiceMetadataObject] service_metadata_put(name, id, body=body)

ServiceMetadataRoute.put

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
api_instance = polarisgenclient.ServiceMetadataApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Service name
id = 'id_example' # str | UUID1 str
body = polarisgenclient.Body22() # Body22 | Service metadata object. (optional)

try:
    # ServiceMetadataRoute.put
    api_response = api_instance.service_metadata_put(name, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceMetadataApi->service_metadata_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Service name | 
 **id** | **str**| UUID1 str | 
 **body** | [**Body22**](Body22.md)| Service metadata object. | [optional] 

### Return type

[**list[ServiceMetadataObject]**](ServiceMetadataObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

