# polarisgenclient.DeviceInterfaceAlarmApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_interface_alarm_get**](DeviceInterfaceAlarmApi.md#device_interface_alarm_get) | **GET** /api/v0.1/interface/alarm | DeviceInterfaceAlarmRoute.get
[**device_interface_alarm_get_by_device**](DeviceInterfaceAlarmApi.md#device_interface_alarm_get_by_device) | **GET** /api/v0.1/device/{device_name}/interface/alarm | DeviceInterfaceAlarmRoute.get


# **device_interface_alarm_get**
> DeviceInterfaceAlarmObject device_interface_alarm_get()

DeviceInterfaceAlarmRoute.get

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
api_instance = polarisgenclient.DeviceInterfaceAlarmApi(polarisgenclient.ApiClient(configuration))

try:
    # DeviceInterfaceAlarmRoute.get
    api_response = api_instance.device_interface_alarm_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceInterfaceAlarmApi->device_interface_alarm_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DeviceInterfaceAlarmObject**](DeviceInterfaceAlarmObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_interface_alarm_get_by_device**
> DeviceInterfaceAlarmObject device_interface_alarm_get_by_device(device_name)

DeviceInterfaceAlarmRoute.get

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
api_instance = polarisgenclient.DeviceInterfaceAlarmApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN

try:
    # DeviceInterfaceAlarmRoute.get
    api_response = api_instance.device_interface_alarm_get_by_device(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceInterfaceAlarmApi->device_interface_alarm_get_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 

### Return type

[**DeviceInterfaceAlarmObject**](DeviceInterfaceAlarmObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

