# polarisgenclient.DhcpHelperProcessApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dhcp_helper_process_delete**](DhcpHelperProcessApi.md#dhcp_helper_process_delete) | **DELETE** /api/v0.1/device/{device_name}/dhcp/helper | DhcpHelperProcessRoute.delete
[**dhcp_helper_process_get**](DhcpHelperProcessApi.md#dhcp_helper_process_get) | **GET** /api/v0.1/dhcp/helper | DhcpHelperProcessRoute.get
[**dhcp_helper_process_get_by_device**](DhcpHelperProcessApi.md#dhcp_helper_process_get_by_device) | **GET** /api/v0.1/device/{device_name}/dhcp/helper | DhcpHelperProcessRoute.get
[**dhcp_helper_process_post**](DhcpHelperProcessApi.md#dhcp_helper_process_post) | **POST** /api/v0.1/dhcp/helper | DhcpHelperProcessRoute.post
[**dhcp_helper_process_put**](DhcpHelperProcessApi.md#dhcp_helper_process_put) | **PUT** /api/v0.1/device/{device_name}/dhcp/helper | DhcpHelperProcessRoute.put


# **dhcp_helper_process_delete**
> DhcpHelperProcessObject dhcp_helper_process_delete(device_name, port, dst_ipv4_address)

DhcpHelperProcessRoute.delete

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
api_instance = polarisgenclient.DhcpHelperProcessApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | DhcpHelperProcess device_name
port = 'port_example' # str | DhcpHelperProcess port
dst_ipv4_address = 'dst_ipv4_address_example' # str | DhcpHelperProcess dst_ipv4_address

try:
    # DhcpHelperProcessRoute.delete
    api_response = api_instance.dhcp_helper_process_delete(device_name, port, dst_ipv4_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DhcpHelperProcessApi->dhcp_helper_process_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| DhcpHelperProcess device_name | 
 **port** | **str**| DhcpHelperProcess port | 
 **dst_ipv4_address** | **str**| DhcpHelperProcess dst_ipv4_address | 

### Return type

[**DhcpHelperProcessObject**](DhcpHelperProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dhcp_helper_process_get**
> DhcpHelperProcessObject dhcp_helper_process_get()

DhcpHelperProcessRoute.get

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
api_instance = polarisgenclient.DhcpHelperProcessApi(polarisgenclient.ApiClient(configuration))

try:
    # DhcpHelperProcessRoute.get
    api_response = api_instance.dhcp_helper_process_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DhcpHelperProcessApi->dhcp_helper_process_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DhcpHelperProcessObject**](DhcpHelperProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dhcp_helper_process_get_by_device**
> DhcpHelperProcessObject dhcp_helper_process_get_by_device(device_name)

DhcpHelperProcessRoute.get

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
api_instance = polarisgenclient.DhcpHelperProcessApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | DhcpHelperProcess device_name

try:
    # DhcpHelperProcessRoute.get
    api_response = api_instance.dhcp_helper_process_get_by_device(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DhcpHelperProcessApi->dhcp_helper_process_get_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| DhcpHelperProcess device_name | 

### Return type

[**DhcpHelperProcessObject**](DhcpHelperProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dhcp_helper_process_post**
> DhcpHelperProcessObject dhcp_helper_process_post(body=body)

DhcpHelperProcessRoute.post

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
api_instance = polarisgenclient.DhcpHelperProcessApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.DhcpHelperProcessObject() # DhcpHelperProcessObject | DhcpHelperProcess object (optional)

try:
    # DhcpHelperProcessRoute.post
    api_response = api_instance.dhcp_helper_process_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DhcpHelperProcessApi->dhcp_helper_process_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DhcpHelperProcessObject**](DhcpHelperProcessObject.md)| DhcpHelperProcess object | [optional] 

### Return type

[**DhcpHelperProcessObject**](DhcpHelperProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dhcp_helper_process_put**
> DhcpHelperProcessObject dhcp_helper_process_put(device_name, body=body)

DhcpHelperProcessRoute.put

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
api_instance = polarisgenclient.DhcpHelperProcessApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | DhcpHelperProcess device_name
body = polarisgenclient.DhcpHelperProcessObject() # DhcpHelperProcessObject | DhcpHelperProcess object (optional)

try:
    # DhcpHelperProcessRoute.put
    api_response = api_instance.dhcp_helper_process_put(device_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DhcpHelperProcessApi->dhcp_helper_process_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| DhcpHelperProcess device_name | 
 **body** | [**DhcpHelperProcessObject**](DhcpHelperProcessObject.md)| DhcpHelperProcess object | [optional] 

### Return type

[**DhcpHelperProcessObject**](DhcpHelperProcessObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

