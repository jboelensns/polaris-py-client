# polarisgenclient.AgentInventoryHistoryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_agent_inventory_history_get**](AgentInventoryHistoryApi.md#api_v01_agent_inventory_history_get) | **GET** /api/v0.1/agent/inventory/history | AgentInventoryHistoryRoute.get
[**api_v01_agent_inventory_history_id_id_delete**](AgentInventoryHistoryApi.md#api_v01_agent_inventory_history_id_id_delete) | **DELETE** /api/v0.1/agent/inventory/history/id/{id} | AgentInventoryHistoryRoute.delete
[**api_v01_agent_inventory_history_id_id_put**](AgentInventoryHistoryApi.md#api_v01_agent_inventory_history_id_id_put) | **PUT** /api/v0.1/agent/inventory/history/id/{id} | AgentInventoryHistoryRoute.put
[**api_v01_agent_inventory_history_post**](AgentInventoryHistoryApi.md#api_v01_agent_inventory_history_post) | **POST** /api/v0.1/agent/inventory/history | AgentInventoryHistoryRoute.post
[**api_v01_device_device_name_agent_inventory_history_get**](AgentInventoryHistoryApi.md#api_v01_device_device_name_agent_inventory_history_get) | **GET** /api/v0.1/device/{device_name}/agent/inventory/history | AgentInventoryHistoryRoute.get


# **api_v01_agent_inventory_history_get**
> list[AgentInventoryHistoryObject] api_v01_agent_inventory_history_get(device_name, gt_id=gt_id, lt_id=lt_id, limit=limit)

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
    api_response = api_instance.api_v01_agent_inventory_history_get(device_name, gt_id=gt_id, lt_id=lt_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryHistoryApi->api_v01_agent_inventory_history_get: %s\n" % e)
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

# **api_v01_agent_inventory_history_id_id_delete**
> AgentInventoryHistoryObject api_v01_agent_inventory_history_id_id_delete(id, body=body)

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
    api_response = api_instance.api_v01_agent_inventory_history_id_id_delete(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryHistoryApi->api_v01_agent_inventory_history_id_id_delete: %s\n" % e)
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

# **api_v01_agent_inventory_history_id_id_put**
> AgentInventoryHistoryObject api_v01_agent_inventory_history_id_id_put(id, body=body)

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
    api_response = api_instance.api_v01_agent_inventory_history_id_id_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryHistoryApi->api_v01_agent_inventory_history_id_id_put: %s\n" % e)
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

# **api_v01_agent_inventory_history_post**
> AgentInventoryHistoryObject api_v01_agent_inventory_history_post(body=body)

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
    api_response = api_instance.api_v01_agent_inventory_history_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryHistoryApi->api_v01_agent_inventory_history_post: %s\n" % e)
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

# **api_v01_device_device_name_agent_inventory_history_get**
> list[AgentInventoryHistoryObject] api_v01_device_device_name_agent_inventory_history_get(device_name, gt_id=gt_id, lt_id=lt_id, limit=limit)

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
    api_response = api_instance.api_v01_device_device_name_agent_inventory_history_get(device_name, gt_id=gt_id, lt_id=lt_id, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentInventoryHistoryApi->api_v01_device_device_name_agent_inventory_history_get: %s\n" % e)
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

