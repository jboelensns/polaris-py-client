# polarisgenclient.SystemProvisionVmApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_system_provision_vm_post**](SystemProvisionVmApi.md#api_v01_system_provision_vm_post) | **POST** /api/v0.1/system/provision/vm | SystemProvisionRoute.post


# **api_v01_system_provision_vm_post**
> SystemProvisionObject api_v01_system_provision_vm_post(system_provision_params=system_provision_params)

SystemProvisionRoute.post

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
api_instance = polarisgenclient.SystemProvisionVmApi(polarisgenclient.ApiClient(configuration))
system_provision_params = polarisgenclient.SystemProvisionObject() # SystemProvisionObject | SystemProvision object (optional)

try:
    # SystemProvisionRoute.post
    api_response = api_instance.api_v01_system_provision_vm_post(system_provision_params=system_provision_params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemProvisionVmApi->api_v01_system_provision_vm_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_provision_params** | [**SystemProvisionObject**](SystemProvisionObject.md)| SystemProvision object | [optional] 

### Return type

[**SystemProvisionObject**](SystemProvisionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

