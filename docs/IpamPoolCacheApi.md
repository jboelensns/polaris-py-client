# polarisgenclient.IpamPoolCacheApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipam_pool_cache_get**](IpamPoolCacheApi.md#ipam_pool_cache_get) | **GET** /api/v0.1/ipam/pool/cache | IpamPoolCacheRoute.get


# **ipam_pool_cache_get**
> IPAMPoolResponse ipam_pool_cache_get()

IpamPoolCacheRoute.get

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
api_instance = polarisgenclient.IpamPoolCacheApi(polarisgenclient.ApiClient(configuration))

try:
    # IpamPoolCacheRoute.get
    api_response = api_instance.ipam_pool_cache_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamPoolCacheApi->ipam_pool_cache_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IPAMPoolResponse**](IPAMPoolResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

