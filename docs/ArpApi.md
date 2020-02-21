# polarisgenclient.ArpApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_arp_address_get**](ArpApi.md#api_v01_arp_address_get) | **GET** /api/v0.1/arp/{address} | ArpRoute.get
[**api_v01_arp_get**](ArpApi.md#api_v01_arp_get) | **GET** /api/v0.1/arp | ArpRoute.get
[**api_v01_device_device_name_arp_get**](ArpApi.md#api_v01_device_device_name_arp_get) | **GET** /api/v0.1/device/{device_name}/arp | ArpRoute.get
[**api_v01_device_device_name_arp_post**](ArpApi.md#api_v01_device_device_name_arp_post) | **POST** /api/v0.1/device/{device_name}/arp | ArpRoute.post


# **api_v01_arp_address_get**
> list[ArpListObject] api_v01_arp_address_get(address, device_name)

ArpRoute.get

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
api_instance = polarisgenclient.ArpApi(polarisgenclient.ApiClient(configuration))
address = 'address_example' # str | address
device_name = 'device_name_example' # str | Device FQDN

try:
    # ArpRoute.get
    api_response = api_instance.api_v01_arp_address_get(address, device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArpApi->api_v01_arp_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address | 
 **device_name** | **str**| Device FQDN | 

### Return type

[**list[ArpListObject]**](ArpListObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_arp_get**
> list[ArpListObject] api_v01_arp_get(address, device_name)

ArpRoute.get

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
api_instance = polarisgenclient.ArpApi(polarisgenclient.ApiClient(configuration))
address = 'address_example' # str | address
device_name = 'device_name_example' # str | Device FQDN

try:
    # ArpRoute.get
    api_response = api_instance.api_v01_arp_get(address, device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArpApi->api_v01_arp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address | 
 **device_name** | **str**| Device FQDN | 

### Return type

[**list[ArpListObject]**](ArpListObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_device_name_arp_get**
> list[ArpListObject] api_v01_device_device_name_arp_get(address, device_name)

ArpRoute.get

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
api_instance = polarisgenclient.ArpApi(polarisgenclient.ApiClient(configuration))
address = 'address_example' # str | address
device_name = 'device_name_example' # str | Device FQDN

try:
    # ArpRoute.get
    api_response = api_instance.api_v01_device_device_name_arp_get(address, device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArpApi->api_v01_device_device_name_arp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address | 
 **device_name** | **str**| Device FQDN | 

### Return type

[**list[ArpListObject]**](ArpListObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v01_device_device_name_arp_post**
> list[ArpListObject] api_v01_device_device_name_arp_post(device_name, body=body)

ArpRoute.post

Dispatch real time ARP scan

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
api_instance = polarisgenclient.ArpApi(polarisgenclient.ApiClient(configuration))
device_name = 'device_name_example' # str | Device FQDN
body = NULL # object | body (optional)

try:
    # ArpRoute.post
    api_response = api_instance.api_v01_device_device_name_arp_post(device_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArpApi->api_v01_device_device_name_arp_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 
 **body** | **object**| body | [optional] 

### Return type

[**list[ArpListObject]**](ArpListObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

