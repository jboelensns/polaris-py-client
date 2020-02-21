# polarisgenclient.OspfNeighborApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_device_device_name_ospf_neighbor_get**](OspfNeighborApi.md#api_v01_device_device_name_ospf_neighbor_get) | **GET** /api/v0.1/device/{device_name}/ospf/neighbor | OspfNeighborRoute.get
[**api_v01_device_device_name_ospf_neighbor_post**](OspfNeighborApi.md#api_v01_device_device_name_ospf_neighbor_post) | **POST** /api/v0.1/device/{device_name}/ospf/neighbor | OspfNeighborRoute.post
[**api_v01_ospf_neighbor_get**](OspfNeighborApi.md#api_v01_ospf_neighbor_get) | **GET** /api/v0.1/ospf/neighbor | OspfNeighborRoute.get


# **api_v01_device_device_name_ospf_neighbor_get**
> OSPFNeighborObject api_v01_device_device_name_ospf_neighbor_get(device_name, port=port)

OspfNeighborRoute.get

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
api_instance = polarisgenclient.OspfNeighborApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
port = 'port_example' # str | Device interface port (optional)

try:
    # OspfNeighborRoute.get
    api_response = api_instance.api_v01_device_device_name_ospf_neighbor_get(device_name, port=port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OspfNeighborApi->api_v01_device_device_name_ospf_neighbor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **port** | **str**| Device interface port | [optional] 

### Return type

[**OSPFNeighborObject**](OSPFNeighborObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_device_name_ospf_neighbor_post**
> api_v01_device_device_name_ospf_neighbor_post(device_name)

OspfNeighborRoute.post

Dispatch real time OSPF neighbor scan

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
api_instance = polarisgenclient.OspfNeighborApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN

try:
    # OspfNeighborRoute.post
    api_instance.api_v01_device_device_name_ospf_neighbor_post(device_name)
except ApiException as e:
    print("Exception when calling OspfNeighborApi->api_v01_device_device_name_ospf_neighbor_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_ospf_neighbor_get**
> OSPFNeighborObject api_v01_ospf_neighbor_get(device_name, port=port)

OspfNeighborRoute.get

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
api_instance = polarisgenclient.OspfNeighborApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
port = 'port_example' # str | Device interface port (optional)

try:
    # OspfNeighborRoute.get
    api_response = api_instance.api_v01_ospf_neighbor_get(device_name, port=port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OspfNeighborApi->api_v01_ospf_neighbor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **port** | **str**| Device interface port | [optional] 

### Return type

[**OSPFNeighborObject**](OSPFNeighborObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

