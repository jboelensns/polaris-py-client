# polarisgenclient.VlanApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vlan_delete**](VlanApi.md#vlan_delete) | **DELETE** /api/v0.1/device/{device_name}/vlan/{num} | VlanRoute.delete
[**vlan_get**](VlanApi.md#vlan_get) | **GET** /api/v0.1/vlan | VlanRoute.get
[**vlan_get_by_num**](VlanApi.md#vlan_get_by_num) | **GET** /api/v0.1/device/{device_name}/vlan/{num} | VlanRoute.get
[**vlan_post**](VlanApi.md#vlan_post) | **POST** /api/v0.1/vlan | VlanRoute.post
[**vlan_route_put**](VlanApi.md#vlan_route_put) | **PUT** /api/v0.1/device/{device_name}/vlan/{num} | VlanRoute.put


# **vlan_delete**
> VlanObject vlan_delete(device_name, num)

VlanRoute.delete

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
api_instance = polarisgenclient.VlanApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
num = 56 # int | Vlan number

try:
    # VlanRoute.delete
    api_response = api_instance.vlan_delete(device_name, num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VlanApi->vlan_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **num** | **int**| Vlan number | 

### Return type

[**VlanObject**](VlanObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vlan_get**
> VlanObject vlan_get(device_name)

VlanRoute.get

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
api_instance = polarisgenclient.VlanApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name

try:
    # VlanRoute.get
    api_response = api_instance.vlan_get(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VlanApi->vlan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 

### Return type

[**VlanObject**](VlanObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vlan_get_by_num**
> VlanObject vlan_get_by_num(device_name, num)

VlanRoute.get

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
api_instance = polarisgenclient.VlanApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
num = 56 # int | Vlan number

try:
    # VlanRoute.get
    api_response = api_instance.vlan_get_by_num(device_name, num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VlanApi->vlan_get_by_num: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **num** | **int**| Vlan number | 

### Return type

[**VlanObject**](VlanObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vlan_post**
> VlanObject vlan_post(vlan=vlan)

VlanRoute.post

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
api_instance = polarisgenclient.VlanApi(polarisgenclient.ApiClient(configuration))
vlan = polarisgenclient.VlanObject() # VlanObject | Vlan object (optional)

try:
    # VlanRoute.post
    api_response = api_instance.vlan_post(vlan=vlan)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VlanApi->vlan_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vlan** | [**VlanObject**](VlanObject.md)| Vlan object | [optional] 

### Return type

[**VlanObject**](VlanObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vlan_route_put**
> VlanObject vlan_route_put(device_name, num, body=body)

VlanRoute.put

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
api_instance = polarisgenclient.VlanApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
num = 56 # int | Vlan number
body = polarisgenclient.VlanObject() # VlanObject | Vlan object (optional)

try:
    # VlanRoute.put
    api_response = api_instance.vlan_route_put(device_name, num, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VlanApi->vlan_route_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **num** | **int**| Vlan number | 
 **body** | [**VlanObject**](VlanObject.md)| Vlan object | [optional] 

### Return type

[**VlanObject**](VlanObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

