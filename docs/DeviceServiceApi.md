# polarisgenclient.DeviceServiceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_service_delete**](DeviceServiceApi.md#device_service_delete) | **DELETE** /api/v0.1/device/{name}/service/{id} | DeviceServiceRoute.delete
[**device_service_get**](DeviceServiceApi.md#device_service_get) | **GET** /api/v0.1/device/{name}/service | DeviceServiceRoute.get
[**device_service_get_by_id**](DeviceServiceApi.md#device_service_get_by_id) | **GET** /api/v0.1/device/{name}/service/{id} | DeviceServiceRoute.get
[**device_service_post**](DeviceServiceApi.md#device_service_post) | **POST** /api/v0.1/device/{name}/service | DeviceServiceRoute.post
[**device_service_put**](DeviceServiceApi.md#device_service_put) | **PUT** /api/v0.1/device/{name}/service/{id} | DeviceServiceRoute.put


# **device_service_delete**
> DeviceServiceObject device_service_delete(name, id)

DeviceServiceRoute.delete

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
api_instance = polarisgenclient.DeviceServiceApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Device name
id = 'id_example' # str | UUID1 string

try:
    # DeviceServiceRoute.delete
    api_response = api_instance.device_service_delete(name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->device_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Device name | 
 **id** | **str**| UUID1 string | 

### Return type

[**DeviceServiceObject**](DeviceServiceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_service_get**
> DeviceServiceObject device_service_get(name, pop_name=pop_name)

DeviceServiceRoute.get

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
api_instance = polarisgenclient.DeviceServiceApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | DeviceService name
pop_name = 'pop_name_example' # str | DeviceService Pop name (optional)

try:
    # DeviceServiceRoute.get
    api_response = api_instance.device_service_get(name, pop_name=pop_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->device_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| DeviceService name | 
 **pop_name** | **str**| DeviceService Pop name | [optional] 

### Return type

[**DeviceServiceObject**](DeviceServiceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_service_get_by_id**
> DeviceServiceObject device_service_get_by_id(name, id, pop_name=pop_name)

DeviceServiceRoute.get

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
api_instance = polarisgenclient.DeviceServiceApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | DeviceService name
id = 'id_example' # str | DeviceService id
pop_name = 'pop_name_example' # str | DeviceService Pop name (optional)

try:
    # DeviceServiceRoute.get
    api_response = api_instance.device_service_get_by_id(name, id, pop_name=pop_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->device_service_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| DeviceService name | 
 **id** | **str**| DeviceService id | 
 **pop_name** | **str**| DeviceService Pop name | [optional] 

### Return type

[**DeviceServiceObject**](DeviceServiceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_service_post**
> DeviceServiceObject device_service_post(name, body=body)

DeviceServiceRoute.post

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
api_instance = polarisgenclient.DeviceServiceApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | 
body = polarisgenclient.DeviceServiceObject() # DeviceServiceObject | Service object (optional)

try:
    # DeviceServiceRoute.post
    api_response = api_instance.device_service_post(name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->device_service_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | [**DeviceServiceObject**](DeviceServiceObject.md)| Service object | [optional] 

### Return type

[**DeviceServiceObject**](DeviceServiceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_service_put**
> DeviceServiceObject device_service_put(name, id, body=body)

DeviceServiceRoute.put

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
api_instance = polarisgenclient.DeviceServiceApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Device name
id = 'id_example' # str | UUID1 string
body = polarisgenclient.DeviceServiceObject() # DeviceServiceObject | DeviceService object (optional)

try:
    # DeviceServiceRoute.put
    api_response = api_instance.device_service_put(name, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->device_service_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Device name | 
 **id** | **str**| UUID1 string | 
 **body** | [**DeviceServiceObject**](DeviceServiceObject.md)| DeviceService object | [optional] 

### Return type

[**DeviceServiceObject**](DeviceServiceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

