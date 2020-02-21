# polarisgenclient.ArpApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**arp_get**](ArpApi.md#arp_get) | **GET** /api/v0.1/arp | ArpRoute.get
[**arp_get_by_address**](ArpApi.md#arp_get_by_address) | **GET** /api/v0.1/arp/{address} | ArpRoute.get
[**arp_get_by_device**](ArpApi.md#arp_get_by_device) | **GET** /api/v0.1/device/{device_name}/arp | ArpRoute.get
[**arp_post**](ArpApi.md#arp_post) | **POST** /api/v0.1/device/{device_name}/arp | ArpRoute.post


# **arp_get**
> list[ArpListObject] arp_get()

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

try:
    # ArpRoute.get
    api_response = api_instance.arp_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArpApi->arp_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ArpListObject]**](ArpListObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arp_get_by_address**
> list[ArpListObject] arp_get_by_address(address)

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

try:
    # ArpRoute.get
    api_response = api_instance.arp_get_by_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArpApi->arp_get_by_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address | 

### Return type

[**list[ArpListObject]**](ArpListObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arp_get_by_device**
> list[ArpListObject] arp_get_by_device(device_name)

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
device_name = 'device_name_example' # str | Device FQDN

try:
    # ArpRoute.get
    api_response = api_instance.arp_get_by_device(device_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArpApi->arp_get_by_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_name** | **str**| Device FQDN | 

### Return type

[**list[ArpListObject]**](ArpListObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arp_post**
> list[ArpListObject] arp_post(device_name, body=body)

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
    api_response = api_instance.arp_post(device_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArpApi->arp_post: %s\n" % e)
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

