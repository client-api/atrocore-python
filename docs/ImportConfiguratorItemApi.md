# clientapi_atrocore.ImportConfiguratorItemApi

All URIs are relative to *https://demo.atropim.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation_for_import_configurator_item**](ImportConfiguratorItemApi.md#add_relation_for_import_configurator_item) | **POST** /ImportConfiguratorItem/{link}/relation | Add relation for ImportConfiguratorItem
[**create_import_configurator_item_item**](ImportConfiguratorItemApi.md#create_import_configurator_item_item) | **POST** /ImportConfiguratorItem | Create a record of the ImportConfiguratorItem
[**delete_import_configurator_item_item**](ImportConfiguratorItemApi.md#delete_import_configurator_item_item) | **DELETE** /ImportConfiguratorItem/{id} | Delete a record of the ImportConfiguratorItem
[**follow_import_configurator_item**](ImportConfiguratorItemApi.md#follow_import_configurator_item) | **PUT** /ImportConfiguratorItem/{id}/subscription | Follow the ImportConfiguratorItem stream
[**get_import_configurator_item_item**](ImportConfiguratorItemApi.md#get_import_configurator_item_item) | **GET** /ImportConfiguratorItem/{id} | Returns a record of the ImportConfiguratorItem
[**get_linked_items_for_import_configurator_item_item**](ImportConfiguratorItemApi.md#get_linked_items_for_import_configurator_item_item) | **GET** /ImportConfiguratorItem/{id}/{link} | Returns linked entities for the ImportConfiguratorItem
[**get_list_of_import_configurator_item_items**](ImportConfiguratorItemApi.md#get_list_of_import_configurator_item_items) | **GET** /ImportConfiguratorItem | Returns a collection of ImportConfiguratorItem records
[**link_import_configurator_item**](ImportConfiguratorItemApi.md#link_import_configurator_item) | **POST** /ImportConfiguratorItem/{id}/{link} | Link ImportConfiguratorItem to Entities
[**mass_delete_import_configurator_item**](ImportConfiguratorItemApi.md#mass_delete_import_configurator_item) | **POST** /ImportConfiguratorItem/action/massDelete | Mass delete of ImportConfiguratorItem data
[**mass_update_import_configurator_item**](ImportConfiguratorItemApi.md#mass_update_import_configurator_item) | **PUT** /ImportConfiguratorItem/action/massUpdate | Mass update of ImportConfiguratorItem data
[**remove_relation_for_import_configurator_item**](ImportConfiguratorItemApi.md#remove_relation_for_import_configurator_item) | **DELETE** /ImportConfiguratorItem/{link}/relation | Remove relation for ImportConfiguratorItem
[**unfollow_import_configurator_item**](ImportConfiguratorItemApi.md#unfollow_import_configurator_item) | **DELETE** /ImportConfiguratorItem/{id}/subscription | Unfollow the ImportConfiguratorItem stream
[**unlink_import_configurator_item**](ImportConfiguratorItemApi.md#unlink_import_configurator_item) | **DELETE** /ImportConfiguratorItem/{id}/{link} | Unlink ImportConfiguratorItem from Entities
[**update_import_configurator_item_item**](ImportConfiguratorItemApi.md#update_import_configurator_item_item) | **PUT** /ImportConfiguratorItem/{id} | Update a record of the ImportConfiguratorItem


# **add_relation_for_import_configurator_item**
> bool add_relation_for_import_configurator_item(link, ids, foreign_ids)

Add relation for ImportConfiguratorItem

Add relation for ImportConfiguratorItem

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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Add relation for ImportConfiguratorItem
        api_response = api_instance.add_relation_for_import_configurator_item(link, ids, foreign_ids)
        print("The response of ImportConfiguratorItemApi->add_relation_for_import_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->add_relation_for_import_configurator_item: %s\n" % e)
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

# **create_import_configurator_item_item**
> ImportConfiguratorItem create_import_configurator_item_item(create_import_configurator_item_item_request)

Create a record of the ImportConfiguratorItem

Create a record of the ImportConfiguratorItem

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.create_import_configurator_item_item_request import CreateImportConfiguratorItemItemRequest
from clientapi_atrocore.models.import_configurator_item import ImportConfiguratorItem
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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    create_import_configurator_item_item_request = clientapi_atrocore.CreateImportConfiguratorItemItemRequest() # CreateImportConfiguratorItemItemRequest | 

    try:
        # Create a record of the ImportConfiguratorItem
        api_response = api_instance.create_import_configurator_item_item(create_import_configurator_item_item_request)
        print("The response of ImportConfiguratorItemApi->create_import_configurator_item_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->create_import_configurator_item_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_import_configurator_item_item_request** | [**CreateImportConfiguratorItemItemRequest**](CreateImportConfiguratorItemItemRequest.md)|  | 

### Return type

[**ImportConfiguratorItem**](ImportConfiguratorItem.md)

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

# **delete_import_configurator_item_item**
> bool delete_import_configurator_item_item(id)

Delete a record of the ImportConfiguratorItem

Delete a record of the ImportConfiguratorItem

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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a record of the ImportConfiguratorItem
        api_response = api_instance.delete_import_configurator_item_item(id)
        print("The response of ImportConfiguratorItemApi->delete_import_configurator_item_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->delete_import_configurator_item_item: %s\n" % e)
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

# **follow_import_configurator_item**
> FollowAccount200Response follow_import_configurator_item(id)

Follow the ImportConfiguratorItem stream

Follow the ImportConfiguratorItem stream

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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 

    try:
        # Follow the ImportConfiguratorItem stream
        api_response = api_instance.follow_import_configurator_item(id)
        print("The response of ImportConfiguratorItemApi->follow_import_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->follow_import_configurator_item: %s\n" % e)
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

# **get_import_configurator_item_item**
> ImportConfiguratorItem get_import_configurator_item_item(id, language=language)

Returns a record of the ImportConfiguratorItem

Returns a record of the ImportConfiguratorItem

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.import_configurator_item import ImportConfiguratorItem
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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns a record of the ImportConfiguratorItem
        api_response = api_instance.get_import_configurator_item_item(id, language=language)
        print("The response of ImportConfiguratorItemApi->get_import_configurator_item_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->get_import_configurator_item_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 

### Return type

[**ImportConfiguratorItem**](ImportConfiguratorItem.md)

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

# **get_linked_items_for_import_configurator_item_item**
> GetLinkedItemsForAccountItem200Response get_linked_items_for_import_configurator_item_item(id, link, language=language)

Returns linked entities for the ImportConfiguratorItem

Returns linked entities for the ImportConfiguratorItem

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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns linked entities for the ImportConfiguratorItem
        api_response = api_instance.get_linked_items_for_import_configurator_item_item(id, link, language=language)
        print("The response of ImportConfiguratorItemApi->get_linked_items_for_import_configurator_item_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->get_linked_items_for_import_configurator_item_item: %s\n" % e)
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

# **get_list_of_import_configurator_item_items**
> GetListOfImportConfiguratorItemItems200Response get_list_of_import_configurator_item_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)

Returns a collection of ImportConfiguratorItem records

Returns a collection of ImportConfiguratorItem records

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.get_list_of_import_configurator_item_items200_response import GetListOfImportConfiguratorItemItems200Response
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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)
    select = 'name,createdAt' # str | Available fields: attribute, attributeData, attributeId, attributeName, attributeValue, channel, channelId, channelName, column, createIfNotExist, createdAt, default, defaultContainer, defaultCurrency, defaultFrom, defaultId, defaultIds, defaultName, defaultNames, defaultPathsData, defaultTo, deleted, entity, entityIdentifier, filterCreateImportJob, filterUpdateImportJob, foreignColumn, foreignImportBy, id, importBy, importFeed, importFeedId, importFeedName, locale, name, replaceArray, scope, sortOrder, sourceFields, type (optional)
    where = None # List[object] | There are a lot of filter types supported. You can learn all of them if you trace what's requested by Atro UI in the network tab in your browser console (press F12 key to open the console). (optional)
    offset = 0 # int |  (optional)
    max_size = 50 # int |  (optional)
    sort_by = 'name' # str |  (optional)
    asc = true # bool |  (optional)

    try:
        # Returns a collection of ImportConfiguratorItem records
        api_response = api_instance.get_list_of_import_configurator_item_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)
        print("The response of ImportConfiguratorItemApi->get_list_of_import_configurator_item_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->get_list_of_import_configurator_item_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 
 **select** | **str**| Available fields: attribute, attributeData, attributeId, attributeName, attributeValue, channel, channelId, channelName, column, createIfNotExist, createdAt, default, defaultContainer, defaultCurrency, defaultFrom, defaultId, defaultIds, defaultName, defaultNames, defaultPathsData, defaultTo, deleted, entity, entityIdentifier, filterCreateImportJob, filterUpdateImportJob, foreignColumn, foreignImportBy, id, importBy, importFeed, importFeedId, importFeedName, locale, name, replaceArray, scope, sortOrder, sourceFields, type | [optional] 
 **where** | [**List[object]**](object.md)| There are a lot of filter types supported. You can learn all of them if you trace what&#39;s requested by Atro UI in the network tab in your browser console (press F12 key to open the console). | [optional] 
 **offset** | **int**|  | [optional] 
 **max_size** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **asc** | **bool**|  | [optional] 

### Return type

[**GetListOfImportConfiguratorItemItems200Response**](GetListOfImportConfiguratorItemItems200Response.md)

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

# **link_import_configurator_item**
> bool link_import_configurator_item(id, link, link_account_request)

Link ImportConfiguratorItem to Entities

Link ImportConfiguratorItem to Entities

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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Link ImportConfiguratorItem to Entities
        api_response = api_instance.link_import_configurator_item(id, link, link_account_request)
        print("The response of ImportConfiguratorItemApi->link_import_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->link_import_configurator_item: %s\n" % e)
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

# **mass_delete_import_configurator_item**
> bool mass_delete_import_configurator_item(link_account_request)

Mass delete of ImportConfiguratorItem data

Mass delete of ImportConfiguratorItem data

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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Mass delete of ImportConfiguratorItem data
        api_response = api_instance.mass_delete_import_configurator_item(link_account_request)
        print("The response of ImportConfiguratorItemApi->mass_delete_import_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->mass_delete_import_configurator_item: %s\n" % e)
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

# **mass_update_import_configurator_item**
> bool mass_update_import_configurator_item(mass_update_account_request)

Mass update of ImportConfiguratorItem data

Mass update of ImportConfiguratorItem data

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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    mass_update_account_request = clientapi_atrocore.MassUpdateAccountRequest() # MassUpdateAccountRequest | 

    try:
        # Mass update of ImportConfiguratorItem data
        api_response = api_instance.mass_update_import_configurator_item(mass_update_account_request)
        print("The response of ImportConfiguratorItemApi->mass_update_import_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->mass_update_import_configurator_item: %s\n" % e)
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

# **remove_relation_for_import_configurator_item**
> bool remove_relation_for_import_configurator_item(link, ids, foreign_ids)

Remove relation for ImportConfiguratorItem

Remove relation for ImportConfiguratorItem

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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Remove relation for ImportConfiguratorItem
        api_response = api_instance.remove_relation_for_import_configurator_item(link, ids, foreign_ids)
        print("The response of ImportConfiguratorItemApi->remove_relation_for_import_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->remove_relation_for_import_configurator_item: %s\n" % e)
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

# **unfollow_import_configurator_item**
> bool unfollow_import_configurator_item(id)

Unfollow the ImportConfiguratorItem stream

Unfollow the ImportConfiguratorItem stream

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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unfollow the ImportConfiguratorItem stream
        api_response = api_instance.unfollow_import_configurator_item(id)
        print("The response of ImportConfiguratorItemApi->unfollow_import_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->unfollow_import_configurator_item: %s\n" % e)
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

# **unlink_import_configurator_item**
> bool unlink_import_configurator_item(id, link, ids)

Unlink ImportConfiguratorItem from Entities

Unlink ImportConfiguratorItem from Entities

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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 

    try:
        # Unlink ImportConfiguratorItem from Entities
        api_response = api_instance.unlink_import_configurator_item(id, link, ids)
        print("The response of ImportConfiguratorItemApi->unlink_import_configurator_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->unlink_import_configurator_item: %s\n" % e)
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

# **update_import_configurator_item_item**
> ImportConfiguratorItem update_import_configurator_item_item(id, create_import_configurator_item_item_request)

Update a record of the ImportConfiguratorItem

Update a record of the ImportConfiguratorItem

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.create_import_configurator_item_item_request import CreateImportConfiguratorItemItemRequest
from clientapi_atrocore.models.import_configurator_item import ImportConfiguratorItem
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
    api_instance = clientapi_atrocore.ImportConfiguratorItemApi(api_client)
    id = 'id_example' # str | 
    create_import_configurator_item_item_request = clientapi_atrocore.CreateImportConfiguratorItemItemRequest() # CreateImportConfiguratorItemItemRequest | 

    try:
        # Update a record of the ImportConfiguratorItem
        api_response = api_instance.update_import_configurator_item_item(id, create_import_configurator_item_item_request)
        print("The response of ImportConfiguratorItemApi->update_import_configurator_item_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportConfiguratorItemApi->update_import_configurator_item_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_import_configurator_item_item_request** | [**CreateImportConfiguratorItemItemRequest**](CreateImportConfiguratorItemItemRequest.md)|  | 

### Return type

[**ImportConfiguratorItem**](ImportConfiguratorItem.md)

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

