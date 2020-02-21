# polarisgenclient.AuthJwtApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_jwt_post**](AuthJwtApi.md#auth_jwt_post) | **POST** /api/v0.1/auth/jwt | AuthJwt.post


# **auth_jwt_post**
> auth_jwt_post(token=token)

AuthJwt.post

### Example
```python
from __future__ import print_function
import time
import polarisgenclient
from polarisgenclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = polarisgenclient.AuthJwtApi()
token = polarisgenclient.Token() # Token | Validate JWT signature (optional)

try:
    # AuthJwt.post
    api_instance.auth_jwt_post(token=token)
except ApiException as e:
    print("Exception when calling AuthJwtApi->auth_jwt_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**Token**](Token.md)| Validate JWT signature | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

