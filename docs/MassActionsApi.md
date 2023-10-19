# clientapi_atrocore.MassActionsApi

All URIs are relative to *https://demo.atropim.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upsert**](MassActionsApi.md#upsert) | **POST** /MassActions/action/upsert | Bulk create and bulk update.


# **upsert**
> List[object] upsert(request_body, use_queue=use_queue)

Bulk create and bulk update.

Bulk create and bulk update.

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
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

# Configure API key authorization: Authorization-Token
configuration.api_key['Authorization-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_atrocore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_atrocore.MassActionsApi(api_client)
    request_body = None # List[object] | 
    use_queue = false # bool |  (optional)

    try:
        # Bulk create and bulk update.
        api_response = api_instance.upsert(request_body, use_queue=use_queue)
        print("The response of MassActionsApi->upsert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MassActionsApi->upsert: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[object]**](object.md)|  | 
 **use_queue** | **bool**|  | [optional] 

### Return type

**List[object]**

### Authorization

[Authorization-Token](../README.md#Authorization-Token)

### HTTP request headers

 - **Content-Type**: application/json
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

