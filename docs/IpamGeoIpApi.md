# polarisgenclient.IpamGeoIpApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gtm_geo_ip_get**](IpamGeoIpApi.md#gtm_geo_ip_get) | **GET** /api/v0.1/gtm/geoip/{hostname} | GtmGeoIpRoute.get
[**gtm_geo_ip_post**](IpamGeoIpApi.md#gtm_geo_ip_post) | **POST** /api/v0.1/gtm/geoip/{hostname} | GtmGeoIpRoute.post
[**gtm_get**](IpamGeoIpApi.md#gtm_get) | **GET** /api/v0.1/gtm/dc | GtmRoute.get
[**gtm_get_by_name**](IpamGeoIpApi.md#gtm_get_by_name) | **GET** /api/v0.1/gtm/dc/{hostname} | GtmRoute.get
[**gtm_region_get**](IpamGeoIpApi.md#gtm_region_get) | **GET** /api/v0.1/gtm/region | GtmRegionRoute.get
[**gtm_region_get_resolve_by_state**](IpamGeoIpApi.md#gtm_region_get_resolve_by_state) | **GET** /api/v0.1/gtm/region/resolve/{country}/{state} | GtmRegionResolveRoute.get
[**gtm_region_resolve_get**](IpamGeoIpApi.md#gtm_region_resolve_get) | **GET** /api/v0.1/gtm/region/resolve/{country} | GtmRegionResolveRoute.get
[**gtm_topology_delete**](IpamGeoIpApi.md#gtm_topology_delete) | **POST** /api/v0.1/gtm/topo/delete | GtmTopologyRoute.delete
[**gtm_topology_get**](IpamGeoIpApi.md#gtm_topology_get) | **GET** /api/v0.1/gtm/topo | GtmTopologyRoute.get
[**gtm_topology_post**](IpamGeoIpApi.md#gtm_topology_post) | **POST** /api/v0.1/gtm/topo/create | GtmTopologyRoute.post
[**gtm_wide_ip_get**](IpamGeoIpApi.md#gtm_wide_ip_get) | **GET** /api/v0.1/gtm/wideip | GtmWideIpRoute.get
[**gtm_wide_ip_get_by_ip**](IpamGeoIpApi.md#gtm_wide_ip_get_by_ip) | **GET** /api/v0.1/gtm/wideip/{wideip} | GtmWideIpRoute.get
[**ipam_geo_provider_get**](IpamGeoIpApi.md#ipam_geo_provider_get) | **GET** /api/v0.1/ipam/geo/provider | IpamGeoProviderRoute.get
[**ipam_geo_provider_post**](IpamGeoIpApi.md#ipam_geo_provider_post) | **POST** /api/v0.1/ipam/geo/provider/{name}/resolve/{ip} | IpamGeoProviderRoute.post
[**ipam_geo_provider_post_by_network**](IpamGeoIpApi.md#ipam_geo_provider_post_by_network) | **POST** /api/v0.1/ipam/geo/provider/{name}/resolve/{ip}/{network} | IpamGeoProviderRoute.post


# **gtm_geo_ip_get**
> gtm_geo_ip_get(hostname)

GtmGeoIpRoute.get

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))
hostname = 'hostname_example' # str | GTM FQDN

try:
    # GtmGeoIpRoute.get
    api_instance.gtm_geo_ip_get(hostname)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->gtm_geo_ip_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| GTM FQDN | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gtm_geo_ip_post**
> gtm_geo_ip_post(hostname)

GtmGeoIpRoute.post

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))
hostname = 'hostname_example' # str | GTM FQDN

try:
    # GtmGeoIpRoute.post
    api_instance.gtm_geo_ip_post(hostname)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->gtm_geo_ip_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| GTM FQDN | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gtm_get**
> gtm_get()

GtmRoute.get

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))

try:
    # GtmRoute.get
    api_instance.gtm_get()
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->gtm_get: %s\n" % e)
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

# **gtm_get_by_name**
> gtm_get_by_name(hostname)

GtmRoute.get

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))
hostname = 'hostname_example' # str | datacenter name

try:
    # GtmRoute.get
    api_instance.gtm_get_by_name(hostname)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->gtm_get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| datacenter name | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gtm_region_get**
> gtm_region_get()

GtmRegionRoute.get

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))

try:
    # GtmRegionRoute.get
    api_instance.gtm_region_get()
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->gtm_region_get: %s\n" % e)
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

# **gtm_region_get_resolve_by_state**
> gtm_region_get_resolve_by_state(country, state)

GtmRegionResolveRoute.get

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))
country = 'country_example' # str | 2-letter Country code
state = 'state_example' # str | optional State or Province name

try:
    # GtmRegionResolveRoute.get
    api_instance.gtm_region_get_resolve_by_state(country, state)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->gtm_region_get_resolve_by_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| 2-letter Country code | 
 **state** | **str**| optional State or Province name | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gtm_region_resolve_get**
> gtm_region_resolve_get(country)

GtmRegionResolveRoute.get

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))
country = 'country_example' # str | 2-letter Country code

try:
    # GtmRegionResolveRoute.get
    api_instance.gtm_region_resolve_get(country)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->gtm_region_resolve_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| 2-letter Country code | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gtm_topology_delete**
> Body15 gtm_topology_delete(body=body)

GtmTopologyRoute.delete

Remove topology record

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.Body15() # Body15 | topo object (optional)

try:
    # GtmTopologyRoute.delete
    api_response = api_instance.gtm_topology_delete(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->gtm_topology_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body15**](Body15.md)| topo object | [optional] 

### Return type

[**Body15**](Body15.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gtm_topology_get**
> gtm_topology_get()

GtmTopologyRoute.get

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))

try:
    # GtmTopologyRoute.get
    api_instance.gtm_topology_get()
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->gtm_topology_get: %s\n" % e)
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

# **gtm_topology_post**
> object gtm_topology_post(body=body)

GtmTopologyRoute.post

Create a new topology record

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))
body = polarisgenclient.Body14() # Body14 | topo object (optional)

try:
    # GtmTopologyRoute.post
    api_response = api_instance.gtm_topology_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->gtm_topology_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body14**](Body14.md)| topo object | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gtm_wide_ip_get**
> gtm_wide_ip_get()

GtmWideIpRoute.get

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))

try:
    # GtmWideIpRoute.get
    api_instance.gtm_wide_ip_get()
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->gtm_wide_ip_get: %s\n" % e)
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

# **gtm_wide_ip_get_by_ip**
> gtm_wide_ip_get_by_ip(wideip)

GtmWideIpRoute.get

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))
wideip = 'wideip_example' # str | wideip hostname

try:
    # GtmWideIpRoute.get
    api_instance.gtm_wide_ip_get_by_ip(wideip)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->gtm_wide_ip_get_by_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wideip** | **str**| wideip hostname | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_geo_provider_get**
> list[str] ipam_geo_provider_get()

IpamGeoProviderRoute.get

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))

try:
    # IpamGeoProviderRoute.get
    api_response = api_instance.ipam_geo_provider_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->ipam_geo_provider_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_geo_provider_post**
> ipam_geo_provider_post(name, ip, network)

IpamGeoProviderRoute.post

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | GeoIp provider name
ip = 'ip_example' # str | ip
network = 'network_example' # str | IP or CIDR to resolve

try:
    # IpamGeoProviderRoute.post
    api_instance.ipam_geo_provider_post(name, ip, network)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->ipam_geo_provider_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| GeoIp provider name | 
 **ip** | **str**| ip | 
 **network** | **str**| IP or CIDR to resolve | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_geo_provider_post_by_network**
> ipam_geo_provider_post_by_network(name, ip, network)

IpamGeoProviderRoute.post

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
api_instance = polarisgenclient.IpamGeoIpApi(polarisgenclient.ApiClient(configuration))
name = 'name_example' # str | GeoIp provider name
ip = 'ip_example' # str | ip
network = 'network_example' # str | IP or CIDR to resolve

try:
    # IpamGeoProviderRoute.post
    api_instance.ipam_geo_provider_post_by_network(name, ip, network)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->ipam_geo_provider_post_by_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| GeoIp provider name | 
 **ip** | **str**| ip | 
 **network** | **str**| IP or CIDR to resolve | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

