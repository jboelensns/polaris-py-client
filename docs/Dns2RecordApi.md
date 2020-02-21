# polarisgenclient.Dns2RecordApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dns2_record_post**](Dns2RecordApi.md#dns2_record_post) | **POST** /api/v0.1/dns2/record/{zone}/{name} | Dns2RecordRoute.post


# **dns2_record_post**
> DnsRecordObject dns2_record_post(zone, name)

Dns2RecordRoute.post

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
api_instance = polarisgenclient.Dns2RecordApi(polarisgenclient.ApiClient(configuration))
zone = 'zone_example' # str | 
name = 'name_example' # str | 

try:
    # Dns2RecordRoute.post
    api_response = api_instance.dns2_record_post(zone, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Dns2RecordApi->dns2_record_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**DnsRecordObject**](DnsRecordObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

