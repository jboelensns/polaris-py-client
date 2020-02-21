# polarisgenclient.MacApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_device_device_name_mac_get**](MacApi.md#api_v01_device_device_name_mac_get) | **GET** /api/v0.1/device/{device_name}/mac | MacRoute.get
[**api_v01_device_device_name_mac_post**](MacApi.md#api_v01_device_device_name_mac_post) | **POST** /api/v0.1/device/{device_name}/mac | MacRoute.post
[**api_v01_mac_address_get**](MacApi.md#api_v01_mac_address_get) | **GET** /api/v0.1/mac/{address} | MacRoute.get
[**api_v01_mac_get**](MacApi.md#api_v01_mac_get) | **GET** /api/v0.1/mac | MacRoute.get


# **api_v01_device_device_name_mac_get**
> list[object] api_v01_device_device_name_mac_get(device_name, address, address2=address2)

MacRoute.get

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
api_instance = polarisgenclient.MacApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
address = 'address_example' # str | address
address2 = 'address_example' # str | Mac Address (optional)

try:
    # MacRoute.get
    api_response = api_instance.api_v01_device_device_name_mac_get(device_name, address, address2=address2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MacApi->api_v01_device_device_name_mac_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **address** | **str**| address | 
 **address2** | **str**| Mac Address | [optional] 

### Return type

**list[object]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_device_name_mac_post**
> list[object] api_v01_device_device_name_mac_post(device_name)

MacRoute.post

Dispatch real time Mac scan

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
api_instance = polarisgenclient.MacApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN

try:
    # MacRoute.post
    api_response = api_instance.api_v01_device_device_name_mac_post(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MacApi->api_v01_device_device_name_mac_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 

### Return type

**list[object]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_mac_address_get**
> list[object] api_v01_mac_address_get(device_name, address, address2=address2)

MacRoute.get

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
api_instance = polarisgenclient.MacApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
address = 'address_example' # str | address
address2 = 'address_example' # str | Mac Address (optional)

try:
    # MacRoute.get
    api_response = api_instance.api_v01_mac_address_get(device_name, address, address2=address2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MacApi->api_v01_mac_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **address** | **str**| address | 
 **address2** | **str**| Mac Address | [optional] 

### Return type

**list[object]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_mac_get**
> list[object] api_v01_mac_get(device_name, address, address2=address2)

MacRoute.get

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
api_instance = polarisgenclient.MacApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
address = 'address_example' # str | address
address2 = 'address_example' # str | Mac Address (optional)

try:
    # MacRoute.get
    api_response = api_instance.api_v01_mac_get(device_name, address, address2=address2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MacApi->api_v01_mac_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **address** | **str**| address | 
 **address2** | **str**| Mac Address | [optional] 

### Return type

**list[object]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

