# polarisgenclient.BgpProcessApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bgp_process_delete**](BgpProcessApi.md#bgp_process_delete) | **DELETE** /api/v0.1/device/{device_name}/bgp/{as_number} | BgpProcessRoute.delete
[**bgp_process_get**](BgpProcessApi.md#bgp_process_get) | **GET** /api/v0.1/bgp | BgpProcessRoute.get
[**bgp_process_get_by_as**](BgpProcessApi.md#bgp_process_get_by_as) | **GET** /api/v0.1/device/{device_name}/bgp/{as_number} | BgpProcessRoute.get
[**bgp_process_get_by_device**](BgpProcessApi.md#bgp_process_get_by_device) | **GET** /api/v0.1/device/{device_name}/bgp | BgpProcessRoute.get
[**bgp_process_post**](BgpProcessApi.md#bgp_process_post) | **POST** /api/v0.1/bgp | BgpProcessRoute.post
[**bgp_process_put**](BgpProcessApi.md#bgp_process_put) | **PUT** /api/v0.1/device/{device_name}/bgp/{as_number} | BgpProcessRoute.put


# **bgp_process_delete**
> BgpProcessObject bgp_process_delete(device_name, as_number)

BgpProcessRoute.delete

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
api_instance = polarisgenclient.BgpProcessApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | BgpProcess device_name
as_number = 56 # int | BgpProcess as_number

try:
    # BgpProcessRoute.delete
    api_response = api_instance.bgp_process_delete(device_name, as_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpProcessApi->bgp_process_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| BgpProcess device_name | 
 **as_number** | **int**| BgpProcess as_number | 

### Return type

[**BgpProcessObject**](BgpProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_process_get**
> BgpProcessObject bgp_process_get()

BgpProcessRoute.get

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
api_instance = polarisgenclient.BgpProcessApi(polarisgenclient.ApiClient(configuration))

try:
    # BgpProcessRoute.get
    api_response = api_instance.bgp_process_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpProcessApi->bgp_process_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BgpProcessObject**](BgpProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_process_get_by_as**
> BgpProcessObject bgp_process_get_by_as(device_name, as_number)

BgpProcessRoute.get

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
api_instance = polarisgenclient.BgpProcessApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | BgpProcess device_name
as_number = 56 # int | BgpProcess as_number

try:
    # BgpProcessRoute.get
    api_response = api_instance.bgp_process_get_by_as(device_name, as_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpProcessApi->bgp_process_get_by_as: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| BgpProcess device_name | 
 **as_number** | **int**| BgpProcess as_number | 

### Return type

[**BgpProcessObject**](BgpProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_process_get_by_device**
> BgpProcessObject bgp_process_get_by_device(device_name)

BgpProcessRoute.get

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
api_instance = polarisgenclient.BgpProcessApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | BgpProcess device_name

try:
    # BgpProcessRoute.get
    api_response = api_instance.bgp_process_get_by_device(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpProcessApi->bgp_process_get_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| BgpProcess device_name | 

### Return type

[**BgpProcessObject**](BgpProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_process_post**
> BgpProcessObject bgp_process_post(body=body)

BgpProcessRoute.post

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
api_instance = polarisgenclient.BgpProcessApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.BgpProcessObject() # BgpProcessObject | BgpProcess object (optional)

try:
    # BgpProcessRoute.post
    api_response = api_instance.bgp_process_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpProcessApi->bgp_process_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BgpProcessObject**](BgpProcessObject.md)| BgpProcess object | [optional] 

### Return type

[**BgpProcessObject**](BgpProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_process_put**
> BgpProcessObject bgp_process_put(device_name, as_number, body=body)

BgpProcessRoute.put

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
api_instance = polarisgenclient.BgpProcessApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | BgpProcess device_name
as_number = 56 # int | BgpProcess as_number
body = polarisgenclient.BgpProcessObject() # BgpProcessObject | BgpProcess object (optional)

try:
    # BgpProcessRoute.put
    api_response = api_instance.bgp_process_put(device_name, as_number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpProcessApi->bgp_process_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| BgpProcess device_name | 
 **as_number** | **int**| BgpProcess as_number | 
 **body** | [**BgpProcessObject**](BgpProcessObject.md)| BgpProcess object | [optional] 

### Return type

[**BgpProcessObject**](BgpProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

