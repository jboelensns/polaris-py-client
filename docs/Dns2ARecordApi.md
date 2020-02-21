# polarisgenclient.Dns2ARecordApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dns2_a_record_delete**](Dns2ARecordApi.md#dns2_a_record_delete) | **DELETE** /api/v0.1/dns2/record/{zone}/{name} | Dns2ARecordRoute.delete
[**dns2_a_record_delete_by_ip**](Dns2ARecordApi.md#dns2_a_record_delete_by_ip) | **DELETE** /api/v0.1/dns2/record/{zone}/{name}/{type}/{ip} | Dns2ARecordRoute.delete
[**dns2_a_record_get**](Dns2ARecordApi.md#dns2_a_record_get) | **GET** /api/v0.1/dns2/record/{zone}/{name} | Dns2ARecordRoute.get


# **dns2_a_record_delete**
> DnsRecordObject dns2_a_record_delete(zone, name)

Dns2ARecordRoute.delete

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
api_instance = polarisgenclient.Dns2ARecordApi(polarisgenclient.ApiClient(configuration))
zone = 'zone_example' # str | zone for record
name = 'name_example' # str | name for fqdn

try:
    # Dns2ARecordRoute.delete
    api_response = api_instance.dns2_a_record_delete(zone, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Dns2ARecordApi->dns2_a_record_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| zone for record | 
 **name** | **str**| name for fqdn | 

### Return type

[**DnsRecordObject**](DnsRecordObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns2_a_record_delete_by_ip**
> DnsRecordObject dns2_a_record_delete_by_ip(zone, name, type, ip)

Dns2ARecordRoute.delete

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
api_instance = polarisgenclient.Dns2ARecordApi(polarisgenclient.ApiClient(configuration))
zone = 'zone_example' # str | zone for record
name = 'name_example' # str | name for fqdn
type = 'type_example' # str | type of record to delete
ip = 'ip_example' # str | ip address

try:
    # Dns2ARecordRoute.delete
    api_response = api_instance.dns2_a_record_delete_by_ip(zone, name, type, ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Dns2ARecordApi->dns2_a_record_delete_by_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| zone for record | 
 **name** | **str**| name for fqdn | 
 **type** | **str**| type of record to delete | 
 **ip** | **str**| ip address | 

### Return type

[**DnsRecordObject**](DnsRecordObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dns2_a_record_get**
> DnsRecordObject dns2_a_record_get(zone, name)

Dns2ARecordRoute.get

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
api_instance = polarisgenclient.Dns2ARecordApi(polarisgenclient.ApiClient(configuration))
zone = 'zone_example' # str | fqdn
name = 'name_example' # str | name

try:
    # Dns2ARecordRoute.get
    api_response = api_instance.dns2_a_record_get(zone, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Dns2ARecordApi->dns2_a_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| fqdn | 
 **name** | **str**| name | 

### Return type

[**DnsRecordObject**](DnsRecordObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

