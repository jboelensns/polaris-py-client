# polarisgenclient.DnsHOSTRecordApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_dns_record_host_fqdn_delete**](DnsHOSTRecordApi.md#api_v01_dns_record_host_fqdn_delete) | **DELETE** /api/v0.1/dns/record/host/{fqdn} | DnsHOSTRecordRoute.delete
[**api_v01_dns_record_host_fqdn_get**](DnsHOSTRecordApi.md#api_v01_dns_record_host_fqdn_get) | **GET** /api/v0.1/dns/record/host/{fqdn} | DnsHOSTRecordRoute.get
[**api_v01_dns_record_host_fqdn_put**](DnsHOSTRecordApi.md#api_v01_dns_record_host_fqdn_put) | **PUT** /api/v0.1/dns/record/host/{fqdn} | DnsHOSTRecordRoute.post
[**api_v01_dns_record_host_get**](DnsHOSTRecordApi.md#api_v01_dns_record_host_get) | **GET** /api/v0.1/dns/record/host | DnsHOSTRecordRoute.get
[**api_v01_dns_record_host_post**](DnsHOSTRecordApi.md#api_v01_dns_record_host_post) | **POST** /api/v0.1/dns/record/host | DnsHOSTRecordRoute.post
[**api_v01_dns_zone_reverse_get**](DnsHOSTRecordApi.md#api_v01_dns_zone_reverse_get) | **GET** /api/v0.1/dns/zone/reverse | DnsHOSTRecordRoute.get


# **api_v01_dns_record_host_fqdn_delete**
> api_v01_dns_record_host_fqdn_delete(fqdn)

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
    api_instance.api_v01_dns_record_host_fqdn_delete(fqdn)
except ApiException as e:
    print("Exception when calling DnsHOSTRecordApi->api_v01_dns_record_host_fqdn_delete: %s\n" % e)
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

# **api_v01_dns_record_host_fqdn_get**
> api_v01_dns_record_host_fqdn_get(fqdn, ipv4addr=ipv4addr, ipv6addr=ipv6addr)

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
    api_instance.api_v01_dns_record_host_fqdn_get(fqdn, ipv4addr=ipv4addr, ipv6addr=ipv6addr)
except ApiException as e:
    print("Exception when calling DnsHOSTRecordApi->api_v01_dns_record_host_fqdn_get: %s\n" % e)
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

# **api_v01_dns_record_host_fqdn_put**
> api_v01_dns_record_host_fqdn_put(fqdn, body=body)

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
fqdn = 'fqdn_example' # str | fqdn
body = polarisgenclient.Body10() # Body10 | Dns object (optional)

try:
    # DnsHOSTRecordRoute.post
    api_instance.api_v01_dns_record_host_fqdn_put(fqdn, body=body)
except ApiException as e:
    print("Exception when calling DnsHOSTRecordApi->api_v01_dns_record_host_fqdn_put: %s\n" % e)
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

# **api_v01_dns_record_host_get**
> api_v01_dns_record_host_get(fqdn, ipv4addr=ipv4addr, ipv6addr=ipv6addr)

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
    api_instance.api_v01_dns_record_host_get(fqdn, ipv4addr=ipv4addr, ipv6addr=ipv6addr)
except ApiException as e:
    print("Exception when calling DnsHOSTRecordApi->api_v01_dns_record_host_get: %s\n" % e)
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

# **api_v01_dns_record_host_post**
> api_v01_dns_record_host_post(body=body)

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
    api_instance.api_v01_dns_record_host_post(body=body)
except ApiException as e:
    print("Exception when calling DnsHOSTRecordApi->api_v01_dns_record_host_post: %s\n" % e)
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

# **api_v01_dns_zone_reverse_get**
> list[DnsZoneResponse] api_v01_dns_zone_reverse_get(cidr=cidr, view=view)

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
cidr = 'cidr_example' # str | cidr (optional)
view = 'view_example' # str | dns view (optional)

try:
    # DnsHOSTRecordRoute.get
    api_response = api_instance.api_v01_dns_zone_reverse_get(cidr=cidr, view=view)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DnsHOSTRecordApi->api_v01_dns_zone_reverse_get: %s\n" % e)
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

