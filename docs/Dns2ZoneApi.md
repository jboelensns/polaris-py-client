# polarisgenclient.Dns2ZoneApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dns2_zone_route_get**](Dns2ZoneApi.md#dns2_zone_route_get) | **GET** /api/v0.1/dns2/zone | Dns2ZoneRoute.get
[**dns2_zone_route_get_by_id**](Dns2ZoneApi.md#dns2_zone_route_get_by_id) | **GET** /api/v0.1/dns2/zone/{zone_id} | Dns2ZoneRoute.get


# **dns2_zone_route_get**
> DnsZoneObject dns2_zone_route_get()

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

try:
    # Dns2ZoneRoute.get
    api_response = api_instance.dns2_zone_route_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Dns2ZoneApi->dns2_zone_route_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DnsZoneObject**](DnsZoneObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns2_zone_route_get_by_id**
> DnsZoneObject dns2_zone_route_get_by_id(zone_id)

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
    api_response = api_instance.dns2_zone_route_get_by_id(zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Dns2ZoneApi->dns2_zone_route_get_by_id: %s\n" % e)
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

