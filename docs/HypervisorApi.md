# polarisgenclient.HypervisorApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_device_device_name_hypervisor_get**](HypervisorApi.md#api_v01_device_device_name_hypervisor_get) | **GET** /api/v0.1/device/{device_name}/hypervisor | HypervisorRoute.get
[**api_v01_hypervisor_get**](HypervisorApi.md#api_v01_hypervisor_get) | **GET** /api/v0.1/hypervisor | HypervisorRoute.get


# **api_v01_device_device_name_hypervisor_get**
> HypervisorObject api_v01_device_device_name_hypervisor_get(device_name, mac_address=mac_address)

HypervisorRoute.get

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
api_instance = polarisgenclient.HypervisorApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
mac_address = 'mac_address_example' # str | MAC address (optional)

try:
    # HypervisorRoute.get
    api_response = api_instance.api_v01_device_device_name_hypervisor_get(device_name, mac_address=mac_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HypervisorApi->api_v01_device_device_name_hypervisor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **mac_address** | **str**| MAC address | [optional] 

### Return type

[**HypervisorObject**](HypervisorObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_hypervisor_get**
> HypervisorObject api_v01_hypervisor_get(device_name, mac_address=mac_address)

HypervisorRoute.get

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
api_instance = polarisgenclient.HypervisorApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
mac_address = 'mac_address_example' # str | MAC address (optional)

try:
    # HypervisorRoute.get
    api_response = api_instance.api_v01_hypervisor_get(device_name, mac_address=mac_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HypervisorApi->api_v01_hypervisor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **mac_address** | **str**| MAC address | [optional] 

### Return type

[**HypervisorObject**](HypervisorObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

