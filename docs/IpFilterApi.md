# polarisgenclient.IpFilterApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ip_filter_delete**](IpFilterApi.md#ip_filter_delete) | **DELETE** /api/v0.1/ipfilter/{name}/id/{id} | IpFilterRoute.delete
[**ip_filter_get**](IpFilterApi.md#ip_filter_get) | **GET** /api/v0.1/ipfilter | IpFilterRoute.get
[**ip_filter_get_by_id**](IpFilterApi.md#ip_filter_get_by_id) | **GET** /api/v0.1/ipfilter/{name}/id/{id} | IpFilterRoute.get
[**ip_filter_get_by_name**](IpFilterApi.md#ip_filter_get_by_name) | **GET** /api/v0.1/ipfilter/{name} | IpFilterRoute.get
[**ip_filter_post**](IpFilterApi.md#ip_filter_post) | **POST** /api/v0.1/ipfilter | IpFilterRoute.post
[**ip_filter_put**](IpFilterApi.md#ip_filter_put) | **PUT** /api/v0.1/ipfilter/{name}/id/{id} | IpFilterRoute.put


# **ip_filter_delete**
> IpFilterObject ip_filter_delete(name, id)

IpFilterRoute.delete

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
api_instance = polarisgenclient.IpFilterApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | IpFilter name
id = 'id_example' # str | UUID1 string

try:
    # IpFilterRoute.delete
    api_response = api_instance.ip_filter_delete(name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpFilterApi->ip_filter_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| IpFilter name | 
 **id** | **str**| UUID1 string | 

### Return type

[**IpFilterObject**](IpFilterObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_filter_get**
> IpFilterObject ip_filter_get()

IpFilterRoute.get

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
api_instance = polarisgenclient.IpFilterApi(polarisgenclient.ApiClient(configuration))

try:
    # IpFilterRoute.get
    api_response = api_instance.ip_filter_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpFilterApi->ip_filter_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IpFilterObject**](IpFilterObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_filter_get_by_id**
> IpFilterObject ip_filter_get_by_id(name, id)

IpFilterRoute.get

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
api_instance = polarisgenclient.IpFilterApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | IpFilter name
id = 'id_example' # str | IpFilter id

try:
    # IpFilterRoute.get
    api_response = api_instance.ip_filter_get_by_id(name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpFilterApi->ip_filter_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| IpFilter name | 
 **id** | **str**| IpFilter id | 

### Return type

[**IpFilterObject**](IpFilterObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_filter_get_by_name**
> IpFilterObject ip_filter_get_by_name(name)

IpFilterRoute.get

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
api_instance = polarisgenclient.IpFilterApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | IpFilter name

try:
    # IpFilterRoute.get
    api_response = api_instance.ip_filter_get_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpFilterApi->ip_filter_get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| IpFilter name | 

### Return type

[**IpFilterObject**](IpFilterObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_filter_post**
> IpFilterObject ip_filter_post(body=body)

IpFilterRoute.post

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
api_instance = polarisgenclient.IpFilterApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.IpFilterObject() # IpFilterObject | IpFilter object (optional)

try:
    # IpFilterRoute.post
    api_response = api_instance.ip_filter_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpFilterApi->ip_filter_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpFilterObject**](IpFilterObject.md)| IpFilter object | [optional] 

### Return type

[**IpFilterObject**](IpFilterObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_filter_put**
> IpFilterObject ip_filter_put(name, id, body=body)

IpFilterRoute.put

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
api_instance = polarisgenclient.IpFilterApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | IpFilter name
id = 'id_example' # str | UUID1 string
body = polarisgenclient.IpFilterObject() # IpFilterObject | IpFilter object (optional)

try:
    # IpFilterRoute.put
    api_response = api_instance.ip_filter_put(name, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpFilterApi->ip_filter_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| IpFilter name | 
 **id** | **str**| UUID1 string | 
 **body** | [**IpFilterObject**](IpFilterObject.md)| IpFilter object | [optional] 

### Return type

[**IpFilterObject**](IpFilterObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

