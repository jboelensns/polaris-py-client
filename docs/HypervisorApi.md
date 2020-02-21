# polarisgenclient.HypervisorApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hypervisor_get**](HypervisorApi.md#hypervisor_get) | **GET** /api/v0.1/hypervisor | HypervisorRoute.get
[**hypervisor_get_by_device**](HypervisorApi.md#hypervisor_get_by_device) | **GET** /api/v0.1/device/{device_name}/hypervisor | HypervisorRoute.get


# **hypervisor_get**
> HypervisorObject hypervisor_get(mac_address=mac_address)

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
mac_address = 'mac_address_example' # str | MAC address (optional)

try:
    # HypervisorRoute.get
    api_response = api_instance.hypervisor_get(mac_address=mac_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HypervisorApi->hypervisor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mac_address** | **str**| MAC address | [optional] 

### Return type

[**HypervisorObject**](HypervisorObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hypervisor_get_by_device**
> HypervisorObject hypervisor_get_by_device(device_name, mac_address=mac_address)

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
    api_response = api_instance.hypervisor_get_by_device(device_name, mac_address=mac_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HypervisorApi->hypervisor_get_by_device: %s\n" % e)
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

