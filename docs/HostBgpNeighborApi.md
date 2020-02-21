# polarisgenclient.HostBgpNeighborApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_host_bgp_neighbor_device_device_name_application_application_delete**](HostBgpNeighborApi.md#api_v01_host_bgp_neighbor_device_device_name_application_application_delete) | **DELETE** /api/v0.1/host/bgp/neighbor/device/{device_name}/application/{application} | HostBgpNeighborRoute.delete
[**api_v01_host_bgp_neighbor_device_device_name_application_application_put**](HostBgpNeighborApi.md#api_v01_host_bgp_neighbor_device_device_name_application_application_put) | **PUT** /api/v0.1/host/bgp/neighbor/device/{device_name}/application/{application} | HostBgpNeighborRoute.put
[**api_v01_host_bgp_neighbor_get**](HostBgpNeighborApi.md#api_v01_host_bgp_neighbor_get) | **GET** /api/v0.1/host/bgp/neighbor | HostBgpNeighborRoute.get
[**api_v01_host_bgp_neighbor_post**](HostBgpNeighborApi.md#api_v01_host_bgp_neighbor_post) | **POST** /api/v0.1/host/bgp/neighbor | HostBgpNeighborRoute.post


# **api_v01_host_bgp_neighbor_device_device_name_application_application_delete**
> HostBgpNeighborObject api_v01_host_bgp_neighbor_device_device_name_application_application_delete(device_name, application, id)

HostBgpNeighborRoute.delete

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
api_instance = polarisgenclient.HostBgpNeighborApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name FQDN
application = 'application_example' # str | Application name
id = 'id_example' # str | HostBgpNeighbor UUIDv1 id

try:
    # HostBgpNeighborRoute.delete
    api_response = api_instance.api_v01_host_bgp_neighbor_device_device_name_application_application_delete(device_name, application, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostBgpNeighborApi->api_v01_host_bgp_neighbor_device_device_name_application_application_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name FQDN | 
 **application** | **str**| Application name | 
 **id** | **str**| HostBgpNeighbor UUIDv1 id | 

### Return type

[**HostBgpNeighborObject**](HostBgpNeighborObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_host_bgp_neighbor_device_device_name_application_application_put**
> HostBgpNeighborObject api_v01_host_bgp_neighbor_device_device_name_application_application_put(device_name, application, id)

HostBgpNeighborRoute.put

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
api_instance = polarisgenclient.HostBgpNeighborApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name FQDN
application = 'application_example' # str | Application name
id = 'id_example' # str | HostBgpNeighbor UUIDv1 id

try:
    # HostBgpNeighborRoute.put
    api_response = api_instance.api_v01_host_bgp_neighbor_device_device_name_application_application_put(device_name, application, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostBgpNeighborApi->api_v01_host_bgp_neighbor_device_device_name_application_application_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name FQDN | 
 **application** | **str**| Application name | 
 **id** | **str**| HostBgpNeighbor UUIDv1 id | 

### Return type

[**HostBgpNeighborObject**](HostBgpNeighborObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_host_bgp_neighbor_get**
> HostBgpNeighborObject api_v01_host_bgp_neighbor_get(device_name, application=application)

HostBgpNeighborRoute.get

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
api_instance = polarisgenclient.HostBgpNeighborApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
application = 'application_example' # str | Application name (optional)

try:
    # HostBgpNeighborRoute.get
    api_response = api_instance.api_v01_host_bgp_neighbor_get(device_name, application=application)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostBgpNeighborApi->api_v01_host_bgp_neighbor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **application** | **str**| Application name | [optional] 

### Return type

[**HostBgpNeighborObject**](HostBgpNeighborObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_host_bgp_neighbor_post**
> HostBgpNeighborObject api_v01_host_bgp_neighbor_post(body=body)

HostBgpNeighborRoute.post

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
api_instance = polarisgenclient.HostBgpNeighborApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.HostBgpNeighborObject() # HostBgpNeighborObject | Host BGP Neighbor object. (optional)

try:
    # HostBgpNeighborRoute.post
    api_response = api_instance.api_v01_host_bgp_neighbor_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostBgpNeighborApi->api_v01_host_bgp_neighbor_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostBgpNeighborObject**](HostBgpNeighborObject.md)| Host BGP Neighbor object. | [optional] 

### Return type

[**HostBgpNeighborObject**](HostBgpNeighborObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

