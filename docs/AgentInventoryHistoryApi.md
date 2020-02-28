# polarisgenclient.AgentInventoryHistoryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_inventory_history_delete**](AgentInventoryHistoryApi.md#agent_inventory_history_delete) | **DELETE** /api/v0.1/agent/inventory/history/id/{id} | AgentInventoryHistoryRoute.delete
[**agent_inventory_history_get**](AgentInventoryHistoryApi.md#agent_inventory_history_get) | **GET** /api/v0.1/agent/inventory/history | AgentInventoryHistoryRoute.get
[**agent_inventory_history_get_by_device**](AgentInventoryHistoryApi.md#agent_inventory_history_get_by_device) | **GET** /api/v0.1/device/{device_name}/agent/inventory/history | AgentInventoryHistoryRoute.get
[**agent_inventory_history_post**](AgentInventoryHistoryApi.md#agent_inventory_history_post) | **POST** /api/v0.1/agent/inventory/history | AgentInventoryHistoryRoute.post
[**agent_inventory_history_put**](AgentInventoryHistoryApi.md#agent_inventory_history_put) | **PUT** /api/v0.1/agent/inventory/history/id/{id} | AgentInventoryHistoryRoute.put


# **agent_inventory_history_delete**
> AgentInventoryHistoryObject agent_inventory_history_delete(id, body=body)

AgentInventoryHistoryRoute.delete

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
api_instance = polarisgenclient.AgentInventoryHistoryApi(polarisgenclient.ApiClient(configuration))
id = 'id_example' # str | UUID1 string
body = polarisgenclient.AgentInventoryHistoryObject() # AgentInventoryHistoryObject | Agent inventory object. (optional)

try:
    # AgentInventoryHistoryRoute.delete
    api_response = api_instance.agent_inventory_history_delete(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryHistoryApi->agent_inventory_history_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID1 string | 
 **body** | [**AgentInventoryHistoryObject**](AgentInventoryHistoryObject.md)| Agent inventory object. | [optional] 

### Return type

[**AgentInventoryHistoryObject**](AgentInventoryHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_inventory_history_get**
> list[AgentInventoryHistoryObject] agent_inventory_history_get(gt_id=gt_id, lt_id=lt_id, limit=limit)

AgentInventoryHistoryRoute.get

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
api_instance = polarisgenclient.AgentInventoryHistoryApi(polarisgenclient.ApiClient(configuration))
gt_id = 'gt_id_example' # str | Paginate greater than id (optional)
lt_id = 'lt_id_example' # str | Paginate greater than id (optional)
limit = 56 # int | Limit results to N records (optional)

try:
    # AgentInventoryHistoryRoute.get
    api_response = api_instance.agent_inventory_history_get(gt_id=gt_id, lt_id=lt_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryHistoryApi->agent_inventory_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gt_id** | **str**| Paginate greater than id | [optional] 
 **lt_id** | **str**| Paginate greater than id | [optional] 
 **limit** | **int**| Limit results to N records | [optional] 

### Return type

[**list[AgentInventoryHistoryObject]**](AgentInventoryHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_inventory_history_get_by_device**
> list[AgentInventoryHistoryObject] agent_inventory_history_get_by_device(device_name, gt_id=gt_id, lt_id=lt_id, limit=limit)

AgentInventoryHistoryRoute.get

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
api_instance = polarisgenclient.AgentInventoryHistoryApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
gt_id = 'gt_id_example' # str | Paginate greater than id (optional)
lt_id = 'lt_id_example' # str | Paginate greater than id (optional)
limit = 56 # int | Limit results to N records (optional)

try:
    # AgentInventoryHistoryRoute.get
    api_response = api_instance.agent_inventory_history_get_by_device(device_name, gt_id=gt_id, lt_id=lt_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryHistoryApi->agent_inventory_history_get_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **gt_id** | **str**| Paginate greater than id | [optional] 
 **lt_id** | **str**| Paginate greater than id | [optional] 
 **limit** | **int**| Limit results to N records | [optional] 

### Return type

[**list[AgentInventoryHistoryObject]**](AgentInventoryHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_inventory_history_post**
> AgentInventoryHistoryObject agent_inventory_history_post(body=body)

AgentInventoryHistoryRoute.post

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
api_instance = polarisgenclient.AgentInventoryHistoryApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.AgentInventoryHistoryObject() # AgentInventoryHistoryObject | Agent inventory object (optional)

try:
    # AgentInventoryHistoryRoute.post
    api_response = api_instance.agent_inventory_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryHistoryApi->agent_inventory_history_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentInventoryHistoryObject**](AgentInventoryHistoryObject.md)| Agent inventory object | [optional] 

### Return type

[**AgentInventoryHistoryObject**](AgentInventoryHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_inventory_history_put**
> AgentInventoryHistoryObject agent_inventory_history_put(id, body=body)

AgentInventoryHistoryRoute.put

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
api_instance = polarisgenclient.AgentInventoryHistoryApi(polarisgenclient.ApiClient(configuration))
id = 'id_example' # str | UUID1 string
body = polarisgenclient.AgentInventoryHistoryObject() # AgentInventoryHistoryObject | Agent inventory object. (optional)

try:
    # AgentInventoryHistoryRoute.put
    api_response = api_instance.agent_inventory_history_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryHistoryApi->agent_inventory_history_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID1 string | 
 **body** | [**AgentInventoryHistoryObject**](AgentInventoryHistoryObject.md)| Agent inventory object. | [optional] 

### Return type

[**AgentInventoryHistoryObject**](AgentInventoryHistoryObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

