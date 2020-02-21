# polarisgenclient.LldpNeighborApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_device_device_name_lldp_neighbor_get**](LldpNeighborApi.md#api_v01_device_device_name_lldp_neighbor_get) | **GET** /api/v0.1/device/{device_name}/lldp/neighbor | LldpNeighborRoute.get
[**api_v01_device_device_name_lldp_neighbor_post**](LldpNeighborApi.md#api_v01_device_device_name_lldp_neighbor_post) | **POST** /api/v0.1/device/{device_name}/lldp/neighbor | LldpNeighborRoute.post
[**api_v01_lldp_neighbor_get**](LldpNeighborApi.md#api_v01_lldp_neighbor_get) | **GET** /api/v0.1/lldp/neighbor | LldpNeighborRoute.get


# **api_v01_device_device_name_lldp_neighbor_get**
> LLDPNeighborObject api_v01_device_device_name_lldp_neighbor_get(device_name, port=port)

LldpNeighborRoute.get

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
api_instance = polarisgenclient.LldpNeighborApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
port = 'port_example' # str | Device interface port (optional)

try:
    # LldpNeighborRoute.get
    api_response = api_instance.api_v01_device_device_name_lldp_neighbor_get(device_name, port=port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LldpNeighborApi->api_v01_device_device_name_lldp_neighbor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **port** | **str**| Device interface port | [optional] 

### Return type

[**LLDPNeighborObject**](LLDPNeighborObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_device_name_lldp_neighbor_post**
> LLDPNeighborObject api_v01_device_device_name_lldp_neighbor_post(device_name)

LldpNeighborRoute.post

Dispatch real time LLDP neighbor scan

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
api_instance = polarisgenclient.LldpNeighborApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN

try:
    # LldpNeighborRoute.post
    api_response = api_instance.api_v01_device_device_name_lldp_neighbor_post(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LldpNeighborApi->api_v01_device_device_name_lldp_neighbor_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 

### Return type

[**LLDPNeighborObject**](LLDPNeighborObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_lldp_neighbor_get**
> LLDPNeighborObject api_v01_lldp_neighbor_get(device_name, port=port)

LldpNeighborRoute.get

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
api_instance = polarisgenclient.LldpNeighborApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
port = 'port_example' # str | Device interface port (optional)

try:
    # LldpNeighborRoute.get
    api_response = api_instance.api_v01_lldp_neighbor_get(device_name, port=port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LldpNeighborApi->api_v01_lldp_neighbor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **port** | **str**| Device interface port | [optional] 

### Return type

[**LLDPNeighborObject**](LLDPNeighborObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

