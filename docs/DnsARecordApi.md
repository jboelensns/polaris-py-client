# polarisgenclient.DnsARecordApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_dns_record_a_fqdn_ip_delete**](DnsARecordApi.md#api_v01_dns_record_a_fqdn_ip_delete) | **DELETE** /api/v0.1/dns/record/a/{fqdn}/{ip} | DnsARecordRoute.delete
[**api_v01_dns_record_a_fqdn_ip_get**](DnsARecordApi.md#api_v01_dns_record_a_fqdn_ip_get) | **GET** /api/v0.1/dns/record/a/{fqdn}/{ip} | DnsARecordRoute.get
[**api_v01_dns_record_a_fqdn_ip_put**](DnsARecordApi.md#api_v01_dns_record_a_fqdn_ip_put) | **PUT** /api/v0.1/dns/record/a/{fqdn}/{ip} | DnsARecordRoute.post
[**api_v01_dns_record_a_get**](DnsARecordApi.md#api_v01_dns_record_a_get) | **GET** /api/v0.1/dns/record/a | DnsARecordRoute.get
[**api_v01_dns_record_a_post**](DnsARecordApi.md#api_v01_dns_record_a_post) | **POST** /api/v0.1/dns/record/a | DnsARecordRoute.post


# **api_v01_dns_record_a_fqdn_ip_delete**
> api_v01_dns_record_a_fqdn_ip_delete(fqdn, ip)

DnsARecordRoute.delete

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
api_instance = polarisgenclient.DnsARecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
ip = 'ip_example' # str | ip address

try:
    # DnsARecordRoute.delete
    api_instance.api_v01_dns_record_a_fqdn_ip_delete(fqdn, ip)
except ApiException as e:
    print("Exception when calling DnsARecordApi->api_v01_dns_record_a_fqdn_ip_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| fqdn | 
 **ip** | **str**| ip address | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_dns_record_a_fqdn_ip_get**
> api_v01_dns_record_a_fqdn_ip_get(fqdn, ip)

DnsARecordRoute.get

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
api_instance = polarisgenclient.DnsARecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
ip = 'ip_example' # str | ip address

try:
    # DnsARecordRoute.get
    api_instance.api_v01_dns_record_a_fqdn_ip_get(fqdn, ip)
except ApiException as e:
    print("Exception when calling DnsARecordApi->api_v01_dns_record_a_fqdn_ip_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| fqdn | 
 **ip** | **str**| ip address | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_dns_record_a_fqdn_ip_put**
> api_v01_dns_record_a_fqdn_ip_put(fqdn, ip, body=body)

DnsARecordRoute.post

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
api_instance = polarisgenclient.DnsARecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | ip
ip = 'ip_example' # str | ip
body = polarisgenclient.Body4() # Body4 | Dns object (optional)

try:
    # DnsARecordRoute.post
    api_instance.api_v01_dns_record_a_fqdn_ip_put(fqdn, ip, body=body)
except ApiException as e:
    print("Exception when calling DnsARecordApi->api_v01_dns_record_a_fqdn_ip_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| ip | 
 **ip** | **str**| ip | 
 **body** | [**Body4**](Body4.md)| Dns object | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_dns_record_a_get**
> api_v01_dns_record_a_get(fqdn, ip)

DnsARecordRoute.get

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
api_instance = polarisgenclient.DnsARecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
ip = 'ip_example' # str | ip address

try:
    # DnsARecordRoute.get
    api_instance.api_v01_dns_record_a_get(fqdn, ip)
except ApiException as e:
    print("Exception when calling DnsARecordApi->api_v01_dns_record_a_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| fqdn | 
 **ip** | **str**| ip address | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_dns_record_a_post**
> api_v01_dns_record_a_post(body=body)

DnsARecordRoute.post

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
api_instance = polarisgenclient.DnsARecordApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.Body3() # Body3 | Dns object. (optional)

try:
    # DnsARecordRoute.post
    api_instance.api_v01_dns_record_a_post(body=body)
except ApiException as e:
    print("Exception when calling DnsARecordApi->api_v01_dns_record_a_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)| Dns object. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

