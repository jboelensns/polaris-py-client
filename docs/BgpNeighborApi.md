# polarisgenclient.BgpNeighborApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bgp_neighbor_get**](BgpNeighborApi.md#bgp_neighbor_get) | **GET** /api/v0.1/bgp/neighbor | BgpNeighborRoute.get
[**bgp_neighbor_get_by_device**](BgpNeighborApi.md#bgp_neighbor_get_by_device) | **GET** /api/v0.1/device/{device_name}/bgp/neighbor | BgpNeighborRoute.get
[**bgp_neighbor_post**](BgpNeighborApi.md#bgp_neighbor_post) | **POST** /api/v0.1/device/{device_name}/bgp/neighbor | BgpNeighborRoute.post


# **bgp_neighbor_get**
> DeviceBGPNeighborResponse bgp_neighbor_get()

BgpNeighborRoute.get

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
api_instance = polarisgenclient.BgpNeighborApi(polarisgenclient.ApiClient(configuration))

try:
    # BgpNeighborRoute.get
    api_response = api_instance.bgp_neighbor_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpNeighborApi->bgp_neighbor_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeviceBGPNeighborResponse**](DeviceBGPNeighborResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_neighbor_get_by_device**
> DeviceBGPNeighborResponse bgp_neighbor_get_by_device(device_name)

BgpNeighborRoute.get

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
api_instance = polarisgenclient.BgpNeighborApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN

try:
    # BgpNeighborRoute.get
    api_response = api_instance.bgp_neighbor_get_by_device(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpNeighborApi->bgp_neighbor_get_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 

### Return type

[**DeviceBGPNeighborResponse**](DeviceBGPNeighborResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_neighbor_post**
> DeviceBGPNeighborResponse bgp_neighbor_post(device_name)

BgpNeighborRoute.post

Dispatch real time ARP scan

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
api_instance = polarisgenclient.BgpNeighborApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN

try:
    # BgpNeighborRoute.post
    api_response = api_instance.bgp_neighbor_post(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpNeighborApi->bgp_neighbor_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 

### Return type

[**DeviceBGPNeighborResponse**](DeviceBGPNeighborResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

