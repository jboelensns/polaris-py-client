# polarisgenclient.BgpRouteMapApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_routemap_bgp_get**](BgpRouteMapApi.md#api_v01_routemap_bgp_get) | **GET** /api/v0.1/routemap/bgp | BgpRouteMapRoute.get
[**api_v01_routemap_bgp_post**](BgpRouteMapApi.md#api_v01_routemap_bgp_post) | **POST** /api/v0.1/routemap/bgp | BgpRouteMapRoute.post
[**api_v01_routemap_route_map_id_bgp_get**](BgpRouteMapApi.md#api_v01_routemap_route_map_id_bgp_get) | **GET** /api/v0.1/routemap/{route_map_id}/bgp | BgpRouteMapRoute.get
[**api_v01_routemap_route_map_id_bgp_id_seq_seq_delete**](BgpRouteMapApi.md#api_v01_routemap_route_map_id_bgp_id_seq_seq_delete) | **DELETE** /api/v0.1/routemap/{route_map_id}/bgp/{id}/seq/{seq} | BgpRouteMapRoute.delete
[**api_v01_routemap_route_map_id_bgp_id_seq_seq_put**](BgpRouteMapApi.md#api_v01_routemap_route_map_id_bgp_id_seq_seq_put) | **PUT** /api/v0.1/routemap/{route_map_id}/bgp/{id}/seq/{seq} | BgpRouteMapRoute.put


# **api_v01_routemap_bgp_get**
> BgpRouteMapObject api_v01_routemap_bgp_get(route_map_id)

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
    api_response = api_instance.api_v01_routemap_bgp_get(route_map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpRouteMapApi->api_v01_routemap_bgp_get: %s\n" % e)
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

# **api_v01_routemap_bgp_post**
> BgpRouteMapObject api_v01_routemap_bgp_post(body=body)

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
    api_response = api_instance.api_v01_routemap_bgp_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpRouteMapApi->api_v01_routemap_bgp_post: %s\n" % e)
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

# **api_v01_routemap_route_map_id_bgp_get**
> BgpRouteMapObject api_v01_routemap_route_map_id_bgp_get(route_map_id)

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
    api_response = api_instance.api_v01_routemap_route_map_id_bgp_get(route_map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpRouteMapApi->api_v01_routemap_route_map_id_bgp_get: %s\n" % e)
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

# **api_v01_routemap_route_map_id_bgp_id_seq_seq_delete**
> BgpRouteMapObject api_v01_routemap_route_map_id_bgp_id_seq_seq_delete(route_map_id, id, seq)

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
    api_response = api_instance.api_v01_routemap_route_map_id_bgp_id_seq_seq_delete(route_map_id, id, seq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpRouteMapApi->api_v01_routemap_route_map_id_bgp_id_seq_seq_delete: %s\n" % e)
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

# **api_v01_routemap_route_map_id_bgp_id_seq_seq_put**
> BgpRouteMapObject api_v01_routemap_route_map_id_bgp_id_seq_seq_put(route_map_id, id, seq, body=body)

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
    api_response = api_instance.api_v01_routemap_route_map_id_bgp_id_seq_seq_put(route_map_id, id, seq, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpRouteMapApi->api_v01_routemap_route_map_id_bgp_id_seq_seq_put: %s\n" % e)
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

