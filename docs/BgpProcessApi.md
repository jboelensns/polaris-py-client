# polarisgenclient.BgpProcessApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_bgp_get**](BgpProcessApi.md#api_v01_bgp_get) | **GET** /api/v0.1/bgp | BgpProcessRoute.get
[**api_v01_bgp_post**](BgpProcessApi.md#api_v01_bgp_post) | **POST** /api/v0.1/bgp | BgpProcessRoute.post
[**api_v01_device_device_name_bgp_as_number_delete**](BgpProcessApi.md#api_v01_device_device_name_bgp_as_number_delete) | **DELETE** /api/v0.1/device/{device_name}/bgp/{as_number} | BgpProcessRoute.delete
[**api_v01_device_device_name_bgp_as_number_put**](BgpProcessApi.md#api_v01_device_device_name_bgp_as_number_put) | **PUT** /api/v0.1/device/{device_name}/bgp/{as_number} | BgpProcessRoute.put


# **api_v01_bgp_get**
> BgpProcessObject api_v01_bgp_get(device_name, as_number)

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
    api_response = api_instance.api_v01_bgp_get(device_name, as_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpProcessApi->api_v01_bgp_get: %s\n" % e)
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

# **api_v01_bgp_post**
> BgpProcessObject api_v01_bgp_post(body=body)

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
    api_response = api_instance.api_v01_bgp_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpProcessApi->api_v01_bgp_post: %s\n" % e)
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

# **api_v01_device_device_name_bgp_as_number_delete**
> BgpProcessObject api_v01_device_device_name_bgp_as_number_delete(device_name, as_number)

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
    api_response = api_instance.api_v01_device_device_name_bgp_as_number_delete(device_name, as_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpProcessApi->api_v01_device_device_name_bgp_as_number_delete: %s\n" % e)
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

# **api_v01_device_device_name_bgp_as_number_put**
> BgpProcessObject api_v01_device_device_name_bgp_as_number_put(device_name, as_number, body=body)

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
    api_response = api_instance.api_v01_device_device_name_bgp_as_number_put(device_name, as_number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpProcessApi->api_v01_device_device_name_bgp_as_number_put: %s\n" % e)
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

