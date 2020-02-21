# polarisgenclient.ZtpDeviceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_ztp_device_get**](ZtpDeviceApi.md#api_v01_ztp_device_get) | **GET** /api/v0.1/ztp/device | ZtpDeviceRoute.get
[**api_v01_ztp_device_post**](ZtpDeviceApi.md#api_v01_ztp_device_post) | **POST** /api/v0.1/ztp/device | ZtpDeviceRoute.post
[**api_v01_ztp_device_serial_number_delete**](ZtpDeviceApi.md#api_v01_ztp_device_serial_number_delete) | **DELETE** /api/v0.1/ztp/device/{serial_number} | ZtpDeviceRoute.delete
[**api_v01_ztp_device_serial_number_get**](ZtpDeviceApi.md#api_v01_ztp_device_serial_number_get) | **GET** /api/v0.1/ztp/device/{serial_number} | ZtpDeviceRoute.get
[**api_v01_ztp_device_serial_number_put**](ZtpDeviceApi.md#api_v01_ztp_device_serial_number_put) | **PUT** /api/v0.1/ztp/device/{serial_number} | ZtpDeviceRoute.post


# **api_v01_ztp_device_get**
> ZtpDevice api_v01_ztp_device_get(serial_number, uuid=uuid, os_version_operating=os_version_operating, os_version_intended=os_version_intended, system_mac_address=system_mac_address, model_name=model_name, management_ip_address=management_ip_address)

ZtpDeviceRoute.get

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
api_instance = polarisgenclient.ZtpDeviceApi(polarisgenclient.ApiClient(configuration))
serial_number = 'serial_number_example' # str | ZTP device serial number
uuid = 'uuid_example' # str | ZTP device uuid (optional)
os_version_operating = 'os_version_operating_example' # str | ZTP device operating os version (optional)
os_version_intended = 'os_version_intended_example' # str | ZTP device intended os version (optional)
system_mac_address = 'system_mac_address_example' # str | ZTP device system mac address (optional)
model_name = 'model_name_example' # str | ZTP device model name (optional)
management_ip_address = 'management_ip_address_example' # str | ZTP device management IP address (optional)

try:
    # ZtpDeviceRoute.get
    api_response = api_instance.api_v01_ztp_device_get(serial_number, uuid=uuid, os_version_operating=os_version_operating, os_version_intended=os_version_intended, system_mac_address=system_mac_address, model_name=model_name, management_ip_address=management_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZtpDeviceApi->api_v01_ztp_device_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**| ZTP device serial number | 
 **uuid** | **str**| ZTP device uuid | [optional] 
 **os_version_operating** | **str**| ZTP device operating os version | [optional] 
 **os_version_intended** | **str**| ZTP device intended os version | [optional] 
 **system_mac_address** | **str**| ZTP device system mac address | [optional] 
 **model_name** | **str**| ZTP device model name | [optional] 
 **management_ip_address** | **str**| ZTP device management IP address | [optional] 

### Return type

[**ZtpDevice**](ZtpDevice.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_ztp_device_post**
> ZtpDevice api_v01_ztp_device_post(device=device)

ZtpDeviceRoute.post

ZTP device registration

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
api_instance = polarisgenclient.ZtpDeviceApi(polarisgenclient.ApiClient(configuration))
device = polarisgenclient.ZtpDevice() # ZtpDevice | ZTP device object (optional)

try:
    # ZtpDeviceRoute.post
    api_response = api_instance.api_v01_ztp_device_post(device=device)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZtpDeviceApi->api_v01_ztp_device_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**ZtpDevice**](ZtpDevice.md)| ZTP device object | [optional] 

### Return type

[**ZtpDevice**](ZtpDevice.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_ztp_device_serial_number_delete**
> ZtpDevice api_v01_ztp_device_serial_number_delete(serial_number)

ZtpDeviceRoute.delete

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
api_instance = polarisgenclient.ZtpDeviceApi(polarisgenclient.ApiClient(configuration))
serial_number = 'serial_number_example' # str | ZTP device serial number

try:
    # ZtpDeviceRoute.delete
    api_response = api_instance.api_v01_ztp_device_serial_number_delete(serial_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZtpDeviceApi->api_v01_ztp_device_serial_number_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**| ZTP device serial number | 

### Return type

[**ZtpDevice**](ZtpDevice.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_ztp_device_serial_number_get**
> ZtpDevice api_v01_ztp_device_serial_number_get(serial_number, uuid=uuid, os_version_operating=os_version_operating, os_version_intended=os_version_intended, system_mac_address=system_mac_address, model_name=model_name, management_ip_address=management_ip_address)

ZtpDeviceRoute.get

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
api_instance = polarisgenclient.ZtpDeviceApi(polarisgenclient.ApiClient(configuration))
serial_number = 'serial_number_example' # str | ZTP device serial number
uuid = 'uuid_example' # str | ZTP device uuid (optional)
os_version_operating = 'os_version_operating_example' # str | ZTP device operating os version (optional)
os_version_intended = 'os_version_intended_example' # str | ZTP device intended os version (optional)
system_mac_address = 'system_mac_address_example' # str | ZTP device system mac address (optional)
model_name = 'model_name_example' # str | ZTP device model name (optional)
management_ip_address = 'management_ip_address_example' # str | ZTP device management IP address (optional)

try:
    # ZtpDeviceRoute.get
    api_response = api_instance.api_v01_ztp_device_serial_number_get(serial_number, uuid=uuid, os_version_operating=os_version_operating, os_version_intended=os_version_intended, system_mac_address=system_mac_address, model_name=model_name, management_ip_address=management_ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZtpDeviceApi->api_v01_ztp_device_serial_number_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**| ZTP device serial number | 
 **uuid** | **str**| ZTP device uuid | [optional] 
 **os_version_operating** | **str**| ZTP device operating os version | [optional] 
 **os_version_intended** | **str**| ZTP device intended os version | [optional] 
 **system_mac_address** | **str**| ZTP device system mac address | [optional] 
 **model_name** | **str**| ZTP device model name | [optional] 
 **management_ip_address** | **str**| ZTP device management IP address | [optional] 

### Return type

[**ZtpDevice**](ZtpDevice.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_ztp_device_serial_number_put**
> ZtpDevice api_v01_ztp_device_serial_number_put(serial_number, body=body)

ZtpDeviceRoute.post

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
api_instance = polarisgenclient.ZtpDeviceApi(polarisgenclient.ApiClient(configuration))
serial_number = 'serial_number_example' # str | ZTP device serial number
body = polarisgenclient.ZtpDevice() # ZtpDevice | Dns object (optional)

try:
    # ZtpDeviceRoute.post
    api_response = api_instance.api_v01_ztp_device_serial_number_put(serial_number, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZtpDeviceApi->api_v01_ztp_device_serial_number_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**| ZTP device serial number | 
 **body** | [**ZtpDevice**](ZtpDevice.md)| Dns object | [optional] 

### Return type

[**ZtpDevice**](ZtpDevice.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

