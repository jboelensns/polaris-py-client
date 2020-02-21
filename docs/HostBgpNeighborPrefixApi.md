# polarisgenclient.HostBgpNeighborPrefixApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_host_bgp_neighbor_prefix_device_device_name_delete**](HostBgpNeighborPrefixApi.md#api_v01_host_bgp_neighbor_prefix_device_device_name_delete) | **DELETE** /api/v0.1/host/bgp/neighbor/prefix/device/{device_name} | HostBgpNeighborPrefixRoute.delete
[**api_v01_host_bgp_neighbor_prefix_device_device_name_put**](HostBgpNeighborPrefixApi.md#api_v01_host_bgp_neighbor_prefix_device_device_name_put) | **PUT** /api/v0.1/host/bgp/neighbor/prefix/device/{device_name} | HostBgpNeighborPrefixRoute.put
[**api_v01_host_bgp_neighbor_prefix_get**](HostBgpNeighborPrefixApi.md#api_v01_host_bgp_neighbor_prefix_get) | **GET** /api/v0.1/host/bgp/neighbor/prefix | HostBgpNeighborPrefixRoute.get
[**api_v01_host_bgp_neighbor_prefix_post**](HostBgpNeighborPrefixApi.md#api_v01_host_bgp_neighbor_prefix_post) | **POST** /api/v0.1/host/bgp/neighbor/prefix | HostBgpNeighborPrefixRoute.post


# **api_v01_host_bgp_neighbor_prefix_device_device_name_delete**
> HostBgpNeighborPrefixObject api_v01_host_bgp_neighbor_prefix_device_device_name_delete(device_name, prefix, id, neighbor_id)

HostBgpNeighborPrefixRoute.delete

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
api_instance = polarisgenclient.HostBgpNeighborPrefixApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name FQDN
prefix = 'prefix_example' # str | IP Prefix
id = 'id_example' # str | HostBgpNeighborPrefix UUIDv1 id
neighbor_id = 'neighbor_id_example' # str | HostBgpNeighbor UUIDv1 id

try:
    # HostBgpNeighborPrefixRoute.delete
    api_response = api_instance.api_v01_host_bgp_neighbor_prefix_device_device_name_delete(device_name, prefix, id, neighbor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostBgpNeighborPrefixApi->api_v01_host_bgp_neighbor_prefix_device_device_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name FQDN | 
 **prefix** | **str**| IP Prefix | 
 **id** | **str**| HostBgpNeighborPrefix UUIDv1 id | 
 **neighbor_id** | **str**| HostBgpNeighbor UUIDv1 id | 

### Return type

[**HostBgpNeighborPrefixObject**](HostBgpNeighborPrefixObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_host_bgp_neighbor_prefix_device_device_name_put**
> HostBgpNeighborPrefixObject api_v01_host_bgp_neighbor_prefix_device_device_name_put(device_name, application, body=body)

HostBgpNeighborPrefixRoute.put

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
api_instance = polarisgenclient.HostBgpNeighborPrefixApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
application = 'application_example' # str | Application name
body = polarisgenclient.HostBgpNeighborPrefixObject() # HostBgpNeighborPrefixObject | Host BGP Neighbor Prefix object. (optional)

try:
    # HostBgpNeighborPrefixRoute.put
    api_response = api_instance.api_v01_host_bgp_neighbor_prefix_device_device_name_put(device_name, application, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostBgpNeighborPrefixApi->api_v01_host_bgp_neighbor_prefix_device_device_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **application** | **str**| Application name | 
 **body** | [**HostBgpNeighborPrefixObject**](HostBgpNeighborPrefixObject.md)| Host BGP Neighbor Prefix object. | [optional] 

### Return type

[**HostBgpNeighborPrefixObject**](HostBgpNeighborPrefixObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_host_bgp_neighbor_prefix_get**
> list[HostBgpNeighborPrefixObject] api_v01_host_bgp_neighbor_prefix_get(device_name, prefix=prefix)

HostBgpNeighborPrefixRoute.get

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
api_instance = polarisgenclient.HostBgpNeighborPrefixApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
prefix = 'prefix_example' # str | IPv4 or IPv6 prefix (optional)

try:
    # HostBgpNeighborPrefixRoute.get
    api_response = api_instance.api_v01_host_bgp_neighbor_prefix_get(device_name, prefix=prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostBgpNeighborPrefixApi->api_v01_host_bgp_neighbor_prefix_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **prefix** | **str**| IPv4 or IPv6 prefix | [optional] 

### Return type

[**list[HostBgpNeighborPrefixObject]**](HostBgpNeighborPrefixObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_host_bgp_neighbor_prefix_post**
> HostBgpNeighborPrefixObject api_v01_host_bgp_neighbor_prefix_post(body=body)

HostBgpNeighborPrefixRoute.post

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
api_instance = polarisgenclient.HostBgpNeighborPrefixApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.HostBgpNeighborPrefixObject() # HostBgpNeighborPrefixObject | Host BGP Neighbor Prefix object (optional)

try:
    # HostBgpNeighborPrefixRoute.post
    api_response = api_instance.api_v01_host_bgp_neighbor_prefix_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostBgpNeighborPrefixApi->api_v01_host_bgp_neighbor_prefix_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostBgpNeighborPrefixObject**](HostBgpNeighborPrefixObject.md)| Host BGP Neighbor Prefix object | [optional] 

### Return type

[**HostBgpNeighborPrefixObject**](HostBgpNeighborPrefixObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

