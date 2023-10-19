# clientapi_atrocore.AppApi

All URIs are relative to *https://demo.atropim.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authorized_user_data**](AppApi.md#get_authorized_user_data) | **GET** /App/user | Generate authorization token and return authorized user data.


# **get_authorized_user_data**
> GetAuthorizedUserData200Response get_authorized_user_data(authorization_token_only, authorization_token_lifetime=authorization_token_lifetime, authorization_token_idletime=authorization_token_idletime)

Generate authorization token and return authorized user data.

Generate authorization token and return authorized user data.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.get_authorized_user_data200_response import GetAuthorizedUserData200Response
from clientapi_atrocore.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.atropim.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_atrocore.Configuration(
    host = "https://demo.atropim.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = clientapi_atrocore.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with clientapi_atrocore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_atrocore.AppApi(api_client)
    authorization_token_only = true # bool | 
    authorization_token_lifetime = 0 # int | Lifetime should be set in hours. 0 means no expiration. If this parameter is not passed, the globally configured parameter is used. (optional)
    authorization_token_idletime = 0 # int | Idletime should be set in hours. 0 means no expiration. If this parameter is not passed, the globally configured parameter is used. (optional)

    try:
        # Generate authorization token and return authorized user data.
        api_response = api_instance.get_authorized_user_data(authorization_token_only, authorization_token_lifetime=authorization_token_lifetime, authorization_token_idletime=authorization_token_idletime)
        print("The response of AppApi->get_authorized_user_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppApi->get_authorized_user_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_token_only** | **bool**|  | 
 **authorization_token_lifetime** | **int**| Lifetime should be set in hours. 0 means no expiration. If this parameter is not passed, the globally configured parameter is used. | [optional] 
 **authorization_token_idletime** | **int**| Idletime should be set in hours. 0 means no expiration. If this parameter is not passed, the globally configured parameter is used. | [optional] 

### Return type

[**GetAuthorizedUserData200Response**](GetAuthorizedUserData200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

