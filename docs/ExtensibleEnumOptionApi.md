# clientapi_atrocore.ExtensibleEnumOptionApi

All URIs are relative to *https://demo.atropim.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation_for_extensible_enum_option**](ExtensibleEnumOptionApi.md#add_relation_for_extensible_enum_option) | **POST** /ExtensibleEnumOption/{link}/relation | Add relation for ExtensibleEnumOption
[**create_extensible_enum_option_item**](ExtensibleEnumOptionApi.md#create_extensible_enum_option_item) | **POST** /ExtensibleEnumOption | Create a record of the ExtensibleEnumOption
[**delete_extensible_enum_option_item**](ExtensibleEnumOptionApi.md#delete_extensible_enum_option_item) | **DELETE** /ExtensibleEnumOption/{id} | Delete a record of the ExtensibleEnumOption
[**follow_extensible_enum_option**](ExtensibleEnumOptionApi.md#follow_extensible_enum_option) | **PUT** /ExtensibleEnumOption/{id}/subscription | Follow the ExtensibleEnumOption stream
[**get_extensible_enum_option_item**](ExtensibleEnumOptionApi.md#get_extensible_enum_option_item) | **GET** /ExtensibleEnumOption/{id} | Returns a record of the ExtensibleEnumOption
[**get_linked_items_for_extensible_enum_option_item**](ExtensibleEnumOptionApi.md#get_linked_items_for_extensible_enum_option_item) | **GET** /ExtensibleEnumOption/{id}/{link} | Returns linked entities for the ExtensibleEnumOption
[**get_list_of_extensible_enum_option_items**](ExtensibleEnumOptionApi.md#get_list_of_extensible_enum_option_items) | **GET** /ExtensibleEnumOption | Returns a collection of ExtensibleEnumOption records
[**link_extensible_enum_option**](ExtensibleEnumOptionApi.md#link_extensible_enum_option) | **POST** /ExtensibleEnumOption/{id}/{link} | Link ExtensibleEnumOption to Entities
[**mass_delete_extensible_enum_option**](ExtensibleEnumOptionApi.md#mass_delete_extensible_enum_option) | **POST** /ExtensibleEnumOption/action/massDelete | Mass delete of ExtensibleEnumOption data
[**mass_update_extensible_enum_option**](ExtensibleEnumOptionApi.md#mass_update_extensible_enum_option) | **PUT** /ExtensibleEnumOption/action/massUpdate | Mass update of ExtensibleEnumOption data
[**remove_relation_for_extensible_enum_option**](ExtensibleEnumOptionApi.md#remove_relation_for_extensible_enum_option) | **DELETE** /ExtensibleEnumOption/{link}/relation | Remove relation for ExtensibleEnumOption
[**unfollow_extensible_enum_option**](ExtensibleEnumOptionApi.md#unfollow_extensible_enum_option) | **DELETE** /ExtensibleEnumOption/{id}/subscription | Unfollow the ExtensibleEnumOption stream
[**unlink_extensible_enum_option**](ExtensibleEnumOptionApi.md#unlink_extensible_enum_option) | **DELETE** /ExtensibleEnumOption/{id}/{link} | Unlink ExtensibleEnumOption from Entities
[**update_extensible_enum_option_item**](ExtensibleEnumOptionApi.md#update_extensible_enum_option_item) | **PUT** /ExtensibleEnumOption/{id} | Update a record of the ExtensibleEnumOption


# **add_relation_for_extensible_enum_option**
> bool add_relation_for_extensible_enum_option(link, ids, foreign_ids)

Add relation for ExtensibleEnumOption

Add relation for ExtensibleEnumOption

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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Add relation for ExtensibleEnumOption
        api_response = api_instance.add_relation_for_extensible_enum_option(link, ids, foreign_ids)
        print("The response of ExtensibleEnumOptionApi->add_relation_for_extensible_enum_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->add_relation_for_extensible_enum_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link** | **str**|  | 
 **ids** | [**List[str]**](str.md)|  | 
 **foreign_ids** | [**List[str]**](str.md)|  | 

### Return type

**bool**

### Authorization

[Authorization-Token](../README.md#Authorization-Token)

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

# **create_extensible_enum_option_item**
> ExtensibleEnumOption create_extensible_enum_option_item(create_extensible_enum_option_item_request)

Create a record of the ExtensibleEnumOption

Create a record of the ExtensibleEnumOption

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.create_extensible_enum_option_item_request import CreateExtensibleEnumOptionItemRequest
from clientapi_atrocore.models.extensible_enum_option import ExtensibleEnumOption
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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    create_extensible_enum_option_item_request = clientapi_atrocore.CreateExtensibleEnumOptionItemRequest() # CreateExtensibleEnumOptionItemRequest | 

    try:
        # Create a record of the ExtensibleEnumOption
        api_response = api_instance.create_extensible_enum_option_item(create_extensible_enum_option_item_request)
        print("The response of ExtensibleEnumOptionApi->create_extensible_enum_option_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->create_extensible_enum_option_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_extensible_enum_option_item_request** | [**CreateExtensibleEnumOptionItemRequest**](CreateExtensibleEnumOptionItemRequest.md)|  | 

### Return type

[**ExtensibleEnumOption**](ExtensibleEnumOption.md)

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

# **delete_extensible_enum_option_item**
> bool delete_extensible_enum_option_item(id)

Delete a record of the ExtensibleEnumOption

Delete a record of the ExtensibleEnumOption

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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a record of the ExtensibleEnumOption
        api_response = api_instance.delete_extensible_enum_option_item(id)
        print("The response of ExtensibleEnumOptionApi->delete_extensible_enum_option_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->delete_extensible_enum_option_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bool**

### Authorization

[Authorization-Token](../README.md#Authorization-Token)

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

# **follow_extensible_enum_option**
> FollowAccount200Response follow_extensible_enum_option(id)

Follow the ExtensibleEnumOption stream

Follow the ExtensibleEnumOption stream

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.follow_account200_response import FollowAccount200Response
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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    id = 'id_example' # str | 

    try:
        # Follow the ExtensibleEnumOption stream
        api_response = api_instance.follow_extensible_enum_option(id)
        print("The response of ExtensibleEnumOptionApi->follow_extensible_enum_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->follow_extensible_enum_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**FollowAccount200Response**](FollowAccount200Response.md)

### Authorization

[Authorization-Token](../README.md#Authorization-Token)

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

# **get_extensible_enum_option_item**
> ExtensibleEnumOption get_extensible_enum_option_item(id, language=language)

Returns a record of the ExtensibleEnumOption

Returns a record of the ExtensibleEnumOption

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.extensible_enum_option import ExtensibleEnumOption
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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    id = 'id_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns a record of the ExtensibleEnumOption
        api_response = api_instance.get_extensible_enum_option_item(id, language=language)
        print("The response of ExtensibleEnumOptionApi->get_extensible_enum_option_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->get_extensible_enum_option_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 

### Return type

[**ExtensibleEnumOption**](ExtensibleEnumOption.md)

### Authorization

[Authorization-Token](../README.md#Authorization-Token)

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

# **get_linked_items_for_extensible_enum_option_item**
> GetLinkedItemsForAccountItem200Response get_linked_items_for_extensible_enum_option_item(id, link, language=language)

Returns linked entities for the ExtensibleEnumOption

Returns linked entities for the ExtensibleEnumOption

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.get_linked_items_for_account_item200_response import GetLinkedItemsForAccountItem200Response
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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns linked entities for the ExtensibleEnumOption
        api_response = api_instance.get_linked_items_for_extensible_enum_option_item(id, link, language=language)
        print("The response of ExtensibleEnumOptionApi->get_linked_items_for_extensible_enum_option_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->get_linked_items_for_extensible_enum_option_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **link** | **str**|  | 
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 

### Return type

[**GetLinkedItemsForAccountItem200Response**](GetLinkedItemsForAccountItem200Response.md)

### Authorization

[Authorization-Token](../README.md#Authorization-Token)

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

# **get_list_of_extensible_enum_option_items**
> GetListOfExtensibleEnumOptionItems200Response get_list_of_extensible_enum_option_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)

Returns a collection of ExtensibleEnumOption records

Returns a collection of ExtensibleEnumOption records

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.get_list_of_extensible_enum_option_items200_response import GetListOfExtensibleEnumOptionItems200Response
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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)
    select = 'name,createdAt' # str | Available fields: code, color, createdAt, createdBy, createdById, createdByName, deleted, extensibleEnum, extensibleEnumId, extensibleEnumName, filterCreateImportJob, filterUpdateImportJob, id, listMultilingual, modifiedAt, modifiedBy, modifiedById, modifiedByName, name, nameDeDe, sortOrder (optional)
    where = None # List[object] | There are a lot of filter types supported. You can learn all of them if you trace what's requested by Atro UI in the network tab in your browser console (press F12 key to open the console). (optional)
    offset = 0 # int |  (optional)
    max_size = 50 # int |  (optional)
    sort_by = 'name' # str |  (optional)
    asc = true # bool |  (optional)

    try:
        # Returns a collection of ExtensibleEnumOption records
        api_response = api_instance.get_list_of_extensible_enum_option_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)
        print("The response of ExtensibleEnumOptionApi->get_list_of_extensible_enum_option_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->get_list_of_extensible_enum_option_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 
 **select** | **str**| Available fields: code, color, createdAt, createdBy, createdById, createdByName, deleted, extensibleEnum, extensibleEnumId, extensibleEnumName, filterCreateImportJob, filterUpdateImportJob, id, listMultilingual, modifiedAt, modifiedBy, modifiedById, modifiedByName, name, nameDeDe, sortOrder | [optional] 
 **where** | [**List[object]**](object.md)| There are a lot of filter types supported. You can learn all of them if you trace what&#39;s requested by Atro UI in the network tab in your browser console (press F12 key to open the console). | [optional] 
 **offset** | **int**|  | [optional] 
 **max_size** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **asc** | **bool**|  | [optional] 

### Return type

[**GetListOfExtensibleEnumOptionItems200Response**](GetListOfExtensibleEnumOptionItems200Response.md)

### Authorization

[Authorization-Token](../README.md#Authorization-Token)

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

# **link_extensible_enum_option**
> bool link_extensible_enum_option(id, link, link_account_request)

Link ExtensibleEnumOption to Entities

Link ExtensibleEnumOption to Entities

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.link_account_request import LinkAccountRequest
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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Link ExtensibleEnumOption to Entities
        api_response = api_instance.link_extensible_enum_option(id, link, link_account_request)
        print("The response of ExtensibleEnumOptionApi->link_extensible_enum_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->link_extensible_enum_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **link** | **str**|  | 
 **link_account_request** | [**LinkAccountRequest**](LinkAccountRequest.md)|  | 

### Return type

**bool**

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

# **mass_delete_extensible_enum_option**
> bool mass_delete_extensible_enum_option(link_account_request)

Mass delete of ExtensibleEnumOption data

Mass delete of ExtensibleEnumOption data

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.link_account_request import LinkAccountRequest
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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Mass delete of ExtensibleEnumOption data
        api_response = api_instance.mass_delete_extensible_enum_option(link_account_request)
        print("The response of ExtensibleEnumOptionApi->mass_delete_extensible_enum_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->mass_delete_extensible_enum_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_account_request** | [**LinkAccountRequest**](LinkAccountRequest.md)|  | 

### Return type

**bool**

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

# **mass_update_extensible_enum_option**
> bool mass_update_extensible_enum_option(mass_update_account_request)

Mass update of ExtensibleEnumOption data

Mass update of ExtensibleEnumOption data

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.mass_update_account_request import MassUpdateAccountRequest
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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    mass_update_account_request = clientapi_atrocore.MassUpdateAccountRequest() # MassUpdateAccountRequest | 

    try:
        # Mass update of ExtensibleEnumOption data
        api_response = api_instance.mass_update_extensible_enum_option(mass_update_account_request)
        print("The response of ExtensibleEnumOptionApi->mass_update_extensible_enum_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->mass_update_extensible_enum_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mass_update_account_request** | [**MassUpdateAccountRequest**](MassUpdateAccountRequest.md)|  | 

### Return type

**bool**

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

# **remove_relation_for_extensible_enum_option**
> bool remove_relation_for_extensible_enum_option(link, ids, foreign_ids)

Remove relation for ExtensibleEnumOption

Remove relation for ExtensibleEnumOption

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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Remove relation for ExtensibleEnumOption
        api_response = api_instance.remove_relation_for_extensible_enum_option(link, ids, foreign_ids)
        print("The response of ExtensibleEnumOptionApi->remove_relation_for_extensible_enum_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->remove_relation_for_extensible_enum_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link** | **str**|  | 
 **ids** | [**List[str]**](str.md)|  | 
 **foreign_ids** | [**List[str]**](str.md)|  | 

### Return type

**bool**

### Authorization

[Authorization-Token](../README.md#Authorization-Token)

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

# **unfollow_extensible_enum_option**
> bool unfollow_extensible_enum_option(id)

Unfollow the ExtensibleEnumOption stream

Unfollow the ExtensibleEnumOption stream

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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unfollow the ExtensibleEnumOption stream
        api_response = api_instance.unfollow_extensible_enum_option(id)
        print("The response of ExtensibleEnumOptionApi->unfollow_extensible_enum_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->unfollow_extensible_enum_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**bool**

### Authorization

[Authorization-Token](../README.md#Authorization-Token)

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

# **unlink_extensible_enum_option**
> bool unlink_extensible_enum_option(id, link, ids)

Unlink ExtensibleEnumOption from Entities

Unlink ExtensibleEnumOption from Entities

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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 

    try:
        # Unlink ExtensibleEnumOption from Entities
        api_response = api_instance.unlink_extensible_enum_option(id, link, ids)
        print("The response of ExtensibleEnumOptionApi->unlink_extensible_enum_option:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->unlink_extensible_enum_option: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **link** | **str**|  | 
 **ids** | [**List[str]**](str.md)|  | 

### Return type

**bool**

### Authorization

[Authorization-Token](../README.md#Authorization-Token)

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

# **update_extensible_enum_option_item**
> ExtensibleEnumOption update_extensible_enum_option_item(id, create_extensible_enum_option_item_request)

Update a record of the ExtensibleEnumOption

Update a record of the ExtensibleEnumOption

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.create_extensible_enum_option_item_request import CreateExtensibleEnumOptionItemRequest
from clientapi_atrocore.models.extensible_enum_option import ExtensibleEnumOption
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
    api_instance = clientapi_atrocore.ExtensibleEnumOptionApi(api_client)
    id = 'id_example' # str | 
    create_extensible_enum_option_item_request = clientapi_atrocore.CreateExtensibleEnumOptionItemRequest() # CreateExtensibleEnumOptionItemRequest | 

    try:
        # Update a record of the ExtensibleEnumOption
        api_response = api_instance.update_extensible_enum_option_item(id, create_extensible_enum_option_item_request)
        print("The response of ExtensibleEnumOptionApi->update_extensible_enum_option_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtensibleEnumOptionApi->update_extensible_enum_option_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_extensible_enum_option_item_request** | [**CreateExtensibleEnumOptionItemRequest**](CreateExtensibleEnumOptionItemRequest.md)|  | 

### Return type

[**ExtensibleEnumOption**](ExtensibleEnumOption.md)

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

