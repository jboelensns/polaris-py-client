# polarisgenclient.AgentInventoryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_inventory_get**](AgentInventoryApi.md#agent_inventory_get) | **GET** /api/v0.1/agent/inventory | AgentInventoryRoute.get
[**agent_inventory_get_by_device**](AgentInventoryApi.md#agent_inventory_get_by_device) | **GET** /api/v0.1/device/{device_name}/agent/inventory | AgentInventoryRoute.get
[**agent_inventory_post**](AgentInventoryApi.md#agent_inventory_post) | **POST** /api/v0.1/agent/inventory | AgentInventoryRoute.post


# **agent_inventory_get**
> list[AgentInventoryObject] agent_inventory_get()

AgentInventoryRoute.get

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
api_instance = polarisgenclient.AgentInventoryApi(polarisgenclient.ApiClient(configuration))

try:
    # AgentInventoryRoute.get
    api_response = api_instance.agent_inventory_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryApi->agent_inventory_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AgentInventoryObject]**](AgentInventoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_inventory_get_by_device**
> list[AgentInventoryObject] agent_inventory_get_by_device(device_name)

AgentInventoryRoute.get

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
api_instance = polarisgenclient.AgentInventoryApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name

try:
    # AgentInventoryRoute.get
    api_response = api_instance.agent_inventory_get_by_device(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryApi->agent_inventory_get_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 

### Return type

[**list[AgentInventoryObject]**](AgentInventoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_inventory_post**
> AgentInventoryObject agent_inventory_post(body=body)

AgentInventoryRoute.post

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
api_instance = polarisgenclient.AgentInventoryApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.AgentInventoryObject() # AgentInventoryObject | Agent inventory object (optional)

try:
    # AgentInventoryRoute.post
    api_response = api_instance.agent_inventory_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryApi->agent_inventory_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentInventoryObject**](AgentInventoryObject.md)| Agent inventory object | [optional] 

### Return type

[**AgentInventoryObject**](AgentInventoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

