# polarisgenclient.DhcpHelperProcessApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_device_device_name_dhcp_helper_delete**](DhcpHelperProcessApi.md#api_v01_device_device_name_dhcp_helper_delete) | **DELETE** /api/v0.1/device/{device_name}/dhcp/helper | DhcpHelperProcessRoute.delete
[**api_v01_device_device_name_dhcp_helper_get**](DhcpHelperProcessApi.md#api_v01_device_device_name_dhcp_helper_get) | **GET** /api/v0.1/device/{device_name}/dhcp/helper | DhcpHelperProcessRoute.get
[**api_v01_device_device_name_dhcp_helper_put**](DhcpHelperProcessApi.md#api_v01_device_device_name_dhcp_helper_put) | **PUT** /api/v0.1/device/{device_name}/dhcp/helper | DhcpHelperProcessRoute.put
[**api_v01_dhcp_helper_get**](DhcpHelperProcessApi.md#api_v01_dhcp_helper_get) | **GET** /api/v0.1/dhcp/helper | DhcpHelperProcessRoute.get
[**api_v01_dhcp_helper_post**](DhcpHelperProcessApi.md#api_v01_dhcp_helper_post) | **POST** /api/v0.1/dhcp/helper | DhcpHelperProcessRoute.post


# **api_v01_device_device_name_dhcp_helper_delete**
> DhcpHelperProcessObject api_v01_device_device_name_dhcp_helper_delete(device_name, port, dst_ipv4_address)

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
    api_response = api_instance.api_v01_device_device_name_dhcp_helper_delete(device_name, port, dst_ipv4_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DhcpHelperProcessApi->api_v01_device_device_name_dhcp_helper_delete: %s\n" % e)
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

# **api_v01_device_device_name_dhcp_helper_get**
> DhcpHelperProcessObject api_v01_device_device_name_dhcp_helper_get(device_name)

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
    api_response = api_instance.api_v01_device_device_name_dhcp_helper_get(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DhcpHelperProcessApi->api_v01_device_device_name_dhcp_helper_get: %s\n" % e)
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

# **api_v01_device_device_name_dhcp_helper_put**
> DhcpHelperProcessObject api_v01_device_device_name_dhcp_helper_put(device_name, body=body)

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
    api_response = api_instance.api_v01_device_device_name_dhcp_helper_put(device_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DhcpHelperProcessApi->api_v01_device_device_name_dhcp_helper_put: %s\n" % e)
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

# **api_v01_dhcp_helper_get**
> DhcpHelperProcessObject api_v01_dhcp_helper_get(device_name)

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
    api_response = api_instance.api_v01_dhcp_helper_get(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DhcpHelperProcessApi->api_v01_dhcp_helper_get: %s\n" % e)
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

# **api_v01_dhcp_helper_post**
> DhcpHelperProcessObject api_v01_dhcp_helper_post(body=body)

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
    api_response = api_instance.api_v01_dhcp_helper_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DhcpHelperProcessApi->api_v01_dhcp_helper_post: %s\n" % e)
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

