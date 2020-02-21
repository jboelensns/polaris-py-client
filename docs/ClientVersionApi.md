# polarisgenclient.ClientVersionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_client_version_client_name_delete**](ClientVersionApi.md#api_v01_client_version_client_name_delete) | **DELETE** /api/v0.1/client/version/{client_name} | ClientVersionRoute.delete
[**api_v01_client_version_client_name_get**](ClientVersionApi.md#api_v01_client_version_client_name_get) | **GET** /api/v0.1/client/version/{client_name} | ClientVersionRoute.get
[**api_v01_client_version_client_name_put**](ClientVersionApi.md#api_v01_client_version_client_name_put) | **PUT** /api/v0.1/client/version/{client_name} | ClientVersionRoute.put
[**api_v01_client_version_get**](ClientVersionApi.md#api_v01_client_version_get) | **GET** /api/v0.1/client/version/ | ClientVersionRoute.get
[**api_v01_client_version_post**](ClientVersionApi.md#api_v01_client_version_post) | **POST** /api/v0.1/client/version/ | ClientVersionRoute.post


# **api_v01_client_version_client_name_delete**
> ClientVersionObject api_v01_client_version_client_name_delete(client_name)

ClientVersionRoute.delete

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
api_instance = polarisgenclient.ClientVersionApi(polarisgenclient.ApiClient(configuration))
client_name = 'client_name_example' # str | Client version name

try:
    # ClientVersionRoute.delete
    api_response = api_instance.api_v01_client_version_client_name_delete(client_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientVersionApi->api_v01_client_version_client_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_name** | **str**| Client version name | 

### Return type

[**ClientVersionObject**](ClientVersionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_client_version_client_name_get**
> ClientVersionObject api_v01_client_version_client_name_get(client_name)

ClientVersionRoute.get

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
api_instance = polarisgenclient.ClientVersionApi(polarisgenclient.ApiClient(configuration))
client_name = 'client_name_example' # str | client name

try:
    # ClientVersionRoute.get
    api_response = api_instance.api_v01_client_version_client_name_get(client_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientVersionApi->api_v01_client_version_client_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_name** | **str**| client name | 

### Return type

[**ClientVersionObject**](ClientVersionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_client_version_client_name_put**
> ClientVersionObject api_v01_client_version_client_name_put(client_name, body=body)

ClientVersionRoute.put

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
api_instance = polarisgenclient.ClientVersionApi(polarisgenclient.ApiClient(configuration))
client_name = 'client_name_example' # str | client name
body = polarisgenclient.Body1() # Body1 | Client version object. (optional)

try:
    # ClientVersionRoute.put
    api_response = api_instance.api_v01_client_version_client_name_put(client_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientVersionApi->api_v01_client_version_client_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_name** | **str**| client name | 
 **body** | [**Body1**](Body1.md)| Client version object. | [optional] 

### Return type

[**ClientVersionObject**](ClientVersionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_client_version_get**
> ClientVersionObject api_v01_client_version_get(client_name)

ClientVersionRoute.get

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
api_instance = polarisgenclient.ClientVersionApi(polarisgenclient.ApiClient(configuration))
client_name = 'client_name_example' # str | client name

try:
    # ClientVersionRoute.get
    api_response = api_instance.api_v01_client_version_get(client_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientVersionApi->api_v01_client_version_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_name** | **str**| client name | 

### Return type

[**ClientVersionObject**](ClientVersionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_client_version_post**
> ClientVersionObject api_v01_client_version_post(body=body)

ClientVersionRoute.post

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
api_instance = polarisgenclient.ClientVersionApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.ClientVersionObject() # ClientVersionObject | ClientVersion object (optional)

try:
    # ClientVersionRoute.post
    api_response = api_instance.api_v01_client_version_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientVersionApi->api_v01_client_version_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientVersionObject**](ClientVersionObject.md)| ClientVersion object | [optional] 

### Return type

[**ClientVersionObject**](ClientVersionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

