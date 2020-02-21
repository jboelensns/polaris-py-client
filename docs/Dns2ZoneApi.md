# polarisgenclient.Dns2ZoneApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_dns2_zone_get**](Dns2ZoneApi.md#api_v01_dns2_zone_get) | **GET** /api/v0.1/dns2/zone | Dns2ZoneRoute.get
[**api_v01_dns2_zone_zone_id_get**](Dns2ZoneApi.md#api_v01_dns2_zone_zone_id_get) | **GET** /api/v0.1/dns2/zone/{zone_id} | Dns2ZoneRoute.get


# **api_v01_dns2_zone_get**
> DnsZoneObject api_v01_dns2_zone_get(zone_id)

Dns2ZoneRoute.get

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
api_instance = polarisgenclient.Dns2ZoneApi(polarisgenclient.ApiClient(configuration))
zone_id = 'zone_id_example' # str | 

try:
    # Dns2ZoneRoute.get
    api_response = api_instance.api_v01_dns2_zone_get(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Dns2ZoneApi->api_v01_dns2_zone_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

[**DnsZoneObject**](DnsZoneObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_dns2_zone_zone_id_get**
> DnsZoneObject api_v01_dns2_zone_zone_id_get(zone_id)

Dns2ZoneRoute.get

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
api_instance = polarisgenclient.Dns2ZoneApi(polarisgenclient.ApiClient(configuration))
zone_id = 'zone_id_example' # str | 

try:
    # Dns2ZoneRoute.get
    api_response = api_instance.api_v01_dns2_zone_zone_id_get(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Dns2ZoneApi->api_v01_dns2_zone_zone_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**|  | 

### Return type

[**DnsZoneObject**](DnsZoneObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

