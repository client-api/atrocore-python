# clientapi_atrocore.ExportConfiguratorItemApi

All URIs are relative to *https://demo.atropim.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation_for_export_configurator_item**](ExportConfiguratorItemApi.md#add_relation_for_export_configurator_item) | **POST** /ExportConfiguratorItem/{link}/relation | Add relation for ExportConfiguratorItem
[**create_export_configurator_item_item**](ExportConfiguratorItemApi.md#create_export_configurator_item_item) | **POST** /ExportConfiguratorItem | Create a record of the ExportConfiguratorItem
[**delete_export_configurator_item_item**](ExportConfiguratorItemApi.md#delete_export_configurator_item_item) | **DELETE** /ExportConfiguratorItem/{id} | Delete a record of the ExportConfiguratorItem
[**follow_export_configurator_item**](ExportConfiguratorItemApi.md#follow_export_configurator_item) | **PUT** /ExportConfiguratorItem/{id}/subscription | Follow the ExportConfiguratorItem stream
[**get_export_configurator_item_item**](ExportConfiguratorItemApi.md#get_export_configurator_item_item) | **GET** /ExportConfiguratorItem/{id} | Returns a record of the ExportConfiguratorItem
[**get_linked_items_for_export_configurator_item_item**](ExportConfiguratorItemApi.md#get_linked_items_for_export_configurator_item_item) | **GET** /ExportConfiguratorItem/{id}/{link} | Returns linked entities for the ExportConfiguratorItem
[**get_list_of_export_configurator_item_items**](ExportConfiguratorItemApi.md#get_list_of_export_configurator_item_items) | **GET** /ExportConfiguratorItem | Returns a collection of ExportConfiguratorItem records
[**link_export_configurator_item**](ExportConfiguratorItemApi.md#link_export_configurator_item) | **POST** /ExportConfiguratorItem/{id}/{link} | Link ExportConfiguratorItem to Entities
[**mass_delete_export_configurator_item**](ExportConfiguratorItemApi.md#mass_delete_export_configurator_item) | **POST** /ExportConfiguratorItem/action/massDelete | Mass delete of ExportConfiguratorItem data
[**mass_update_export_configurator_item**](ExportConfiguratorItemApi.md#mass_update_export_configurator_item) | **PUT** /ExportConfiguratorItem/action/massUpdate | Mass update of ExportConfiguratorItem data
[**remove_relation_for_export_configurator_item**](ExportConfiguratorItemApi.md#remove_relation_for_export_configurator_item) | **DELETE** /ExportConfiguratorItem/{link}/relation | Remove relation for ExportConfiguratorItem
[**unfollow_export_configurator_item**](ExportConfiguratorItemApi.md#unfollow_export_configurator_item) | **DELETE** /ExportConfiguratorItem/{id}/subscription | Unfollow the ExportConfiguratorItem stream
[**unlink_export_configurator_item**](ExportConfiguratorItemApi.md#unlink_export_configurator_item) | **DELETE** /ExportConfiguratorItem/{id}/{link} | Unlink ExportConfiguratorItem from Entities
[**update_export_configurator_item_item**](ExportConfiguratorItemApi.md#update_export_configurator_item_item) | **PUT** /ExportConfiguratorItem/{id} | Update a record of the ExportConfiguratorItem


# **add_relation_for_export_configurator_item**
> bool add_relation_for_export_configurator_item(link, ids, foreign_ids)

Add relation for ExportConfiguratorItem

Add relation for ExportConfiguratorItem

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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Add relation for ExportConfiguratorItem
        api_response = api_instance.add_relation_for_export_configurator_item(link, ids, foreign_ids)
        print("The response of ExportConfiguratorItemApi->add_relation_for_export_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->add_relation_for_export_configurator_item: %s\n" % e)
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

# **create_export_configurator_item_item**
> ExportConfiguratorItem create_export_configurator_item_item(create_export_configurator_item_item_request)

Create a record of the ExportConfiguratorItem

Create a record of the ExportConfiguratorItem

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.create_export_configurator_item_item_request import CreateExportConfiguratorItemItemRequest
from clientapi_atrocore.models.export_configurator_item import ExportConfiguratorItem
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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    create_export_configurator_item_item_request = clientapi_atrocore.CreateExportConfiguratorItemItemRequest() # CreateExportConfiguratorItemItemRequest | 

    try:
        # Create a record of the ExportConfiguratorItem
        api_response = api_instance.create_export_configurator_item_item(create_export_configurator_item_item_request)
        print("The response of ExportConfiguratorItemApi->create_export_configurator_item_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->create_export_configurator_item_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_export_configurator_item_item_request** | [**CreateExportConfiguratorItemItemRequest**](CreateExportConfiguratorItemItemRequest.md)|  | 

### Return type

[**ExportConfiguratorItem**](ExportConfiguratorItem.md)

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

# **delete_export_configurator_item_item**
> bool delete_export_configurator_item_item(id)

Delete a record of the ExportConfiguratorItem

Delete a record of the ExportConfiguratorItem

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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a record of the ExportConfiguratorItem
        api_response = api_instance.delete_export_configurator_item_item(id)
        print("The response of ExportConfiguratorItemApi->delete_export_configurator_item_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->delete_export_configurator_item_item: %s\n" % e)
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

# **follow_export_configurator_item**
> FollowAccount200Response follow_export_configurator_item(id)

Follow the ExportConfiguratorItem stream

Follow the ExportConfiguratorItem stream

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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 

    try:
        # Follow the ExportConfiguratorItem stream
        api_response = api_instance.follow_export_configurator_item(id)
        print("The response of ExportConfiguratorItemApi->follow_export_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->follow_export_configurator_item: %s\n" % e)
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

# **get_export_configurator_item_item**
> ExportConfiguratorItem get_export_configurator_item_item(id, language=language)

Returns a record of the ExportConfiguratorItem

Returns a record of the ExportConfiguratorItem

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.export_configurator_item import ExportConfiguratorItem
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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns a record of the ExportConfiguratorItem
        api_response = api_instance.get_export_configurator_item_item(id, language=language)
        print("The response of ExportConfiguratorItemApi->get_export_configurator_item_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->get_export_configurator_item_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 

### Return type

[**ExportConfiguratorItem**](ExportConfiguratorItem.md)

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

# **get_linked_items_for_export_configurator_item_item**
> GetLinkedItemsForAccountItem200Response get_linked_items_for_export_configurator_item_item(id, link, language=language)

Returns linked entities for the ExportConfiguratorItem

Returns linked entities for the ExportConfiguratorItem

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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns linked entities for the ExportConfiguratorItem
        api_response = api_instance.get_linked_items_for_export_configurator_item_item(id, link, language=language)
        print("The response of ExportConfiguratorItemApi->get_linked_items_for_export_configurator_item_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->get_linked_items_for_export_configurator_item_item: %s\n" % e)
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

# **get_list_of_export_configurator_item_items**
> GetListOfExportConfiguratorItemItems200Response get_list_of_export_configurator_item_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)

Returns a collection of ExportConfiguratorItem records

Returns a collection of ExportConfiguratorItem records

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.get_list_of_export_configurator_item_items200_response import GetListOfExportConfiguratorItemItems200Response
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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)
    select = 'name,createdAt' # str | Available fields: attribute, attributeCode, attributeId, attributeName, attributeNameValue, attributeType, attributeValue, channel, channelId, channelName, column, columnType, createdAt, deleted, editable, entity, exportBy, exportFeed, exportFeedId, exportFeedLanguage, exportFeedName, exportIntoSeparateColumns, fileNameTemplate, filterCreateImportJob, filterField, filterFieldValue, filterUpdateImportJob, fixedValue, id, isAttributeMultiLang, language, limitRelation, mask, name, offsetRelation, previousItem, remove, scope, sortFieldRelation, sortOrder, sortOrderRelation, type, valueModifier, virtualFields, zip (optional)
    where = None # List[object] | There are a lot of filter types supported. You can learn all of them if you trace what's requested by Atro UI in the network tab in your browser console (press F12 key to open the console). (optional)
    offset = 0 # int |  (optional)
    max_size = 50 # int |  (optional)
    sort_by = 'name' # str |  (optional)
    asc = true # bool |  (optional)

    try:
        # Returns a collection of ExportConfiguratorItem records
        api_response = api_instance.get_list_of_export_configurator_item_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)
        print("The response of ExportConfiguratorItemApi->get_list_of_export_configurator_item_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->get_list_of_export_configurator_item_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 
 **select** | **str**| Available fields: attribute, attributeCode, attributeId, attributeName, attributeNameValue, attributeType, attributeValue, channel, channelId, channelName, column, columnType, createdAt, deleted, editable, entity, exportBy, exportFeed, exportFeedId, exportFeedLanguage, exportFeedName, exportIntoSeparateColumns, fileNameTemplate, filterCreateImportJob, filterField, filterFieldValue, filterUpdateImportJob, fixedValue, id, isAttributeMultiLang, language, limitRelation, mask, name, offsetRelation, previousItem, remove, scope, sortFieldRelation, sortOrder, sortOrderRelation, type, valueModifier, virtualFields, zip | [optional] 
 **where** | [**List[object]**](object.md)| There are a lot of filter types supported. You can learn all of them if you trace what&#39;s requested by Atro UI in the network tab in your browser console (press F12 key to open the console). | [optional] 
 **offset** | **int**|  | [optional] 
 **max_size** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **asc** | **bool**|  | [optional] 

### Return type

[**GetListOfExportConfiguratorItemItems200Response**](GetListOfExportConfiguratorItemItems200Response.md)

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

# **link_export_configurator_item**
> bool link_export_configurator_item(id, link, link_account_request)

Link ExportConfiguratorItem to Entities

Link ExportConfiguratorItem to Entities

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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Link ExportConfiguratorItem to Entities
        api_response = api_instance.link_export_configurator_item(id, link, link_account_request)
        print("The response of ExportConfiguratorItemApi->link_export_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->link_export_configurator_item: %s\n" % e)
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

# **mass_delete_export_configurator_item**
> bool mass_delete_export_configurator_item(link_account_request)

Mass delete of ExportConfiguratorItem data

Mass delete of ExportConfiguratorItem data

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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Mass delete of ExportConfiguratorItem data
        api_response = api_instance.mass_delete_export_configurator_item(link_account_request)
        print("The response of ExportConfiguratorItemApi->mass_delete_export_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->mass_delete_export_configurator_item: %s\n" % e)
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

# **mass_update_export_configurator_item**
> bool mass_update_export_configurator_item(mass_update_account_request)

Mass update of ExportConfiguratorItem data

Mass update of ExportConfiguratorItem data

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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    mass_update_account_request = clientapi_atrocore.MassUpdateAccountRequest() # MassUpdateAccountRequest | 

    try:
        # Mass update of ExportConfiguratorItem data
        api_response = api_instance.mass_update_export_configurator_item(mass_update_account_request)
        print("The response of ExportConfiguratorItemApi->mass_update_export_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->mass_update_export_configurator_item: %s\n" % e)
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

# **remove_relation_for_export_configurator_item**
> bool remove_relation_for_export_configurator_item(link, ids, foreign_ids)

Remove relation for ExportConfiguratorItem

Remove relation for ExportConfiguratorItem

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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Remove relation for ExportConfiguratorItem
        api_response = api_instance.remove_relation_for_export_configurator_item(link, ids, foreign_ids)
        print("The response of ExportConfiguratorItemApi->remove_relation_for_export_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->remove_relation_for_export_configurator_item: %s\n" % e)
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

# **unfollow_export_configurator_item**
> bool unfollow_export_configurator_item(id)

Unfollow the ExportConfiguratorItem stream

Unfollow the ExportConfiguratorItem stream

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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unfollow the ExportConfiguratorItem stream
        api_response = api_instance.unfollow_export_configurator_item(id)
        print("The response of ExportConfiguratorItemApi->unfollow_export_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->unfollow_export_configurator_item: %s\n" % e)
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

# **unlink_export_configurator_item**
> bool unlink_export_configurator_item(id, link, ids)

Unlink ExportConfiguratorItem from Entities

Unlink ExportConfiguratorItem from Entities

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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 

    try:
        # Unlink ExportConfiguratorItem from Entities
        api_response = api_instance.unlink_export_configurator_item(id, link, ids)
        print("The response of ExportConfiguratorItemApi->unlink_export_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->unlink_export_configurator_item: %s\n" % e)
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

# **update_export_configurator_item_item**
> ExportConfiguratorItem update_export_configurator_item_item(id, create_export_configurator_item_item_request)

Update a record of the ExportConfiguratorItem

Update a record of the ExportConfiguratorItem

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.create_export_configurator_item_item_request import CreateExportConfiguratorItemItemRequest
from clientapi_atrocore.models.export_configurator_item import ExportConfiguratorItem
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
    api_instance = clientapi_atrocore.ExportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 
    create_export_configurator_item_item_request = clientapi_atrocore.CreateExportConfiguratorItemItemRequest() # CreateExportConfiguratorItemItemRequest | 

    try:
        # Update a record of the ExportConfiguratorItem
        api_response = api_instance.update_export_configurator_item_item(id, create_export_configurator_item_item_request)
        print("The response of ExportConfiguratorItemApi->update_export_configurator_item_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportConfiguratorItemApi->update_export_configurator_item_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_export_configurator_item_item_request** | [**CreateExportConfiguratorItemItemRequest**](CreateExportConfiguratorItemItemRequest.md)|  | 

### Return type

[**ExportConfiguratorItem**](ExportConfiguratorItem.md)

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

