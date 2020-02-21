# polarisgenclient.CaptureGroupApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_capture_group_get**](CaptureGroupApi.md#api_v01_capture_group_get) | **GET** /api/v0.1/capture/group | CaptureGroupRoute.get
[**api_v01_capture_group_post**](CaptureGroupApi.md#api_v01_capture_group_post) | **POST** /api/v0.1/capture/group | CaptureGroupRoute.post
[**api_v01_capture_group_session_id_delete**](CaptureGroupApi.md#api_v01_capture_group_session_id_delete) | **DELETE** /api/v0.1/capture/group/{session_id} | CaptureGroupRoute.delete
[**api_v01_capture_group_session_id_put**](CaptureGroupApi.md#api_v01_capture_group_session_id_put) | **PUT** /api/v0.1/capture/group/{session_id} | CaptureGroupRoute.put


# **api_v01_capture_group_get**
> list[CaptureGroupObject] api_v01_capture_group_get(session_id=session_id)

CaptureGroupRoute.get

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
api_instance = polarisgenclient.CaptureGroupApi(polarisgenclient.ApiClient(configuration))
session_id = 'session_id_example' # str | UUIDv1 session id (optional)

try:
    # CaptureGroupRoute.get
    api_response = api_instance.api_v01_capture_group_get(session_id=session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptureGroupApi->api_v01_capture_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| UUIDv1 session id | [optional] 

### Return type

[**list[CaptureGroupObject]**](CaptureGroupObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_capture_group_post**
> CaptureGroupObject api_v01_capture_group_post(body=body)

CaptureGroupRoute.post

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
api_instance = polarisgenclient.CaptureGroupApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.CaptureGroupObjectPost() # CaptureGroupObjectPost | CaptureGroupObject (optional)

try:
    # CaptureGroupRoute.post
    api_response = api_instance.api_v01_capture_group_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptureGroupApi->api_v01_capture_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CaptureGroupObjectPost**](CaptureGroupObjectPost.md)| CaptureGroupObject | [optional] 

### Return type

[**CaptureGroupObject**](CaptureGroupObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_capture_group_session_id_delete**
> CaptureGroupObject api_v01_capture_group_session_id_delete(session_id)

CaptureGroupRoute.delete

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
api_instance = polarisgenclient.CaptureGroupApi(polarisgenclient.ApiClient(configuration))
session_id = 'session_id_example' # str | UUID1 string

try:
    # CaptureGroupRoute.delete
    api_response = api_instance.api_v01_capture_group_session_id_delete(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptureGroupApi->api_v01_capture_group_session_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| UUID1 string | 

### Return type

[**CaptureGroupObject**](CaptureGroupObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_capture_group_session_id_put**
> CaptureGroupObject api_v01_capture_group_session_id_put(session_id, body=body)

CaptureGroupRoute.put

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
api_instance = polarisgenclient.CaptureGroupApi(polarisgenclient.ApiClient(configuration))
session_id = 'session_id_example' # str | UUID1 string
body = polarisgenclient.CaptureGroupObjectPut() # CaptureGroupObjectPut | CaptureGroupObjectPut (optional)

try:
    # CaptureGroupRoute.put
    api_response = api_instance.api_v01_capture_group_session_id_put(session_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptureGroupApi->api_v01_capture_group_session_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| UUID1 string | 
 **body** | [**CaptureGroupObjectPut**](CaptureGroupObjectPut.md)| CaptureGroupObjectPut | [optional] 

### Return type

[**CaptureGroupObject**](CaptureGroupObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

