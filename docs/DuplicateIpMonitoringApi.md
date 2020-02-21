# polarisgenclient.DuplicateIpMonitoringApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**duplicate_ip_monitoring_get**](DuplicateIpMonitoringApi.md#duplicate_ip_monitoring_get) | **GET** /api/v0.1/monitoring/duplicate/ip | DuplicateIpMonitoringRoute.get


# **duplicate_ip_monitoring_get**
> DuplicateIpMonitoringObject duplicate_ip_monitoring_get()

DuplicateIpMonitoringRoute.get

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
api_instance = polarisgenclient.DuplicateIpMonitoringApi(polarisgenclient.ApiClient(configuration))

try:
    # DuplicateIpMonitoringRoute.get
    api_response = api_instance.duplicate_ip_monitoring_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DuplicateIpMonitoringApi->duplicate_ip_monitoring_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DuplicateIpMonitoringObject**](DuplicateIpMonitoringObject.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

