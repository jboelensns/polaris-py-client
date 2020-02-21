# polarisgenclient.RouteMapApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_routemap_get**](RouteMapApi.md#api_v01_routemap_get) | **GET** /api/v0.1/routemap | RouteMapRoute.get
[**api_v01_routemap_name_id_id_delete**](RouteMapApi.md#api_v01_routemap_name_id_id_delete) | **DELETE** /api/v0.1/routemap/{name}/id/{id} | RouteMapRoute.delete
[**api_v01_routemap_name_id_id_put**](RouteMapApi.md#api_v01_routemap_name_id_id_put) | **PUT** /api/v0.1/routemap/{name}/id/{id} | RouteMapRoute.put
[**api_v01_routemap_post**](RouteMapApi.md#api_v01_routemap_post) | **POST** /api/v0.1/routemap | RouteMapRoute.post


# **api_v01_routemap_get**
> RouteMapObject api_v01_routemap_get(name, id)

RouteMapRoute.get

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
api_instance = polarisgenclient.RouteMapApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | RouteMap name
id = 'id_example' # str | RouteMap id

try:
    # RouteMapRoute.get
    api_response = api_instance.api_v01_routemap_get(name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteMapApi->api_v01_routemap_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| RouteMap name | 
 **id** | **str**| RouteMap id | 

### Return type

[**RouteMapObject**](RouteMapObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_routemap_name_id_id_delete**
> RouteMapObject api_v01_routemap_name_id_id_delete(name, id)

RouteMapRoute.delete

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
api_instance = polarisgenclient.RouteMapApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | RouteMap name
id = 'id_example' # str | UUID1 string

try:
    # RouteMapRoute.delete
    api_response = api_instance.api_v01_routemap_name_id_id_delete(name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteMapApi->api_v01_routemap_name_id_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| RouteMap name | 
 **id** | **str**| UUID1 string | 

### Return type

[**RouteMapObject**](RouteMapObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_routemap_name_id_id_put**
> RouteMapObject api_v01_routemap_name_id_id_put(name, id, body=body)

RouteMapRoute.put

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
api_instance = polarisgenclient.RouteMapApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | RouteMap name
id = 'id_example' # str | UUID1 string
body = polarisgenclient.RouteMapObject() # RouteMapObject | RouteMap object (optional)

try:
    # RouteMapRoute.put
    api_response = api_instance.api_v01_routemap_name_id_id_put(name, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteMapApi->api_v01_routemap_name_id_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| RouteMap name | 
 **id** | **str**| UUID1 string | 
 **body** | [**RouteMapObject**](RouteMapObject.md)| RouteMap object | [optional] 

### Return type

[**RouteMapObject**](RouteMapObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_routemap_post**
> RouteMapObject api_v01_routemap_post(body=body)

RouteMapRoute.post

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
api_instance = polarisgenclient.RouteMapApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.RouteMapObject() # RouteMapObject | RouteMap object (optional)

try:
    # RouteMapRoute.post
    api_response = api_instance.api_v01_routemap_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteMapApi->api_v01_routemap_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RouteMapObject**](RouteMapObject.md)| RouteMap object | [optional] 

### Return type

[**RouteMapObject**](RouteMapObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

