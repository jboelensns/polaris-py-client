# polarisgenclient.DnsCNAMERecordApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dns_cname_record_delete**](DnsCNAMERecordApi.md#dns_cname_record_delete) | **DELETE** /api/v0.1/dns/record/cname/{fqdn} | DnsCNAMERecordRoute.delete
[**dns_cname_record_get**](DnsCNAMERecordApi.md#dns_cname_record_get) | **GET** /api/v0.1/dns/record/cname | DnsCNAMERecordRoute.get
[**dns_cname_record_get_by_fqdn**](DnsCNAMERecordApi.md#dns_cname_record_get_by_fqdn) | **GET** /api/v0.1/dns/record/cname/{fqdn} | DnsCNAMERecordRoute.get
[**dns_cname_record_post**](DnsCNAMERecordApi.md#dns_cname_record_post) | **POST** /api/v0.1/dns/record/cname | DnsCNAMERecordRoute.post
[**dns_cname_record_put**](DnsCNAMERecordApi.md#dns_cname_record_put) | **PUT** /api/v0.1/dns/record/cname/{fqdn} | DnsCNAMERecordRoute.put


# **dns_cname_record_delete**
> dns_cname_record_delete(fqdn)

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
    api_instance.dns_cname_record_delete(fqdn)
except ApiException as e:
    print("Exception when calling DnsCNAMERecordApi->dns_cname_record_delete: %s\n" % e)
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

# **dns_cname_record_get**
> dns_cname_record_get(canonical=canonical)

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
canonical = 'canonical_example' # str | canonical name (optional)

try:
    # DnsCNAMERecordRoute.get
    api_instance.dns_cname_record_get(canonical=canonical)
except ApiException as e:
    print("Exception when calling DnsCNAMERecordApi->dns_cname_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **canonical** | **str**| canonical name | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_cname_record_get_by_fqdn**
> dns_cname_record_get_by_fqdn(fqdn, canonical=canonical)

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
canonical = 'canonical_example' # str | canonical name (optional)

try:
    # DnsCNAMERecordRoute.get
    api_instance.dns_cname_record_get_by_fqdn(fqdn, canonical=canonical)
except ApiException as e:
    print("Exception when calling DnsCNAMERecordApi->dns_cname_record_get_by_fqdn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| fqdn | 
 **canonical** | **str**| canonical name | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns_cname_record_post**
> dns_cname_record_post(body=body)

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
    api_instance.dns_cname_record_post(body=body)
except ApiException as e:
    print("Exception when calling DnsCNAMERecordApi->dns_cname_record_post: %s\n" % e)
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

# **dns_cname_record_put**
> dns_cname_record_put(fqdn, canonical, body=body)

DnsCNAMERecordRoute.put

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
    # DnsCNAMERecordRoute.put
    api_instance.dns_cname_record_put(fqdn, canonical, body=body)
except ApiException as e:
    print("Exception when calling DnsCNAMERecordApi->dns_cname_record_put: %s\n" % e)
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

