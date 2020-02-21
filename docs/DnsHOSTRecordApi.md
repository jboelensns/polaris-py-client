# polarisgenclient.DnsHOSTRecordApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dns_host_record_delete**](DnsHOSTRecordApi.md#dns_host_record_delete) | **DELETE** /api/v0.1/dns/record/host/{fqdn} | DnsHOSTRecordRoute.delete
[**dns_host_record_get**](DnsHOSTRecordApi.md#dns_host_record_get) | **GET** /api/v0.1/dns/record/host | DnsHOSTRecordRoute.get
[**dns_host_record_get_by_fqdn**](DnsHOSTRecordApi.md#dns_host_record_get_by_fqdn) | **GET** /api/v0.1/dns/record/host/{fqdn} | DnsHOSTRecordRoute.get
[**dns_host_record_post**](DnsHOSTRecordApi.md#dns_host_record_post) | **POST** /api/v0.1/dns/record/host | DnsHOSTRecordRoute.post
[**dns_host_record_put**](DnsHOSTRecordApi.md#dns_host_record_put) | **PUT** /api/v0.1/dns/record/host/{fqdn} | DnsHOSTRecordRoute.put
[**dns_reverse_record_get**](DnsHOSTRecordApi.md#dns_reverse_record_get) | **GET** /api/v0.1/dns/zone/reverse | DnsReverseRecordRoute.get


# **dns_host_record_delete**
> dns_host_record_delete(fqdn)

DnsHOSTRecordRoute.delete

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
api_instance = polarisgenclient.DnsHOSTRecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn

try:
    # DnsHOSTRecordRoute.delete
    api_instance.dns_host_record_delete(fqdn)
except ApiException as e:
    print("Exception when calling DnsHOSTRecordApi->dns_host_record_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| fqdn | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_host_record_get**
> dns_host_record_get(ipv4addr=ipv4addr, ipv6addr=ipv6addr)

DnsHOSTRecordRoute.get

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
api_instance = polarisgenclient.DnsHOSTRecordApi(polarisgenclient.ApiClient(configuration))
ipv4addr = 'ipv4addr_example' # str | ipv4 address (optional)
ipv6addr = 'ipv6addr_example' # str | ipv6 address (optional)

try:
    # DnsHOSTRecordRoute.get
    api_instance.dns_host_record_get(ipv4addr=ipv4addr, ipv6addr=ipv6addr)
except ApiException as e:
    print("Exception when calling DnsHOSTRecordApi->dns_host_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipv4addr** | **str**| ipv4 address | [optional] 
 **ipv6addr** | **str**| ipv6 address | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_host_record_get_by_fqdn**
> dns_host_record_get_by_fqdn(fqdn, ipv4addr=ipv4addr, ipv6addr=ipv6addr)

DnsHOSTRecordRoute.get

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
api_instance = polarisgenclient.DnsHOSTRecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
ipv4addr = 'ipv4addr_example' # str | ipv4 address (optional)
ipv6addr = 'ipv6addr_example' # str | ipv6 address (optional)

try:
    # DnsHOSTRecordRoute.get
    api_instance.dns_host_record_get_by_fqdn(fqdn, ipv4addr=ipv4addr, ipv6addr=ipv6addr)
except ApiException as e:
    print("Exception when calling DnsHOSTRecordApi->dns_host_record_get_by_fqdn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| fqdn | 
 **ipv4addr** | **str**| ipv4 address | [optional] 
 **ipv6addr** | **str**| ipv6 address | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_host_record_post**
> dns_host_record_post(body=body)

DnsHOSTRecordRoute.post

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
api_instance = polarisgenclient.DnsHOSTRecordApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.Body9() # Body9 | Dns HOST object. (optional)

try:
    # DnsHOSTRecordRoute.post
    api_instance.dns_host_record_post(body=body)
except ApiException as e:
    print("Exception when calling DnsHOSTRecordApi->dns_host_record_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body9**](Body9.md)| Dns HOST object. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_host_record_put**
> dns_host_record_put(fqdn, body=body)

DnsHOSTRecordRoute.put

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
api_instance = polarisgenclient.DnsHOSTRecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
body = polarisgenclient.Body10() # Body10 | Dns object (optional)

try:
    # DnsHOSTRecordRoute.put
    api_instance.dns_host_record_put(fqdn, body=body)
except ApiException as e:
    print("Exception when calling DnsHOSTRecordApi->dns_host_record_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| fqdn | 
 **body** | [**Body10**](Body10.md)| Dns object | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_reverse_record_get**
> list[DnsZoneResponse] dns_reverse_record_get(cidr=cidr, view=view)

DnsReverseRecordRoute.get

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
api_instance = polarisgenclient.DnsHOSTRecordApi(polarisgenclient.ApiClient(configuration))
cidr = 'cidr_example' # str | cidr (optional)
view = 'view_example' # str | dns view (optional)

try:
    # DnsReverseRecordRoute.get
    api_response = api_instance.dns_reverse_record_get(cidr=cidr, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsHOSTRecordApi->dns_reverse_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cidr** | **str**| cidr | [optional] 
 **view** | **str**| dns view | [optional] 

### Return type

[**list[DnsZoneResponse]**](DnsZoneResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

