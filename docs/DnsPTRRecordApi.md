# polarisgenclient.DnsPTRRecordApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_dns_record_ptr_fqdn_ip_delete**](DnsPTRRecordApi.md#api_v01_dns_record_ptr_fqdn_ip_delete) | **DELETE** /api/v0.1/dns/record/ptr/{fqdn}/{ip} | DnsPTRRecordRoute.delete
[**api_v01_dns_record_ptr_fqdn_ip_get**](DnsPTRRecordApi.md#api_v01_dns_record_ptr_fqdn_ip_get) | **GET** /api/v0.1/dns/record/ptr/{fqdn}/{ip} | DnsPTRRecordRoute.get
[**api_v01_dns_record_ptr_fqdn_ip_put**](DnsPTRRecordApi.md#api_v01_dns_record_ptr_fqdn_ip_put) | **PUT** /api/v0.1/dns/record/ptr/{fqdn}/{ip} | DnsPTRRecordRoute.put
[**api_v01_dns_record_ptr_get**](DnsPTRRecordApi.md#api_v01_dns_record_ptr_get) | **GET** /api/v0.1/dns/record/ptr | DnsPTRRecordRoute.get
[**api_v01_dns_record_ptr_post**](DnsPTRRecordApi.md#api_v01_dns_record_ptr_post) | **POST** /api/v0.1/dns/record/ptr | DnsPTRRecordRoute.post


# **api_v01_dns_record_ptr_fqdn_ip_delete**
> api_v01_dns_record_ptr_fqdn_ip_delete(fqdn, ip)

DnsPTRRecordRoute.delete

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
api_instance = polarisgenclient.DnsPTRRecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
ip = 'ip_example' # str | ip address

try:
    # DnsPTRRecordRoute.delete
    api_instance.api_v01_dns_record_ptr_fqdn_ip_delete(fqdn, ip)
except ApiException as e:
    print("Exception when calling DnsPTRRecordApi->api_v01_dns_record_ptr_fqdn_ip_delete: %s\n" % e)
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

# **api_v01_dns_record_ptr_fqdn_ip_get**
> api_v01_dns_record_ptr_fqdn_ip_get(fqdn, ip)

DnsPTRRecordRoute.get

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
api_instance = polarisgenclient.DnsPTRRecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
ip = 'ip_example' # str | ip address

try:
    # DnsPTRRecordRoute.get
    api_instance.api_v01_dns_record_ptr_fqdn_ip_get(fqdn, ip)
except ApiException as e:
    print("Exception when calling DnsPTRRecordApi->api_v01_dns_record_ptr_fqdn_ip_get: %s\n" % e)
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

# **api_v01_dns_record_ptr_fqdn_ip_put**
> api_v01_dns_record_ptr_fqdn_ip_put(fqdn, ip, body=body)

DnsPTRRecordRoute.put

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
api_instance = polarisgenclient.DnsPTRRecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | ip
ip = 'ip_example' # str | ip
body = polarisgenclient.Body12() # Body12 | Dns object (optional)

try:
    # DnsPTRRecordRoute.put
    api_instance.api_v01_dns_record_ptr_fqdn_ip_put(fqdn, ip, body=body)
except ApiException as e:
    print("Exception when calling DnsPTRRecordApi->api_v01_dns_record_ptr_fqdn_ip_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| ip | 
 **ip** | **str**| ip | 
 **body** | [**Body12**](Body12.md)| Dns object | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_dns_record_ptr_get**
> api_v01_dns_record_ptr_get(fqdn, ip)

DnsPTRRecordRoute.get

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
api_instance = polarisgenclient.DnsPTRRecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
ip = 'ip_example' # str | ip address

try:
    # DnsPTRRecordRoute.get
    api_instance.api_v01_dns_record_ptr_get(fqdn, ip)
except ApiException as e:
    print("Exception when calling DnsPTRRecordApi->api_v01_dns_record_ptr_get: %s\n" % e)
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

# **api_v01_dns_record_ptr_post**
> api_v01_dns_record_ptr_post(body=body)

DnsPTRRecordRoute.post

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
api_instance = polarisgenclient.DnsPTRRecordApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.Body11() # Body11 | Dns object. (optional)

try:
    # DnsPTRRecordRoute.post
    api_instance.api_v01_dns_record_ptr_post(body=body)
except ApiException as e:
    print("Exception when calling DnsPTRRecordApi->api_v01_dns_record_ptr_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body11**](Body11.md)| Dns object. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

