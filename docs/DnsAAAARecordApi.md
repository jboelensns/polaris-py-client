# polarisgenclient.DnsAAAARecordApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_dns_record_aaaa_fqdn_ip_delete**](DnsAAAARecordApi.md#api_v01_dns_record_aaaa_fqdn_ip_delete) | **DELETE** /api/v0.1/dns/record/aaaa/{fqdn}/{ip} | DnsAAAARecordRoute.delete
[**api_v01_dns_record_aaaa_fqdn_ip_get**](DnsAAAARecordApi.md#api_v01_dns_record_aaaa_fqdn_ip_get) | **GET** /api/v0.1/dns/record/aaaa/{fqdn}/{ip} | DnsAAAARecordRoute.get
[**api_v01_dns_record_aaaa_fqdn_ip_put**](DnsAAAARecordApi.md#api_v01_dns_record_aaaa_fqdn_ip_put) | **PUT** /api/v0.1/dns/record/aaaa/{fqdn}/{ip} | DnsAAAARecordRoute.post
[**api_v01_dns_record_aaaa_get**](DnsAAAARecordApi.md#api_v01_dns_record_aaaa_get) | **GET** /api/v0.1/dns/record/aaaa | DnsAAAARecordRoute.get
[**api_v01_dns_record_aaaa_post**](DnsAAAARecordApi.md#api_v01_dns_record_aaaa_post) | **POST** /api/v0.1/dns/record/aaaa | DnsAAAARecordRoute.post


# **api_v01_dns_record_aaaa_fqdn_ip_delete**
> api_v01_dns_record_aaaa_fqdn_ip_delete(fqdn, ip)

DnsAAAARecordRoute.delete

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
api_instance = polarisgenclient.DnsAAAARecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
ip = 'ip_example' # str | ip address

try:
    # DnsAAAARecordRoute.delete
    api_instance.api_v01_dns_record_aaaa_fqdn_ip_delete(fqdn, ip)
except ApiException as e:
    print("Exception when calling DnsAAAARecordApi->api_v01_dns_record_aaaa_fqdn_ip_delete: %s\n" % e)
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

# **api_v01_dns_record_aaaa_fqdn_ip_get**
> api_v01_dns_record_aaaa_fqdn_ip_get(fqdn, ip)

DnsAAAARecordRoute.get

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
api_instance = polarisgenclient.DnsAAAARecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
ip = 'ip_example' # str | ip address

try:
    # DnsAAAARecordRoute.get
    api_instance.api_v01_dns_record_aaaa_fqdn_ip_get(fqdn, ip)
except ApiException as e:
    print("Exception when calling DnsAAAARecordApi->api_v01_dns_record_aaaa_fqdn_ip_get: %s\n" % e)
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

# **api_v01_dns_record_aaaa_fqdn_ip_put**
> api_v01_dns_record_aaaa_fqdn_ip_put(fqdn, ip, body=body)

DnsAAAARecordRoute.post

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
api_instance = polarisgenclient.DnsAAAARecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | ip
ip = 'ip_example' # str | ip
body = polarisgenclient.Body6() # Body6 | Dns object (optional)

try:
    # DnsAAAARecordRoute.post
    api_instance.api_v01_dns_record_aaaa_fqdn_ip_put(fqdn, ip, body=body)
except ApiException as e:
    print("Exception when calling DnsAAAARecordApi->api_v01_dns_record_aaaa_fqdn_ip_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| ip | 
 **ip** | **str**| ip | 
 **body** | [**Body6**](Body6.md)| Dns object | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_dns_record_aaaa_get**
> api_v01_dns_record_aaaa_get(fqdn, ip)

DnsAAAARecordRoute.get

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
api_instance = polarisgenclient.DnsAAAARecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
ip = 'ip_example' # str | ip address

try:
    # DnsAAAARecordRoute.get
    api_instance.api_v01_dns_record_aaaa_get(fqdn, ip)
except ApiException as e:
    print("Exception when calling DnsAAAARecordApi->api_v01_dns_record_aaaa_get: %s\n" % e)
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

# **api_v01_dns_record_aaaa_post**
> api_v01_dns_record_aaaa_post(body=body)

DnsAAAARecordRoute.post

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
api_instance = polarisgenclient.DnsAAAARecordApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.Body5() # Body5 | Dns object. (optional)

try:
    # DnsAAAARecordRoute.post
    api_instance.api_v01_dns_record_aaaa_post(body=body)
except ApiException as e:
    print("Exception when calling DnsAAAARecordApi->api_v01_dns_record_aaaa_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body5**](Body5.md)| Dns object. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

