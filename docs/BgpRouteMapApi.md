# polarisgenclient.BgpRouteMapApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bgp_route_map_delete**](BgpRouteMapApi.md#bgp_route_map_delete) | **DELETE** /api/v0.1/routemap/{route_map_id}/bgp/{id}/seq/{seq} | BgpRouteMapRoute.delete
[**bgp_route_map_get**](BgpRouteMapApi.md#bgp_route_map_get) | **GET** /api/v0.1/routemap/bgp | BgpRouteMapRoute.get
[**bgp_route_map_get_by_id**](BgpRouteMapApi.md#bgp_route_map_get_by_id) | **GET** /api/v0.1/routemap/{route_map_id}/bgp | BgpRouteMapRoute.get
[**bgp_route_map_post**](BgpRouteMapApi.md#bgp_route_map_post) | **POST** /api/v0.1/routemap/bgp | BgpRouteMapRoute.post
[**bgp_route_map_put**](BgpRouteMapApi.md#bgp_route_map_put) | **PUT** /api/v0.1/routemap/{route_map_id}/bgp/{id}/seq/{seq} | BgpRouteMapRoute.put


# **bgp_route_map_delete**
> BgpRouteMapObject bgp_route_map_delete(route_map_id, id, seq)

BgpRouteMapRoute.delete

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
api_instance = polarisgenclient.BgpRouteMapApi(polarisgenclient.ApiClient(configuration))
route_map_id = 'route_map_id_example' # str | RouteMap id
id = 'id_example' # str | UUID1 string
seq = 56 # int | seq

try:
    # BgpRouteMapRoute.delete
    api_response = api_instance.bgp_route_map_delete(route_map_id, id, seq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpRouteMapApi->bgp_route_map_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_map_id** | **str**| RouteMap id | 
 **id** | **str**| UUID1 string | 
 **seq** | **int**| seq | 

### Return type

[**BgpRouteMapObject**](BgpRouteMapObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_route_map_get**
> BgpRouteMapObject bgp_route_map_get()

BgpRouteMapRoute.get

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
api_instance = polarisgenclient.BgpRouteMapApi(polarisgenclient.ApiClient(configuration))

try:
    # BgpRouteMapRoute.get
    api_response = api_instance.bgp_route_map_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpRouteMapApi->bgp_route_map_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BgpRouteMapObject**](BgpRouteMapObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_route_map_get_by_id**
> BgpRouteMapObject bgp_route_map_get_by_id(route_map_id)

BgpRouteMapRoute.get

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
api_instance = polarisgenclient.BgpRouteMapApi(polarisgenclient.ApiClient(configuration))
route_map_id = 'route_map_id_example' # str | RouteMap id

try:
    # BgpRouteMapRoute.get
    api_response = api_instance.bgp_route_map_get_by_id(route_map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpRouteMapApi->bgp_route_map_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_map_id** | **str**| RouteMap id | 

### Return type

[**BgpRouteMapObject**](BgpRouteMapObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_route_map_post**
> BgpRouteMapObject bgp_route_map_post(body=body)

BgpRouteMapRoute.post

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
api_instance = polarisgenclient.BgpRouteMapApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.BgpRouteMapObject() # BgpRouteMapObject | BgpRouteMap object (optional)

try:
    # BgpRouteMapRoute.post
    api_response = api_instance.bgp_route_map_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpRouteMapApi->bgp_route_map_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BgpRouteMapObject**](BgpRouteMapObject.md)| BgpRouteMap object | [optional] 

### Return type

[**BgpRouteMapObject**](BgpRouteMapObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_route_map_put**
> BgpRouteMapObject bgp_route_map_put(route_map_id, id, seq, body=body)

BgpRouteMapRoute.put

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
api_instance = polarisgenclient.BgpRouteMapApi(polarisgenclient.ApiClient(configuration))
route_map_id = 'route_map_id_example' # str | RouteMap id
id = 'id_example' # str | UUID1 string
seq = 56 # int | seq
body = polarisgenclient.BgpRouteMapObject() # BgpRouteMapObject | BgpRouteMap object (optional)

try:
    # BgpRouteMapRoute.put
    api_response = api_instance.bgp_route_map_put(route_map_id, id, seq, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpRouteMapApi->bgp_route_map_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_map_id** | **str**| RouteMap id | 
 **id** | **str**| UUID1 string | 
 **seq** | **int**| seq | 
 **body** | [**BgpRouteMapObject**](BgpRouteMapObject.md)| BgpRouteMap object | [optional] 

### Return type

[**BgpRouteMapObject**](BgpRouteMapObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

