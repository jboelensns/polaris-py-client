# polarisgenclient.DeviceServiceDiscoverApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_device_name_service_discover_get**](DeviceServiceDiscoverApi.md#api_v01_device_name_service_discover_get) | **GET** /api/v0.1/device/{name}/service/discover | DeviceServiceDiscoverRoute.get
[**api_v01_device_name_service_service_name_discover_get**](DeviceServiceDiscoverApi.md#api_v01_device_name_service_service_name_discover_get) | **GET** /api/v0.1/device/{name}/service/{service_name}/discover | DeviceServiceDiscoverRoute.get
[**api_v01_device_service_discover_bulk_post**](DeviceServiceDiscoverApi.md#api_v01_device_service_discover_bulk_post) | **POST** /api/v0.1/device/service/discover/bulk | DeviceServiceDiscoverRoute.post
[**api_v01_device_service_discover_get**](DeviceServiceDiscoverApi.md#api_v01_device_service_discover_get) | **GET** /api/v0.1/device/service/discover | DeviceServiceDiscoverRoute.get
[**api_v01_device_service_discover_post**](DeviceServiceDiscoverApi.md#api_v01_device_service_discover_post) | **POST** /api/v0.1/device/service/discover | DeviceServiceDiscoverRoute.post


# **api_v01_device_name_service_discover_get**
> list[DeviceServiceDiscoverObject] api_v01_device_name_service_discover_get(name, service_name, ip_address=ip_address, port=port, protocol=protocol)

DeviceServiceDiscoverRoute.get

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
api_instance = polarisgenclient.DeviceServiceDiscoverApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Device name
service_name = 'service_name_example' # str | Service name
ip_address = 'ip_address_example' # str | IP Address (optional)
port = 56 # int | Port (optional)
protocol = 'protocol_example' # str | Protocol (optional)

try:
    # DeviceServiceDiscoverRoute.get
    api_response = api_instance.api_v01_device_name_service_discover_get(name, service_name, ip_address=ip_address, port=port, protocol=protocol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceDiscoverApi->api_v01_device_name_service_discover_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Device name | 
 **service_name** | **str**| Service name | 
 **ip_address** | **str**| IP Address | [optional] 
 **port** | **int**| Port | [optional] 
 **protocol** | **str**| Protocol | [optional] 

### Return type

[**list[DeviceServiceDiscoverObject]**](DeviceServiceDiscoverObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_name_service_service_name_discover_get**
> list[DeviceServiceDiscoverObject] api_v01_device_name_service_service_name_discover_get(name, service_name, ip_address=ip_address, port=port, protocol=protocol)

DeviceServiceDiscoverRoute.get

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
api_instance = polarisgenclient.DeviceServiceDiscoverApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Device name
service_name = 'service_name_example' # str | Service name
ip_address = 'ip_address_example' # str | IP Address (optional)
port = 56 # int | Port (optional)
protocol = 'protocol_example' # str | Protocol (optional)

try:
    # DeviceServiceDiscoverRoute.get
    api_response = api_instance.api_v01_device_name_service_service_name_discover_get(name, service_name, ip_address=ip_address, port=port, protocol=protocol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceDiscoverApi->api_v01_device_name_service_service_name_discover_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Device name | 
 **service_name** | **str**| Service name | 
 **ip_address** | **str**| IP Address | [optional] 
 **port** | **int**| Port | [optional] 
 **protocol** | **str**| Protocol | [optional] 

### Return type

[**list[DeviceServiceDiscoverObject]**](DeviceServiceDiscoverObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_service_discover_bulk_post**
> list[DeviceServiceDiscoverObject] api_v01_device_service_discover_bulk_post(body=body)

DeviceServiceDiscoverRoute.post

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
api_instance = polarisgenclient.DeviceServiceDiscoverApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.Body2() # Body2 | Device Service Discover object (optional)

try:
    # DeviceServiceDiscoverRoute.post
    api_response = api_instance.api_v01_device_service_discover_bulk_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceDiscoverApi->api_v01_device_service_discover_bulk_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)| Device Service Discover object | [optional] 

### Return type

[**list[DeviceServiceDiscoverObject]**](DeviceServiceDiscoverObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_service_discover_get**
> list[DeviceServiceDiscoverObject] api_v01_device_service_discover_get(name, service_name, ip_address=ip_address, port=port, protocol=protocol)

DeviceServiceDiscoverRoute.get

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
api_instance = polarisgenclient.DeviceServiceDiscoverApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Device name
service_name = 'service_name_example' # str | Service name
ip_address = 'ip_address_example' # str | IP Address (optional)
port = 56 # int | Port (optional)
protocol = 'protocol_example' # str | Protocol (optional)

try:
    # DeviceServiceDiscoverRoute.get
    api_response = api_instance.api_v01_device_service_discover_get(name, service_name, ip_address=ip_address, port=port, protocol=protocol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceDiscoverApi->api_v01_device_service_discover_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Device name | 
 **service_name** | **str**| Service name | 
 **ip_address** | **str**| IP Address | [optional] 
 **port** | **int**| Port | [optional] 
 **protocol** | **str**| Protocol | [optional] 

### Return type

[**list[DeviceServiceDiscoverObject]**](DeviceServiceDiscoverObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_service_discover_post**
> DeviceServiceDiscoverObject api_v01_device_service_discover_post(body=body)

DeviceServiceDiscoverRoute.post

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
api_instance = polarisgenclient.DeviceServiceDiscoverApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.DeviceServiceDiscoverObject() # DeviceServiceDiscoverObject | Device Service Discover object (optional)

try:
    # DeviceServiceDiscoverRoute.post
    api_response = api_instance.api_v01_device_service_discover_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceDiscoverApi->api_v01_device_service_discover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceServiceDiscoverObject**](DeviceServiceDiscoverObject.md)| Device Service Discover object | [optional] 

### Return type

[**DeviceServiceDiscoverObject**](DeviceServiceDiscoverObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

