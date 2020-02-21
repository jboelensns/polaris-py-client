# polarisgenclient.DeviceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_get**](DeviceApi.md#device_get) | **GET** /api/v0.1/device | DeviceRoute.get
[**device_get_by_name**](DeviceApi.md#device_get_by_name) | **GET** /api/v0.1/device/{device_name} | DeviceRoute.get
[**device_post**](DeviceApi.md#device_post) | **POST** /api/v0.1/device/{device_name}/discover | DeviceRoute.post


# **device_get**
> DeviceObject device_get(pop_name=pop_name, include_agent=include_agent, only_agent=only_agent)

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
pop_name = 'pop_name_example' # str | Device POP (optional)
include_agent = true # bool | Include agent (optional) (default to true)
only_agent = false # bool | Only provide agent based devices (optional) (default to false)

try:
    # DeviceRoute.get
    api_response = api_instance.device_get(pop_name=pop_name, include_agent=include_agent, only_agent=only_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **device_get_by_name**
> DeviceObject device_get_by_name(device_name, pop_name=pop_name, include_agent=include_agent, only_agent=only_agent)

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
    api_response = api_instance.device_get_by_name(device_name, pop_name=pop_name, include_agent=include_agent, only_agent=only_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->device_get_by_name: %s\n" % e)
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

# **device_post**
> device_post(device_name)

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
    api_instance.device_post(device_name)
except ApiException as e:
    print("Exception when calling DeviceApi->device_post: %s\n" % e)
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

