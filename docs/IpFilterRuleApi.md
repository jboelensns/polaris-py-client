# polarisgenclient.IpFilterRuleApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ip_filter_rule_delete**](IpFilterRuleApi.md#ip_filter_rule_delete) | **DELETE** /api/v0.1/ipfilter/{ip_filter_id}/rule/{id}/seq/{seq} | IpFilterRuleRoute.delete
[**ip_filter_rule_get**](IpFilterRuleApi.md#ip_filter_rule_get) | **GET** /api/v0.1/ipfilter/rule | IpFilterRuleRoute.get
[**ip_filter_rule_get_by_id**](IpFilterRuleApi.md#ip_filter_rule_get_by_id) | **GET** /api/v0.1/ipfilter/{ip_filter_id}/rule | IpFilterRuleRoute.get
[**ip_filter_rule_post**](IpFilterRuleApi.md#ip_filter_rule_post) | **POST** /api/v0.1/ipfilter/rule | IpFilterRuleRoute.post
[**ip_filter_rule_put**](IpFilterRuleApi.md#ip_filter_rule_put) | **PUT** /api/v0.1/ipfilter/{ip_filter_id}/rule/{id}/seq/{seq} | IpFilterRuleRoute.put


# **ip_filter_rule_delete**
> IpFilterRuleObject ip_filter_rule_delete(ip_filter_id, id, seq)

IpFilterRuleRoute.delete

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
api_instance = polarisgenclient.IpFilterRuleApi(polarisgenclient.ApiClient(configuration))
ip_filter_id = 'ip_filter_id_example' # str | IpFilter id name
id = 'id_example' # str | UUID1 string
seq = 56 # int | seq

try:
    # IpFilterRuleRoute.delete
    api_response = api_instance.ip_filter_rule_delete(ip_filter_id, id, seq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpFilterRuleApi->ip_filter_rule_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_filter_id** | **str**| IpFilter id name | 
 **id** | **str**| UUID1 string | 
 **seq** | **int**| seq | 

### Return type

[**IpFilterRuleObject**](IpFilterRuleObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_filter_rule_get**
> IpFilterRuleObject ip_filter_rule_get()

IpFilterRuleRoute.get

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
api_instance = polarisgenclient.IpFilterRuleApi(polarisgenclient.ApiClient(configuration))

try:
    # IpFilterRuleRoute.get
    api_response = api_instance.ip_filter_rule_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpFilterRuleApi->ip_filter_rule_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IpFilterRuleObject**](IpFilterRuleObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_filter_rule_get_by_id**
> IpFilterRuleObject ip_filter_rule_get_by_id(ip_filter_id)

IpFilterRuleRoute.get

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
api_instance = polarisgenclient.IpFilterRuleApi(polarisgenclient.ApiClient(configuration))
ip_filter_id = 'ip_filter_id_example' # str | IpFilter id

try:
    # IpFilterRuleRoute.get
    api_response = api_instance.ip_filter_rule_get_by_id(ip_filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpFilterRuleApi->ip_filter_rule_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_filter_id** | **str**| IpFilter id | 

### Return type

[**IpFilterRuleObject**](IpFilterRuleObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_filter_rule_post**
> IpFilterRuleObject ip_filter_rule_post(body=body)

IpFilterRuleRoute.post

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
api_instance = polarisgenclient.IpFilterRuleApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.IpFilterRuleObject() # IpFilterRuleObject | IpFilterRule object (optional)

try:
    # IpFilterRuleRoute.post
    api_response = api_instance.ip_filter_rule_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpFilterRuleApi->ip_filter_rule_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IpFilterRuleObject**](IpFilterRuleObject.md)| IpFilterRule object | [optional] 

### Return type

[**IpFilterRuleObject**](IpFilterRuleObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_filter_rule_put**
> IpFilterRuleObject ip_filter_rule_put(ip_filter_id, id, seq, body=body)

IpFilterRuleRoute.put

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
api_instance = polarisgenclient.IpFilterRuleApi(polarisgenclient.ApiClient(configuration))
ip_filter_id = 'ip_filter_id_example' # str | IpFilterRule id
id = 'id_example' # str | UUID1 string
seq = 56 # int | seq
body = polarisgenclient.IpFilterRuleObject() # IpFilterRuleObject | IpFilterRule object (optional)

try:
    # IpFilterRuleRoute.put
    api_response = api_instance.ip_filter_rule_put(ip_filter_id, id, seq, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpFilterRuleApi->ip_filter_rule_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_filter_id** | **str**| IpFilterRule id | 
 **id** | **str**| UUID1 string | 
 **seq** | **int**| seq | 
 **body** | [**IpFilterRuleObject**](IpFilterRuleObject.md)| IpFilterRule object | [optional] 

### Return type

[**IpFilterRuleObject**](IpFilterRuleObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

