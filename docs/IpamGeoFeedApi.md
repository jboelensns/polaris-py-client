# polarisgenclient.IpamGeoFeedApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipam_geo_feed_delete**](IpamGeoFeedApi.md#ipam_geo_feed_delete) | **DELETE** /api/v0.1/ipam/geo/feed.csv | IpamGeoFeedRoute.delete
[**ipam_geo_feed_get**](IpamGeoFeedApi.md#ipam_geo_feed_get) | **GET** /api/v0.1/ipam/geo/feed.csv | IpamGeoFeedRoute.get


# **ipam_geo_feed_delete**
> ipam_geo_feed_delete()

IpamGeoFeedRoute.delete

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
api_instance = polarisgenclient.IpamGeoFeedApi(polarisgenclient.ApiClient(configuration))

try:
    # IpamGeoFeedRoute.delete
    api_instance.ipam_geo_feed_delete()
except ApiException as e:
    print("Exception when calling IpamGeoFeedApi->ipam_geo_feed_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_geo_feed_get**
> ipam_geo_feed_get()

IpamGeoFeedRoute.get

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
api_instance = polarisgenclient.IpamGeoFeedApi(polarisgenclient.ApiClient(configuration))

try:
    # IpamGeoFeedRoute.get
    api_instance.ipam_geo_feed_get()
except ApiException as e:
    print("Exception when calling IpamGeoFeedApi->ipam_geo_feed_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

