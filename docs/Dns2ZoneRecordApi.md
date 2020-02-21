# polarisgenclient.Dns2ZoneRecordApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_dns2_zone_zone_id_records_get**](Dns2ZoneRecordApi.md#api_v01_dns2_zone_zone_id_records_get) | **GET** /api/v0.1/dns2/zone/{zone_id}/records | Dns2ZoneRecordRoute.get


# **api_v01_dns2_zone_zone_id_records_get**
> DnsZoneRecordObject api_v01_dns2_zone_zone_id_records_get(zone_id)

Dns2ZoneRecordRoute.get

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
api_instance = polarisgenclient.Dns2ZoneRecordApi(polarisgenclient.ApiClient(configuration))
zone_id = 'zone_id_example' # str | 

try:
    # Dns2ZoneRecordRoute.get
    api_response = api_instance.api_v01_dns2_zone_zone_id_records_get(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Dns2ZoneRecordApi->api_v01_dns2_zone_zone_id_records_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

[**DnsZoneRecordObject**](DnsZoneRecordObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

