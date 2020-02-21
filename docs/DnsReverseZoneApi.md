# polarisgenclient.DnsReverseZoneApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_dns_zone_reverse_cidr_delete**](DnsReverseZoneApi.md#api_v01_dns_zone_reverse_cidr_delete) | **DELETE** /api/v0.1/dns/zone/reverse/{cidr} | DnsReverseZoneRoute.delete
[**api_v01_dns_zone_reverse_delete**](DnsReverseZoneApi.md#api_v01_dns_zone_reverse_delete) | **DELETE** /api/v0.1/dns/zone/reverse | DnsReverseZoneRoute.delete
[**api_v01_dns_zone_reverse_post**](DnsReverseZoneApi.md#api_v01_dns_zone_reverse_post) | **POST** /api/v0.1/dns/zone/reverse | DnsReverseZoneRoute.post


# **api_v01_dns_zone_reverse_cidr_delete**
> list[DnsZoneResponse] api_v01_dns_zone_reverse_cidr_delete(cidr)

DnsReverseZoneRoute.delete

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
api_instance = polarisgenclient.DnsReverseZoneApi(polarisgenclient.ApiClient(configuration))
cidr = 'cidr_example' # str | fqdn

try:
    # DnsReverseZoneRoute.delete
    api_response = api_instance.api_v01_dns_zone_reverse_cidr_delete(cidr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsReverseZoneApi->api_v01_dns_zone_reverse_cidr_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cidr** | **str**| fqdn | 

### Return type

[**list[DnsZoneResponse]**](DnsZoneResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_dns_zone_reverse_delete**
> list[DnsZoneResponse] api_v01_dns_zone_reverse_delete(cidr)

DnsReverseZoneRoute.delete

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
api_instance = polarisgenclient.DnsReverseZoneApi(polarisgenclient.ApiClient(configuration))
cidr = 'cidr_example' # str | fqdn

try:
    # DnsReverseZoneRoute.delete
    api_response = api_instance.api_v01_dns_zone_reverse_delete(cidr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsReverseZoneApi->api_v01_dns_zone_reverse_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cidr** | **str**| fqdn | 

### Return type

[**list[DnsZoneResponse]**](DnsZoneResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_dns_zone_reverse_post**
> list[DnsZoneResponse] api_v01_dns_zone_reverse_post(body=body)

DnsReverseZoneRoute.post

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
api_instance = polarisgenclient.DnsReverseZoneApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.Body13() # Body13 | Dns HOST object. (optional)

try:
    # DnsReverseZoneRoute.post
    api_response = api_instance.api_v01_dns_zone_reverse_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsReverseZoneApi->api_v01_dns_zone_reverse_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body13**](Body13.md)| Dns HOST object. | [optional] 

### Return type

[**list[DnsZoneResponse]**](DnsZoneResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

