# polarisgenclient.BgpCommunityApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_bgp_community_get**](BgpCommunityApi.md#api_v01_bgp_community_get) | **GET** /api/v0.1/bgp/community | BgpCommunityRoute.get
[**api_v01_bgp_community_name_get**](BgpCommunityApi.md#api_v01_bgp_community_name_get) | **GET** /api/v0.1/bgp/community/{name} | BgpCommunityRoute.get
[**api_v01_bgp_community_name_put**](BgpCommunityApi.md#api_v01_bgp_community_name_put) | **PUT** /api/v0.1/bgp/community/{name} | BgpCommunityRoute.put
[**api_v01_bgp_community_name_value_value_delete**](BgpCommunityApi.md#api_v01_bgp_community_name_value_value_delete) | **DELETE** /api/v0.1/bgp/community/{name}/value/{value} | BgpCommunityRoute.delete
[**api_v01_bgp_community_post**](BgpCommunityApi.md#api_v01_bgp_community_post) | **POST** /api/v0.1/bgp/community | BgpCommunityRoute.post


# **api_v01_bgp_community_get**
> BGPCommunityObject api_v01_bgp_community_get(name)

BgpCommunityRoute.get

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
api_instance = polarisgenclient.BgpCommunityApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Community name

try:
    # BgpCommunityRoute.get
    api_response = api_instance.api_v01_bgp_community_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpCommunityApi->api_v01_bgp_community_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Community name | 

### Return type

[**BGPCommunityObject**](BGPCommunityObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_bgp_community_name_get**
> BGPCommunityObject api_v01_bgp_community_name_get(name)

BgpCommunityRoute.get

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
api_instance = polarisgenclient.BgpCommunityApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Community name

try:
    # BgpCommunityRoute.get
    api_response = api_instance.api_v01_bgp_community_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpCommunityApi->api_v01_bgp_community_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Community name | 

### Return type

[**BGPCommunityObject**](BGPCommunityObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_bgp_community_name_put**
> BGPCommunityObject api_v01_bgp_community_name_put(name, body=body)

BgpCommunityRoute.put

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
api_instance = polarisgenclient.BgpCommunityApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | Community name
body = polarisgenclient.Body() # Body | BGP community object. (optional)

try:
    # BgpCommunityRoute.put
    api_response = api_instance.api_v01_bgp_community_name_put(name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpCommunityApi->api_v01_bgp_community_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Community name | 
 **body** | [**Body**](Body.md)| BGP community object. | [optional] 

### Return type

[**BGPCommunityObject**](BGPCommunityObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_bgp_community_name_value_value_delete**
> BGPCommunityObject api_v01_bgp_community_name_value_value_delete(name, value)

BgpCommunityRoute.delete

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
api_instance = polarisgenclient.BgpCommunityApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | BGP community name
value = 'value_example' # str | BGP community value

try:
    # BgpCommunityRoute.delete
    api_response = api_instance.api_v01_bgp_community_name_value_value_delete(name, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpCommunityApi->api_v01_bgp_community_name_value_value_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| BGP community name | 
 **value** | **str**| BGP community value | 

### Return type

[**BGPCommunityObject**](BGPCommunityObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_bgp_community_post**
> BGPCommunityObject api_v01_bgp_community_post(body=body)

BgpCommunityRoute.post

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
api_instance = polarisgenclient.BgpCommunityApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.BGPCommunityObject() # BGPCommunityObject | BGP community object. (optional)

try:
    # BgpCommunityRoute.post
    api_response = api_instance.api_v01_bgp_community_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BgpCommunityApi->api_v01_bgp_community_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BGPCommunityObject**](BGPCommunityObject.md)| BGP community object. | [optional] 

### Return type

[**BGPCommunityObject**](BGPCommunityObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

