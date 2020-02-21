# polarisgenclient.IpamPrefixApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipam_prefix_delete**](IpamPrefixApi.md#ipam_prefix_delete) | **DELETE** /api/v0.1/ipam/prefix/{id} | IpamPrefixRoute.delete
[**ipam_prefix_get**](IpamPrefixApi.md#ipam_prefix_get) | **GET** /api/v0.1/ipam/prefix | IpamPrefixRoute.get
[**ipam_prefix_get_by_id**](IpamPrefixApi.md#ipam_prefix_get_by_id) | **GET** /api/v0.1/ipam/prefix/{id} | IpamPrefixRoute.get
[**ipam_prefix_post**](IpamPrefixApi.md#ipam_prefix_post) | **POST** /api/v0.1/ipam/prefix | IpamPrefixRoute.post
[**ipam_prefix_put**](IpamPrefixApi.md#ipam_prefix_put) | **PUT** /api/v0.1/ipam/prefix/{id} | IpamPrefixRoute.put


# **ipam_prefix_delete**
> ipam_prefix_delete(id, recursive=recursive)

IpamPrefixRoute.delete

Delete a IPAM Prefix object.

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
api_instance = polarisgenclient.IpamPrefixApi(polarisgenclient.ApiClient(configuration))
id = 56 # int | IPAM Prefix id.
recursive = true # bool | Delete child prefixes as well (optional)

try:
    # IpamPrefixRoute.delete
    api_instance.ipam_prefix_delete(id, recursive=recursive)
except ApiException as e:
    print("Exception when calling IpamPrefixApi->ipam_prefix_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IPAM Prefix id. | 
 **recursive** | **bool**| Delete child prefixes as well | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefix_get**
> list[Prefix] ipam_prefix_get(family=family, is_exact=is_exact, is_indent=is_indent, text=text, tags=tags, max_result=max_result, prefix=prefix)

IpamPrefixRoute.get

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
api_instance = polarisgenclient.IpamPrefixApi(polarisgenclient.ApiClient(configuration))
family = 56 # int | IPAM prefix IP family (optional)
is_exact = true # bool | IPAM prefix is_exact match (optional)
is_indent = true # bool | IPAM prefix is_indent (optional)
text = 'text_example' # str | IPAM prefix text (optional)
tags = 'tags_example' # str | IPAM prefix tags (optional)
max_result = 56 # int | IPAM prefix max result (optional)
prefix = 'prefix_example' # str | IPAM prefix (optional)

try:
    # IpamPrefixRoute.get
    api_response = api_instance.ipam_prefix_get(family=family, is_exact=is_exact, is_indent=is_indent, text=text, tags=tags, max_result=max_result, prefix=prefix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamPrefixApi->ipam_prefix_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family** | **int**| IPAM prefix IP family | [optional] 
 **is_exact** | **bool**| IPAM prefix is_exact match | [optional] 
 **is_indent** | **bool**| IPAM prefix is_indent | [optional] 
 **text** | **str**| IPAM prefix text | [optional] 
 **tags** | **str**| IPAM prefix tags | [optional] 
 **max_result** | **int**| IPAM prefix max result | [optional] 
 **prefix** | **str**| IPAM prefix | [optional] 

### Return type

[**list[Prefix]**](Prefix.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefix_get_by_id**
> Prefix ipam_prefix_get_by_id(id)

IpamPrefixRoute.get

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
api_instance = polarisgenclient.IpamPrefixApi(polarisgenclient.ApiClient(configuration))
id = 56 # int | IPAM prefix id

try:
    # IpamPrefixRoute.get
    api_response = api_instance.ipam_prefix_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamPrefixApi->ipam_prefix_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IPAM prefix id | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefix_post**
> Prefix ipam_prefix_post(body=body)

IpamPrefixRoute.post

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
api_instance = polarisgenclient.IpamPrefixApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.Body16() # Body16 | IPAM Prefix object. (optional)

try:
    # IpamPrefixRoute.post
    api_response = api_instance.ipam_prefix_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamPrefixApi->ipam_prefix_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body16**](Body16.md)| IPAM Prefix object. | [optional] 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefix_put**
> Prefix ipam_prefix_put(id, body=body)

IpamPrefixRoute.put

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
api_instance = polarisgenclient.IpamPrefixApi(polarisgenclient.ApiClient(configuration))
id = 56 # int | IPAM Prefix id.
body = polarisgenclient.Body18() # Body18 | IPAM Prefix object. (optional)

try:
    # IpamPrefixRoute.put
    api_response = api_instance.ipam_prefix_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamPrefixApi->ipam_prefix_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IPAM Prefix id. | 
 **body** | [**Body18**](Body18.md)| IPAM Prefix object. | [optional] 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

