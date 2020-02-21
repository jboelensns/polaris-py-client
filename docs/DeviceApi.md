# polarisgenclient.DeviceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_device_device_name_discover_post**](DeviceApi.md#api_v01_device_device_name_discover_post) | **POST** /api/v0.1/device/{device_name}/discover | DeviceRoute.post
[**api_v01_device_device_name_get**](DeviceApi.md#api_v01_device_device_name_get) | **GET** /api/v0.1/device/{device_name} | DeviceRoute.get
[**api_v01_device_get**](DeviceApi.md#api_v01_device_get) | **GET** /api/v0.1/device | DeviceRoute.get


# **api_v01_device_device_name_discover_post**
> api_v01_device_device_name_discover_post(device_name)

DeviceRoute.post

Dispatch real time Device scan

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
api_instance = polarisgenclient.DeviceApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN

try:
    # DeviceRoute.post
    api_instance.api_v01_device_device_name_discover_post(device_name)
except ApiException as e:
    print("Exception when calling DeviceApi->api_v01_device_device_name_discover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_device_name_get**
> DeviceObject api_v01_device_device_name_get(device_name, pop_name=pop_name, include_agent=include_agent, only_agent=only_agent)

DeviceRoute.get

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
api_instance = polarisgenclient.DeviceApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
pop_name = 'pop_name_example' # str | Device POP (optional)
include_agent = true # bool | Include agent (optional) (default to true)
only_agent = false # bool | Only provide agent based devices (optional) (default to false)

try:
    # DeviceRoute.get
    api_response = api_instance.api_v01_device_device_name_get(device_name, pop_name=pop_name, include_agent=include_agent, only_agent=only_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->api_v01_device_device_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **pop_name** | **str**| Device POP | [optional] 
 **include_agent** | **bool**| Include agent | [optional] [default to true]
 **only_agent** | **bool**| Only provide agent based devices | [optional] [default to false]

### Return type

[**DeviceObject**](DeviceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_get**
> DeviceObject api_v01_device_get(device_name, pop_name=pop_name, include_agent=include_agent, only_agent=only_agent)

DeviceRoute.get

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
api_instance = polarisgenclient.DeviceApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
pop_name = 'pop_name_example' # str | Device POP (optional)
include_agent = true # bool | Include agent (optional) (default to true)
only_agent = false # bool | Only provide agent based devices (optional) (default to false)

try:
    # DeviceRoute.get
    api_response = api_instance.api_v01_device_get(device_name, pop_name=pop_name, include_agent=include_agent, only_agent=only_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->api_v01_device_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **pop_name** | **str**| Device POP | [optional] 
 **include_agent** | **bool**| Include agent | [optional] [default to true]
 **only_agent** | **bool**| Only provide agent based devices | [optional] [default to false]

### Return type

[**DeviceObject**](DeviceObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

