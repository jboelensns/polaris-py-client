# polarisgenclient.IpamPoolApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipam_pool_delete**](IpamPoolApi.md#ipam_pool_delete) | **DELETE** /api/v0.1/ipam/pool/{id} | IpamPoolRoute.delete
[**ipam_pool_get**](IpamPoolApi.md#ipam_pool_get) | **GET** /api/v0.1/ipam/pool | IpamPoolRoute.get
[**ipam_pool_post**](IpamPoolApi.md#ipam_pool_post) | **POST** /api/v0.1/ipam/pool | IpamPoolRoute.post
[**ipam_pool_put**](IpamPoolApi.md#ipam_pool_put) | **PUT** /api/v0.1/ipam/pool/{id} | IpamPoolRoute.put


# **ipam_pool_delete**
> IPAMPoolResponse ipam_pool_delete(id)

IpamPoolRoute.delete

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
api_instance = polarisgenclient.IpamPoolApi(polarisgenclient.ApiClient(configuration))
id = 56 # int | IPAM pool id

try:
    # IpamPoolRoute.delete
    api_response = api_instance.ipam_pool_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamPoolApi->ipam_pool_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IPAM pool id | 

### Return type

[**IPAMPoolResponse**](IPAMPoolResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_pool_get**
> IPAMPoolResponse ipam_pool_get(id, name=name, text=text, tags=tags, max_result=max_result)

IpamPoolRoute.get

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
api_instance = polarisgenclient.IpamPoolApi(polarisgenclient.ApiClient(configuration))
id = 56 # int | IPAM pool id
name = 'name_example' # str | IPAM pool name (optional)
text = 'text_example' # str | IPAM pool text (optional)
tags = 'tags_example' # str | IPAM pool tags (optional)
max_result = 56 # int | IPAM pool max result (optional)

try:
    # IpamPoolRoute.get
    api_response = api_instance.ipam_pool_get(id, name=name, text=text, tags=tags, max_result=max_result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamPoolApi->ipam_pool_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IPAM pool id | 
 **name** | **str**| IPAM pool name | [optional] 
 **text** | **str**| IPAM pool text | [optional] 
 **tags** | **str**| IPAM pool tags | [optional] 
 **max_result** | **int**| IPAM pool max result | [optional] 

### Return type

[**IPAMPoolResponse**](IPAMPoolResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_pool_post**
> IPAMPoolResponse ipam_pool_post(body=body)

IpamPoolRoute.post

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
api_instance = polarisgenclient.IpamPoolApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.IPAMPool() # IPAMPool | IPAM Pool object. (optional)

try:
    # IpamPoolRoute.post
    api_response = api_instance.ipam_pool_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamPoolApi->ipam_pool_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IPAMPool**](IPAMPool.md)| IPAM Pool object. | [optional] 

### Return type

[**IPAMPoolResponse**](IPAMPoolResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_pool_put**
> IPAMPoolResponse ipam_pool_put(id, body=body)

IpamPoolRoute.put

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
api_instance = polarisgenclient.IpamPoolApi(polarisgenclient.ApiClient(configuration))
id = 56 # int | IPAM pool id
body = polarisgenclient.IPAMPool() # IPAMPool | IPAM Pool object. (optional)

try:
    # IpamPoolRoute.put
    api_response = api_instance.ipam_pool_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamPoolApi->ipam_pool_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IPAM pool id | 
 **body** | [**IPAMPool**](IPAMPool.md)| IPAM Pool object. | [optional] 

### Return type

[**IPAMPoolResponse**](IPAMPoolResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

