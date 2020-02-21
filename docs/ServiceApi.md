# polarisgenclient.ServiceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_service_get**](ServiceApi.md#api_v01_service_get) | **GET** /api/v0.1/service | ServiceRoute.get
[**api_v01_service_name_id_id_delete**](ServiceApi.md#api_v01_service_name_id_id_delete) | **DELETE** /api/v0.1/service/{name}/id/{id} | ServiceRoute.delete
[**api_v01_service_name_id_id_put**](ServiceApi.md#api_v01_service_name_id_id_put) | **PUT** /api/v0.1/service/{name}/id/{id} | ServiceRoute.put
[**api_v01_service_post**](ServiceApi.md#api_v01_service_post) | **POST** /api/v0.1/service | ServiceRoute.post


# **api_v01_service_get**
> ServiceObject api_v01_service_get(name, id)

ServiceRoute.get

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
api_instance = polarisgenclient.ServiceApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Service name
id = 'id_example' # str | Service id

try:
    # ServiceRoute.get
    api_response = api_instance.api_v01_service_get(name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v01_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Service name | 
 **id** | **str**| Service id | 

### Return type

[**ServiceObject**](ServiceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_service_name_id_id_delete**
> ServiceObject api_v01_service_name_id_id_delete(name, id)

ServiceRoute.delete

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
api_instance = polarisgenclient.ServiceApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Service name
id = 'id_example' # str | UUID1 string

try:
    # ServiceRoute.delete
    api_response = api_instance.api_v01_service_name_id_id_delete(name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v01_service_name_id_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Service name | 
 **id** | **str**| UUID1 string | 

### Return type

[**ServiceObject**](ServiceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_service_name_id_id_put**
> ServiceObject api_v01_service_name_id_id_put(name, id, body=body)

ServiceRoute.put

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
api_instance = polarisgenclient.ServiceApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Service name
id = 'id_example' # str | UUID1 string
body = polarisgenclient.ServiceObject() # ServiceObject | Service object (optional)

try:
    # ServiceRoute.put
    api_response = api_instance.api_v01_service_name_id_id_put(name, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v01_service_name_id_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Service name | 
 **id** | **str**| UUID1 string | 
 **body** | [**ServiceObject**](ServiceObject.md)| Service object | [optional] 

### Return type

[**ServiceObject**](ServiceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_service_post**
> ServiceObject api_v01_service_post(body=body)

ServiceRoute.post

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
api_instance = polarisgenclient.ServiceApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.ServiceObject() # ServiceObject | Service object (optional)

try:
    # ServiceRoute.post
    api_response = api_instance.api_v01_service_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceApi->api_v01_service_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceObject**](ServiceObject.md)| Service object | [optional] 

### Return type

[**ServiceObject**](ServiceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

