# polarisgenclient.VlanInterfaceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vlan_interface_delete**](VlanInterfaceApi.md#vlan_interface_delete) | **DELETE** /api/v0.1/device/{device_name}/vlan/{num}/interface | VlanInterfaceRoute.delete
[**vlan_interface_get**](VlanInterfaceApi.md#vlan_interface_get) | **GET** /api/v0.1/vlan/interface | VlanInterfaceRoute.get
[**vlan_interface_get_by_num**](VlanInterfaceApi.md#vlan_interface_get_by_num) | **GET** /api/v0.1/device/{device_name}/vlan/{num}/interface | VlanInterfaceRoute.get
[**vlan_interface_post**](VlanInterfaceApi.md#vlan_interface_post) | **POST** /api/v0.1/vlan/interface | VlanInterfaceRoute.post
[**vlan_interface_put**](VlanInterfaceApi.md#vlan_interface_put) | **PUT** /api/v0.1/device/{device_name}/vlan/{num}/interface | VlanInterfaceRoute.put


# **vlan_interface_delete**
> VlanInterfaceObject vlan_interface_delete(device_name, num, port)

VlanInterfaceRoute.delete

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
api_instance = polarisgenclient.VlanInterfaceApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
num = 56 # int | Vlan number
port = 'port_example' # str | VlanInterface port

try:
    # VlanInterfaceRoute.delete
    api_response = api_instance.vlan_interface_delete(device_name, num, port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VlanInterfaceApi->vlan_interface_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **num** | **int**| Vlan number | 
 **port** | **str**| VlanInterface port | 

### Return type

[**VlanInterfaceObject**](VlanInterfaceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vlan_interface_get**
> VlanInterfaceObject vlan_interface_get(device_name, port=port)

VlanInterfaceRoute.get

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
api_instance = polarisgenclient.VlanInterfaceApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
port = 'port_example' # str | VlanInterface port (optional)

try:
    # VlanInterfaceRoute.get
    api_response = api_instance.vlan_interface_get(device_name, port=port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VlanInterfaceApi->vlan_interface_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **port** | **str**| VlanInterface port | [optional] 

### Return type

[**VlanInterfaceObject**](VlanInterfaceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vlan_interface_get_by_num**
> VlanInterfaceObject vlan_interface_get_by_num(device_name, num, port=port)

VlanInterfaceRoute.get

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
api_instance = polarisgenclient.VlanInterfaceApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
num = 56 # int | VlanInterface number
port = 'port_example' # str | VlanInterface port (optional)

try:
    # VlanInterfaceRoute.get
    api_response = api_instance.vlan_interface_get_by_num(device_name, num, port=port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VlanInterfaceApi->vlan_interface_get_by_num: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **num** | **int**| VlanInterface number | 
 **port** | **str**| VlanInterface port | [optional] 

### Return type

[**VlanInterfaceObject**](VlanInterfaceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vlan_interface_post**
> VlanInterfaceObject vlan_interface_post(interface=interface)

VlanInterfaceRoute.post

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
api_instance = polarisgenclient.VlanInterfaceApi(polarisgenclient.ApiClient(configuration))
interface = polarisgenclient.VlanInterfaceObject() # VlanInterfaceObject | VlanInterface object (optional)

try:
    # VlanInterfaceRoute.post
    api_response = api_instance.vlan_interface_post(interface=interface)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VlanInterfaceApi->vlan_interface_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interface** | [**VlanInterfaceObject**](VlanInterfaceObject.md)| VlanInterface object | [optional] 

### Return type

[**VlanInterfaceObject**](VlanInterfaceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vlan_interface_put**
> VlanInterfaceObject vlan_interface_put(device_name, num, port, body=body)

VlanInterfaceRoute.put

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
api_instance = polarisgenclient.VlanInterfaceApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
num = 56 # int | VlanInterface number
port = 56 # int | VlanInterface port
body = polarisgenclient.VlanInterfaceObject() # VlanInterfaceObject | VlanInterface object (optional)

try:
    # VlanInterfaceRoute.put
    api_response = api_instance.vlan_interface_put(device_name, num, port, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VlanInterfaceApi->vlan_interface_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **num** | **int**| VlanInterface number | 
 **port** | **int**| VlanInterface port | 
 **body** | [**VlanInterfaceObject**](VlanInterfaceObject.md)| VlanInterface object | [optional] 

### Return type

[**VlanInterfaceObject**](VlanInterfaceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

