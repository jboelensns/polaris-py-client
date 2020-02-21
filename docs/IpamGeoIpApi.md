# polarisgenclient.IpamGeoIpApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v01_gtm_dc_get**](IpamGeoIpApi.md#api_v01_gtm_dc_get) | **GET** /api/v0.1/gtm/dc | GtmRoute.get
[**api_v01_gtm_dc_hostname_get**](IpamGeoIpApi.md#api_v01_gtm_dc_hostname_get) | **GET** /api/v0.1/gtm/dc/{hostname} | GtmRoute.get
[**api_v01_gtm_geoip_hostname_get**](IpamGeoIpApi.md#api_v01_gtm_geoip_hostname_get) | **GET** /api/v0.1/gtm/geoip/{hostname} | GtmGeoIpRoute.get
[**api_v01_gtm_geoip_hostname_post**](IpamGeoIpApi.md#api_v01_gtm_geoip_hostname_post) | **POST** /api/v0.1/gtm/geoip/{hostname} | GtmGeoIpRoute.post
[**api_v01_gtm_region_get**](IpamGeoIpApi.md#api_v01_gtm_region_get) | **GET** /api/v0.1/gtm/region | GtmRegionRoute.get
[**api_v01_gtm_region_resolve_country_get**](IpamGeoIpApi.md#api_v01_gtm_region_resolve_country_get) | **GET** /api/v0.1/gtm/region/resolve/{country} | GtmRegionRoute.post
[**api_v01_gtm_region_resolve_country_state_get**](IpamGeoIpApi.md#api_v01_gtm_region_resolve_country_state_get) | **GET** /api/v0.1/gtm/region/resolve/{country}/{state} | GtmRegionRoute.post
[**api_v01_gtm_topo_create_post**](IpamGeoIpApi.md#api_v01_gtm_topo_create_post) | **POST** /api/v0.1/gtm/topo/create | GtmTopologyRoute.post
[**api_v01_gtm_topo_delete_post**](IpamGeoIpApi.md#api_v01_gtm_topo_delete_post) | **POST** /api/v0.1/gtm/topo/delete | GtmTopologyDeleteRoute.post
[**api_v01_gtm_topo_get**](IpamGeoIpApi.md#api_v01_gtm_topo_get) | **GET** /api/v0.1/gtm/topo | GtmTopologyRoute.get
[**api_v01_gtm_wideip_get**](IpamGeoIpApi.md#api_v01_gtm_wideip_get) | **GET** /api/v0.1/gtm/wideip | GtmWideIpRoute.get
[**api_v01_gtm_wideip_wideip_get**](IpamGeoIpApi.md#api_v01_gtm_wideip_wideip_get) | **GET** /api/v0.1/gtm/wideip/{wideip} | GtmWideIpRoute.get
[**api_v01_ipam_geo_provider_get**](IpamGeoIpApi.md#api_v01_ipam_geo_provider_get) | **GET** /api/v0.1/ipam/geo/provider | IpamGeoProviderRoute.get
[**api_v01_ipam_geo_provider_name_resolve_ip_network_post**](IpamGeoIpApi.md#api_v01_ipam_geo_provider_name_resolve_ip_network_post) | **POST** /api/v0.1/ipam/geo/provider/{name}/resolve/{ip}/{network} | IpamGeoProviderRoute.post
[**api_v01_ipam_geo_provider_name_resolve_ip_post**](IpamGeoIpApi.md#api_v01_ipam_geo_provider_name_resolve_ip_post) | **POST** /api/v0.1/ipam/geo/provider/{name}/resolve/{ip} | IpamGeoProviderRoute.post


# **api_v01_gtm_dc_get**
> api_v01_gtm_dc_get(hostname)

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
    api_instance.api_v01_gtm_dc_get(hostname)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_gtm_dc_get: %s\n" % e)
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

# **api_v01_gtm_dc_hostname_get**
> api_v01_gtm_dc_hostname_get(hostname)

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
    api_instance.api_v01_gtm_dc_hostname_get(hostname)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_gtm_dc_hostname_get: %s\n" % e)
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

# **api_v01_gtm_geoip_hostname_get**
> api_v01_gtm_geoip_hostname_get(hostname)

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
    api_instance.api_v01_gtm_geoip_hostname_get(hostname)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_gtm_geoip_hostname_get: %s\n" % e)
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

# **api_v01_gtm_geoip_hostname_post**
> api_v01_gtm_geoip_hostname_post(hostname)

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
    api_instance.api_v01_gtm_geoip_hostname_post(hostname)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_gtm_geoip_hostname_post: %s\n" % e)
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

# **api_v01_gtm_region_get**
> api_v01_gtm_region_get()

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
    api_instance.api_v01_gtm_region_get()
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_gtm_region_get: %s\n" % e)
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

# **api_v01_gtm_region_resolve_country_get**
> api_v01_gtm_region_resolve_country_get(country, state)

GtmRegionRoute.post

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
    # GtmRegionRoute.post
    api_instance.api_v01_gtm_region_resolve_country_get(country, state)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_gtm_region_resolve_country_get: %s\n" % e)
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

# **api_v01_gtm_region_resolve_country_state_get**
> api_v01_gtm_region_resolve_country_state_get(country, state)

GtmRegionRoute.post

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
    # GtmRegionRoute.post
    api_instance.api_v01_gtm_region_resolve_country_state_get(country, state)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_gtm_region_resolve_country_state_get: %s\n" % e)
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

# **api_v01_gtm_topo_create_post**
> object api_v01_gtm_topo_create_post(body=body)

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
    api_response = api_instance.api_v01_gtm_topo_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_gtm_topo_create_post: %s\n" % e)
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

# **api_v01_gtm_topo_delete_post**
> Body15 api_v01_gtm_topo_delete_post(body=body)

GtmTopologyDeleteRoute.post

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
    # GtmTopologyDeleteRoute.post
    api_response = api_instance.api_v01_gtm_topo_delete_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_gtm_topo_delete_post: %s\n" % e)
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

# **api_v01_gtm_topo_get**
> api_v01_gtm_topo_get()

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
    api_instance.api_v01_gtm_topo_get()
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_gtm_topo_get: %s\n" % e)
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

# **api_v01_gtm_wideip_get**
> api_v01_gtm_wideip_get(wideip)

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
    api_instance.api_v01_gtm_wideip_get(wideip)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_gtm_wideip_get: %s\n" % e)
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

# **api_v01_gtm_wideip_wideip_get**
> api_v01_gtm_wideip_wideip_get(wideip)

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
    api_instance.api_v01_gtm_wideip_wideip_get(wideip)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_gtm_wideip_wideip_get: %s\n" % e)
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

# **api_v01_ipam_geo_provider_get**
> list[str] api_v01_ipam_geo_provider_get()

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
    api_response = api_instance.api_v01_ipam_geo_provider_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_ipam_geo_provider_get: %s\n" % e)
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

# **api_v01_ipam_geo_provider_name_resolve_ip_network_post**
> api_v01_ipam_geo_provider_name_resolve_ip_network_post(name, ip, network)

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
    api_instance.api_v01_ipam_geo_provider_name_resolve_ip_network_post(name, ip, network)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_ipam_geo_provider_name_resolve_ip_network_post: %s\n" % e)
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

# **api_v01_ipam_geo_provider_name_resolve_ip_post**
> api_v01_ipam_geo_provider_name_resolve_ip_post(name, ip, network)

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
    api_instance.api_v01_ipam_geo_provider_name_resolve_ip_post(name, ip, network)
except ApiException as e:
    print("Exception when calling IpamGeoIpApi->api_v01_ipam_geo_provider_name_resolve_ip_post: %s\n" % e)
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

