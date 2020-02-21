# polarisgenclient.DeviceInterfaceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_device_device_name_interface_get**](DeviceInterfaceApi.md#api_v01_device_device_name_interface_get) | **GET** /api/v0.1/device/{device_name}/interface | DeviceInterfaceRoute.get
[**api_v01_device_device_name_interface_port_get**](DeviceInterfaceApi.md#api_v01_device_device_name_interface_port_get) | **GET** /api/v0.1/device/{device_name}/interface/{port} | DeviceInterfaceRoute.get
[**api_v01_device_device_name_interface_post**](DeviceInterfaceApi.md#api_v01_device_device_name_interface_post) | **POST** /api/v0.1/device/{device_name}/interface | DeviceInterfaceRoute.post


# **api_v01_device_device_name_interface_get**
> api_v01_device_device_name_interface_get(device_name, port)

DeviceInterfaceRoute.get

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
api_instance = polarisgenclient.DeviceInterfaceApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
port = 'port_example' # str | Device interface port

try:
    # DeviceInterfaceRoute.get
    api_instance.api_v01_device_device_name_interface_get(device_name, port)
except ApiException as e:
    print("Exception when calling DeviceInterfaceApi->api_v01_device_device_name_interface_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **port** | **str**| Device interface port | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_device_name_interface_port_get**
> api_v01_device_device_name_interface_port_get(device_name, port)

DeviceInterfaceRoute.get

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
api_instance = polarisgenclient.DeviceInterfaceApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
port = 'port_example' # str | Device interface port

try:
    # DeviceInterfaceRoute.get
    api_instance.api_v01_device_device_name_interface_port_get(device_name, port)
except ApiException as e:
    print("Exception when calling DeviceInterfaceApi->api_v01_device_device_name_interface_port_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **port** | **str**| Device interface port | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_device_name_interface_post**
> DeviceObject api_v01_device_device_name_interface_post(device_name)

DeviceInterfaceRoute.post

Dispatch real time interface scan

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
api_instance = polarisgenclient.DeviceInterfaceApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN

try:
    # DeviceInterfaceRoute.post
    api_response = api_instance.api_v01_device_device_name_interface_post(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceInterfaceApi->api_v01_device_device_name_interface_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 

### Return type

[**DeviceObject**](DeviceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

