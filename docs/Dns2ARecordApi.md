# polarisgenclient.Dns2ARecordApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dns2_a_record_get**](Dns2ARecordApi.md#dns2_a_record_get) | **GET** /api/v0.1/dns2/record/{fqdn} | Dns2ARecordRoute.get


# **dns2_a_record_get**
> DnsRecordObject dns2_a_record_get(fqdn, name)

Dns2ARecordRoute.get

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
api_instance = polarisgenclient.Dns2ARecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
name = 'name_example' # str | name

try:
    # Dns2ARecordRoute.get
    api_response = api_instance.dns2_a_record_get(fqdn, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Dns2ARecordApi->dns2_a_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| fqdn | 
 **name** | **str**| name | 

### Return type

[**DnsRecordObject**](DnsRecordObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

