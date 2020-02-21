# polarisgenclient.IpamGeoFeedApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_ipam_geo_feed_csv_delete**](IpamGeoFeedApi.md#api_v01_ipam_geo_feed_csv_delete) | **DELETE** /api/v0.1/ipam/geo/feed.csv | IpamGeoFeedRoute.delete
[**api_v01_ipam_geo_feed_csv_get**](IpamGeoFeedApi.md#api_v01_ipam_geo_feed_csv_get) | **GET** /api/v0.1/ipam/geo/feed.csv | IpamGeoFeedRoute.get


# **api_v01_ipam_geo_feed_csv_delete**
> api_v01_ipam_geo_feed_csv_delete()

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
    api_instance.api_v01_ipam_geo_feed_csv_delete()
except ApiException as e:
    print("Exception when calling IpamGeoFeedApi->api_v01_ipam_geo_feed_csv_delete: %s\n" % e)
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

# **api_v01_ipam_geo_feed_csv_get**
> api_v01_ipam_geo_feed_csv_get()

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
    api_instance.api_v01_ipam_geo_feed_csv_get()
except ApiException as e:
    print("Exception when calling IpamGeoFeedApi->api_v01_ipam_geo_feed_csv_get: %s\n" % e)
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

