# polarisgenclient.CaptureSessionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_capture_session_device_name_get**](CaptureSessionApi.md#api_v01_capture_session_device_name_get) | **GET** /api/v0.1/capture/session/{device_name} | CaptureSessionRoute.get
[**api_v01_capture_session_device_name_group_session_id_id_id_delete**](CaptureSessionApi.md#api_v01_capture_session_device_name_group_session_id_id_id_delete) | **DELETE** /api/v0.1/capture/session/{device_name}/group/{session_id}/id/{id} | CaptureSessionRoute.delete
[**api_v01_capture_session_device_name_group_session_id_id_id_put**](CaptureSessionApi.md#api_v01_capture_session_device_name_group_session_id_id_id_put) | **PUT** /api/v0.1/capture/session/{device_name}/group/{session_id}/id/{id} | CaptureSessionRoute.put
[**api_v01_capture_session_get**](CaptureSessionApi.md#api_v01_capture_session_get) | **GET** /api/v0.1/capture/session | CaptureSessionRoute.get
[**api_v01_capture_session_post**](CaptureSessionApi.md#api_v01_capture_session_post) | **POST** /api/v0.1/capture/session | CaptureSessionRoute.post


# **api_v01_capture_session_device_name_get**
> list[CaptureSessionObject] api_v01_capture_session_device_name_get(device_name, session_id=session_id, id=id)

CaptureSessionRoute.get

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
api_instance = polarisgenclient.CaptureSessionApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
session_id = 'session_id_example' # str | UUIDv1 session id (optional)
id = 'id_example' # str | UUIDv1 id (optional)

try:
    # CaptureSessionRoute.get
    api_response = api_instance.api_v01_capture_session_device_name_get(device_name, session_id=session_id, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptureSessionApi->api_v01_capture_session_device_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **session_id** | **str**| UUIDv1 session id | [optional] 
 **id** | **str**| UUIDv1 id | [optional] 

### Return type

[**list[CaptureSessionObject]**](CaptureSessionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_capture_session_device_name_group_session_id_id_id_delete**
> CaptureSessionObject api_v01_capture_session_device_name_group_session_id_id_id_delete(device_name, session_id, id)

CaptureSessionRoute.delete

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
api_instance = polarisgenclient.CaptureSessionApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
session_id = 'session_id_example' # str | UUID1 string
id = 'id_example' # str | UUID1 string

try:
    # CaptureSessionRoute.delete
    api_response = api_instance.api_v01_capture_session_device_name_group_session_id_id_id_delete(device_name, session_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptureSessionApi->api_v01_capture_session_device_name_group_session_id_id_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **session_id** | **str**| UUID1 string | 
 **id** | **str**| UUID1 string | 

### Return type

[**CaptureSessionObject**](CaptureSessionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_capture_session_device_name_group_session_id_id_id_put**
> CaptureSessionObject api_v01_capture_session_device_name_group_session_id_id_id_put(device_name, session_id, id, body=body)

CaptureSessionRoute.put

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
api_instance = polarisgenclient.CaptureSessionApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
session_id = 'session_id_example' # str | UUID1 string
id = 'id_example' # str | UUID1 string
body = polarisgenclient.CaptureSessionObjectPut() # CaptureSessionObjectPut | CaptureSessionObjectPut (optional)

try:
    # CaptureSessionRoute.put
    api_response = api_instance.api_v01_capture_session_device_name_group_session_id_id_id_put(device_name, session_id, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptureSessionApi->api_v01_capture_session_device_name_group_session_id_id_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **session_id** | **str**| UUID1 string | 
 **id** | **str**| UUID1 string | 
 **body** | [**CaptureSessionObjectPut**](CaptureSessionObjectPut.md)| CaptureSessionObjectPut | [optional] 

### Return type

[**CaptureSessionObject**](CaptureSessionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_capture_session_get**
> list[CaptureSessionObject] api_v01_capture_session_get(device_name, session_id=session_id, id=id)

CaptureSessionRoute.get

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
api_instance = polarisgenclient.CaptureSessionApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device name
session_id = 'session_id_example' # str | UUIDv1 session id (optional)
id = 'id_example' # str | UUIDv1 id (optional)

try:
    # CaptureSessionRoute.get
    api_response = api_instance.api_v01_capture_session_get(device_name, session_id=session_id, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptureSessionApi->api_v01_capture_session_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device name | 
 **session_id** | **str**| UUIDv1 session id | [optional] 
 **id** | **str**| UUIDv1 id | [optional] 

### Return type

[**list[CaptureSessionObject]**](CaptureSessionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_capture_session_post**
> CaptureSessionObject api_v01_capture_session_post(body=body)

CaptureSessionRoute.post

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
api_instance = polarisgenclient.CaptureSessionApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.CaptureSessionObject() # CaptureSessionObject | CaptureSessionObject (optional)

try:
    # CaptureSessionRoute.post
    api_response = api_instance.api_v01_capture_session_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaptureSessionApi->api_v01_capture_session_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CaptureSessionObject**](CaptureSessionObject.md)| CaptureSessionObject | [optional] 

### Return type

[**CaptureSessionObject**](CaptureSessionObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

