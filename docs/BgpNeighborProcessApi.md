# polarisgenclient.BgpNeighborProcessApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bgp_neighbor_process_delete**](BgpNeighborProcessApi.md#bgp_neighbor_process_delete) | **DELETE** /api/v0.1/device/{device_name}/bgp/{as_number}/neighbor/{ip_address}/process | BgpNeighborProcessRoute.delete
[**bgp_neighbor_process_get**](BgpNeighborProcessApi.md#bgp_neighbor_process_get) | **GET** /api/v0.1/bgp/neighbor/process | BgpNeighborProcessRoute.get
[**bgp_neighbor_process_get_by_as**](BgpNeighborProcessApi.md#bgp_neighbor_process_get_by_as) | **GET** /api/v0.1/device/{device_name}/bgp/{as_number}/neighbor/{ip_address}/process | BgpNeighborProcessRoute.get
[**bgp_neighbor_process_post**](BgpNeighborProcessApi.md#bgp_neighbor_process_post) | **POST** /api/v0.1/bgp/neighbor/process | BgpNeighborProcessRoute.post
[**bgp_neighbor_process_put**](BgpNeighborProcessApi.md#bgp_neighbor_process_put) | **PUT** /api/v0.1/device/{device_name}/bgp/{as_number}/neighbor/{ip_address}/process | BgpNeighborProcessRoute.put


# **bgp_neighbor_process_delete**
> BgpNeighborProcessObject bgp_neighbor_process_delete(device_name, as_number, ip_address)

BgpNeighborProcessRoute.delete

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
api_instance = polarisgenclient.BgpNeighborProcessApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | BgpNeighborProcess device_name
as_number = 56 # int | BgpNeighborProcess as_number
ip_address = 'ip_address_example' # str | BgpNeighborProcess ip_address

try:
    # BgpNeighborProcessRoute.delete
    api_response = api_instance.bgp_neighbor_process_delete(device_name, as_number, ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpNeighborProcessApi->bgp_neighbor_process_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| BgpNeighborProcess device_name | 
 **as_number** | **int**| BgpNeighborProcess as_number | 
 **ip_address** | **str**| BgpNeighborProcess ip_address | 

### Return type

[**BgpNeighborProcessObject**](BgpNeighborProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_neighbor_process_get**
> BgpNeighborProcessObject bgp_neighbor_process_get()

BgpNeighborProcessRoute.get

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
api_instance = polarisgenclient.BgpNeighborProcessApi(polarisgenclient.ApiClient(configuration))

try:
    # BgpNeighborProcessRoute.get
    api_response = api_instance.bgp_neighbor_process_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpNeighborProcessApi->bgp_neighbor_process_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BgpNeighborProcessObject**](BgpNeighborProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_neighbor_process_get_by_as**
> BgpNeighborProcessObject bgp_neighbor_process_get_by_as(device_name, as_number, ip_address)

BgpNeighborProcessRoute.get

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
api_instance = polarisgenclient.BgpNeighborProcessApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | BgpNeighborProcess device_name
as_number = 56 # int | BgpNeighborProcess as_number
ip_address = 'ip_address_example' # str | BgpNeighborProcess ip address

try:
    # BgpNeighborProcessRoute.get
    api_response = api_instance.bgp_neighbor_process_get_by_as(device_name, as_number, ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpNeighborProcessApi->bgp_neighbor_process_get_by_as: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| BgpNeighborProcess device_name | 
 **as_number** | **int**| BgpNeighborProcess as_number | 
 **ip_address** | **str**| BgpNeighborProcess ip address | 

### Return type

[**BgpNeighborProcessObject**](BgpNeighborProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_neighbor_process_post**
> BgpNeighborProcessObject bgp_neighbor_process_post(body=body)

BgpNeighborProcessRoute.post

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
api_instance = polarisgenclient.BgpNeighborProcessApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.BgpNeighborProcessObject() # BgpNeighborProcessObject | BgpNeighborProcess object (optional)

try:
    # BgpNeighborProcessRoute.post
    api_response = api_instance.bgp_neighbor_process_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpNeighborProcessApi->bgp_neighbor_process_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BgpNeighborProcessObject**](BgpNeighborProcessObject.md)| BgpNeighborProcess object | [optional] 

### Return type

[**BgpNeighborProcessObject**](BgpNeighborProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_neighbor_process_put**
> BgpNeighborProcessObject bgp_neighbor_process_put(device_name, as_number, ip_address, body=body)

BgpNeighborProcessRoute.put

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
api_instance = polarisgenclient.BgpNeighborProcessApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | BgpNeighborProcess device_name
as_number = 56 # int | BgpNeighborProcess as_number
ip_address = 'ip_address_example' # str | BgpNeighborProcess ip_address
body = polarisgenclient.BgpNeighborProcessObject() # BgpNeighborProcessObject | BgpNeighborProcess object (optional)

try:
    # BgpNeighborProcessRoute.put
    api_response = api_instance.bgp_neighbor_process_put(device_name, as_number, ip_address, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpNeighborProcessApi->bgp_neighbor_process_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| BgpNeighborProcess device_name | 
 **as_number** | **int**| BgpNeighborProcess as_number | 
 **ip_address** | **str**| BgpNeighborProcess ip_address | 
 **body** | [**BgpNeighborProcessObject**](BgpNeighborProcessObject.md)| BgpNeighborProcess object | [optional] 

### Return type

[**BgpNeighborProcessObject**](BgpNeighborProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

