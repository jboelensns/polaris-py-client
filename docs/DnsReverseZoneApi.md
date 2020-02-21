# polarisgenclient.DnsReverseZoneApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dns_reverse_zone_delete**](DnsReverseZoneApi.md#dns_reverse_zone_delete) | **DELETE** /api/v0.1/dns/zone/reverse | DnsReverseZoneRoute.delete
[**dns_reverse_zone_delete_by_cidr**](DnsReverseZoneApi.md#dns_reverse_zone_delete_by_cidr) | **DELETE** /api/v0.1/dns/zone/reverse/{cidr} | DnsReverseZoneRoute.delete
[**dns_reverse_zone_post**](DnsReverseZoneApi.md#dns_reverse_zone_post) | **POST** /api/v0.1/dns/zone/reverse | DnsReverseZoneRoute.post


# **dns_reverse_zone_delete**
> list[DnsZoneResponse] dns_reverse_zone_delete()

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

try:
    # DnsReverseZoneRoute.delete
    api_response = api_instance.dns_reverse_zone_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsReverseZoneApi->dns_reverse_zone_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DnsZoneResponse]**](DnsZoneResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_reverse_zone_delete_by_cidr**
> list[DnsZoneResponse] dns_reverse_zone_delete_by_cidr(cidr)

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
    api_response = api_instance.dns_reverse_zone_delete_by_cidr(cidr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsReverseZoneApi->dns_reverse_zone_delete_by_cidr: %s\n" % e)
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

# **dns_reverse_zone_post**
> list[DnsZoneResponse] dns_reverse_zone_post(body=body)

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
    api_response = api_instance.dns_reverse_zone_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsReverseZoneApi->dns_reverse_zone_post: %s\n" % e)
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

