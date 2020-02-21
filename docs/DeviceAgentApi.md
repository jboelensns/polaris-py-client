# polarisgenclient.DeviceAgentApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_agent_post**](DeviceAgentApi.md#device_agent_post) | **POST** /api/v0.1/device/{device_name}/agent | DeviceAgentRoute.post


# **device_agent_post**
> DeviceAgentObject device_agent_post(device_name, body=body)

DeviceAgentRoute.post

Register device agent

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
api_instance = polarisgenclient.DeviceAgentApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
body = polarisgenclient.DeviceAgentObject() # DeviceAgentObject | Device object (optional)

try:
    # DeviceAgentRoute.post
    api_response = api_instance.device_agent_post(device_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceAgentApi->device_agent_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **body** | [**DeviceAgentObject**](DeviceAgentObject.md)| Device object | [optional] 

### Return type

[**DeviceAgentObject**](DeviceAgentObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

