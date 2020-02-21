# polarisgenclient.DnsCNAMERecordApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_dns_record_cname_fqdn_delete**](DnsCNAMERecordApi.md#api_v01_dns_record_cname_fqdn_delete) | **DELETE** /api/v0.1/dns/record/cname/{fqdn} | DnsCNAMERecordRoute.delete
[**api_v01_dns_record_cname_fqdn_get**](DnsCNAMERecordApi.md#api_v01_dns_record_cname_fqdn_get) | **GET** /api/v0.1/dns/record/cname/{fqdn} | DnsCNAMERecordRoute.get
[**api_v01_dns_record_cname_fqdn_put**](DnsCNAMERecordApi.md#api_v01_dns_record_cname_fqdn_put) | **PUT** /api/v0.1/dns/record/cname/{fqdn} | DnsCNAMERecordRoute.post
[**api_v01_dns_record_cname_get**](DnsCNAMERecordApi.md#api_v01_dns_record_cname_get) | **GET** /api/v0.1/dns/record/cname | DnsCNAMERecordRoute.get
[**api_v01_dns_record_cname_post**](DnsCNAMERecordApi.md#api_v01_dns_record_cname_post) | **POST** /api/v0.1/dns/record/cname | DnsCNAMERecordRoute.post


# **api_v01_dns_record_cname_fqdn_delete**
> api_v01_dns_record_cname_fqdn_delete(fqdn)

DnsCNAMERecordRoute.delete

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
api_instance = polarisgenclient.DnsCNAMERecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn

try:
    # DnsCNAMERecordRoute.delete
    api_instance.api_v01_dns_record_cname_fqdn_delete(fqdn)
except ApiException as e:
    print("Exception when calling DnsCNAMERecordApi->api_v01_dns_record_cname_fqdn_delete: %s\n" % e)
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

# **api_v01_dns_record_cname_fqdn_get**
> api_v01_dns_record_cname_fqdn_get(fqdn, canonical)

DnsCNAMERecordRoute.get

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
api_instance = polarisgenclient.DnsCNAMERecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
canonical = 'canonical_example' # str | canonical name

try:
    # DnsCNAMERecordRoute.get
    api_instance.api_v01_dns_record_cname_fqdn_get(fqdn, canonical)
except ApiException as e:
    print("Exception when calling DnsCNAMERecordApi->api_v01_dns_record_cname_fqdn_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| fqdn | 
 **canonical** | **str**| canonical name | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_dns_record_cname_fqdn_put**
> api_v01_dns_record_cname_fqdn_put(fqdn, canonical, body=body)

DnsCNAMERecordRoute.post

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
api_instance = polarisgenclient.DnsCNAMERecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | ip
canonical = 'canonical_example' # str | canonical
body = polarisgenclient.Body8() # Body8 | Dns object (optional)

try:
    # DnsCNAMERecordRoute.post
    api_instance.api_v01_dns_record_cname_fqdn_put(fqdn, canonical, body=body)
except ApiException as e:
    print("Exception when calling DnsCNAMERecordApi->api_v01_dns_record_cname_fqdn_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| ip | 
 **canonical** | **str**| canonical | 
 **body** | [**Body8**](Body8.md)| Dns object | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_dns_record_cname_get**
> api_v01_dns_record_cname_get(fqdn, canonical)

DnsCNAMERecordRoute.get

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
api_instance = polarisgenclient.DnsCNAMERecordApi(polarisgenclient.ApiClient(configuration))
fqdn = 'fqdn_example' # str | fqdn
canonical = 'canonical_example' # str | canonical name

try:
    # DnsCNAMERecordRoute.get
    api_instance.api_v01_dns_record_cname_get(fqdn, canonical)
except ApiException as e:
    print("Exception when calling DnsCNAMERecordApi->api_v01_dns_record_cname_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| fqdn | 
 **canonical** | **str**| canonical name | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_dns_record_cname_post**
> api_v01_dns_record_cname_post(body=body)

DnsCNAMERecordRoute.post

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
api_instance = polarisgenclient.DnsCNAMERecordApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.Body7() # Body7 | Dns CNAME object. (optional)

try:
    # DnsCNAMERecordRoute.post
    api_instance.api_v01_dns_record_cname_post(body=body)
except ApiException as e:
    print("Exception when calling DnsCNAMERecordApi->api_v01_dns_record_cname_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body7**](Body7.md)| Dns CNAME object. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

