# polarisgenclient.IpamProfileApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipam_pool_get**](IpamProfileApi.md#ipam_pool_get) | **GET** /api/v0.1/ipam/profile/{name} | IpamPoolRoute.get
[**ipam_profile_deploy_post**](IpamProfileApi.md#ipam_profile_deploy_post) | **POST** /api/v0.1/ipam/profile/{name}/deploy | IpamProfileDeployRoute.post
[**ipam_profile_revert_post**](IpamProfileApi.md#ipam_profile_revert_post) | **POST** /api/v0.1/ipam/profile/{name}/revert | IpamProfileRevertRoute.post


# **ipam_pool_get**
> ipam_pool_get(name)

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
api_instance = polarisgenclient.IpamProfileApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | IPAM profile name

try:
    # IpamPoolRoute.get
    api_instance.ipam_pool_get(name)
except ApiException as e:
    print("Exception when calling IpamProfileApi->ipam_pool_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| IPAM profile name | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_profile_deploy_post**
> ipam_profile_deploy_post(name, body=body)

IpamProfileDeployRoute.post

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
api_instance = polarisgenclient.IpamProfileApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | name
body = polarisgenclient.Body19() # Body19 | IPAM Profile object. (optional)

try:
    # IpamProfileDeployRoute.post
    api_instance.ipam_profile_deploy_post(name, body=body)
except ApiException as e:
    print("Exception when calling IpamProfileApi->ipam_profile_deploy_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 
 **body** | [**Body19**](Body19.md)| IPAM Profile object. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_profile_revert_post**
> ipam_profile_revert_post(name, body=body)

IpamProfileRevertRoute.post

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
api_instance = polarisgenclient.IpamProfileApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | name
body = polarisgenclient.Body20() # Body20 | IPAM Profile object. (optional)

try:
    # IpamProfileRevertRoute.post
    api_instance.ipam_profile_revert_post(name, body=body)
except ApiException as e:
    print("Exception when calling IpamProfileApi->ipam_profile_revert_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name | 
 **body** | [**Body20**](Body20.md)| IPAM Profile object. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

