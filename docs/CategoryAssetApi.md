# clientapi_atrocore.CategoryAssetApi

All URIs are relative to *https://demo.atropim.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation_for_category_asset**](CategoryAssetApi.md#add_relation_for_category_asset) | **POST** /CategoryAsset/{link}/relation | Add relation for CategoryAsset
[**create_category_asset_item**](CategoryAssetApi.md#create_category_asset_item) | **POST** /CategoryAsset | Create a record of the CategoryAsset
[**delete_category_asset_item**](CategoryAssetApi.md#delete_category_asset_item) | **DELETE** /CategoryAsset/{id} | Delete a record of the CategoryAsset
[**follow_category_asset**](CategoryAssetApi.md#follow_category_asset) | **PUT** /CategoryAsset/{id}/subscription | Follow the CategoryAsset stream
[**get_category_asset_item**](CategoryAssetApi.md#get_category_asset_item) | **GET** /CategoryAsset/{id} | Returns a record of the CategoryAsset
[**get_linked_items_for_category_asset_item**](CategoryAssetApi.md#get_linked_items_for_category_asset_item) | **GET** /CategoryAsset/{id}/{link} | Returns linked entities for the CategoryAsset
[**get_list_of_category_asset_items**](CategoryAssetApi.md#get_list_of_category_asset_items) | **GET** /CategoryAsset | Returns a collection of CategoryAsset records
[**link_category_asset**](CategoryAssetApi.md#link_category_asset) | **POST** /CategoryAsset/{id}/{link} | Link CategoryAsset to Entities
[**mass_delete_category_asset**](CategoryAssetApi.md#mass_delete_category_asset) | **POST** /CategoryAsset/action/massDelete | Mass delete of CategoryAsset data
[**mass_update_category_asset**](CategoryAssetApi.md#mass_update_category_asset) | **PUT** /CategoryAsset/action/massUpdate | Mass update of CategoryAsset data
[**remove_relation_for_category_asset**](CategoryAssetApi.md#remove_relation_for_category_asset) | **DELETE** /CategoryAsset/{link}/relation | Remove relation for CategoryAsset
[**unfollow_category_asset**](CategoryAssetApi.md#unfollow_category_asset) | **DELETE** /CategoryAsset/{id}/subscription | Unfollow the CategoryAsset stream
[**unlink_category_asset**](CategoryAssetApi.md#unlink_category_asset) | **DELETE** /CategoryAsset/{id}/{link} | Unlink CategoryAsset from Entities
[**update_category_asset_item**](CategoryAssetApi.md#update_category_asset_item) | **PUT** /CategoryAsset/{id} | Update a record of the CategoryAsset


# **add_relation_for_category_asset**
> bool add_relation_for_category_asset(link, ids, foreign_ids)

Add relation for CategoryAsset

Add relation for CategoryAsset

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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Add relation for CategoryAsset
        api_response = api_instance.add_relation_for_category_asset(link, ids, foreign_ids)
        print("The response of CategoryAssetApi->add_relation_for_category_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->add_relation_for_category_asset: %s\n" % e)
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

# **create_category_asset_item**
> CategoryAsset create_category_asset_item(create_category_asset_item_request)

Create a record of the CategoryAsset

Create a record of the CategoryAsset

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.category_asset import CategoryAsset
from clientapi_atrocore.models.create_category_asset_item_request import CreateCategoryAssetItemRequest
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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    create_category_asset_item_request = clientapi_atrocore.CreateCategoryAssetItemRequest() # CreateCategoryAssetItemRequest | 

    try:
        # Create a record of the CategoryAsset
        api_response = api_instance.create_category_asset_item(create_category_asset_item_request)
        print("The response of CategoryAssetApi->create_category_asset_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->create_category_asset_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_category_asset_item_request** | [**CreateCategoryAssetItemRequest**](CreateCategoryAssetItemRequest.md)|  | 

### Return type

[**CategoryAsset**](CategoryAsset.md)

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

# **delete_category_asset_item**
> bool delete_category_asset_item(id)

Delete a record of the CategoryAsset

Delete a record of the CategoryAsset

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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a record of the CategoryAsset
        api_response = api_instance.delete_category_asset_item(id)
        print("The response of CategoryAssetApi->delete_category_asset_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->delete_category_asset_item: %s\n" % e)
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

# **follow_category_asset**
> FollowAccount200Response follow_category_asset(id)

Follow the CategoryAsset stream

Follow the CategoryAsset stream

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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    id = 'id_example' # str | 

    try:
        # Follow the CategoryAsset stream
        api_response = api_instance.follow_category_asset(id)
        print("The response of CategoryAssetApi->follow_category_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->follow_category_asset: %s\n" % e)
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

# **get_category_asset_item**
> CategoryAsset get_category_asset_item(id, language=language)

Returns a record of the CategoryAsset

Returns a record of the CategoryAsset

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.category_asset import CategoryAsset
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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    id = 'id_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns a record of the CategoryAsset
        api_response = api_instance.get_category_asset_item(id, language=language)
        print("The response of CategoryAssetApi->get_category_asset_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->get_category_asset_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 

### Return type

[**CategoryAsset**](CategoryAsset.md)

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

# **get_linked_items_for_category_asset_item**
> GetLinkedItemsForAccountItem200Response get_linked_items_for_category_asset_item(id, link, language=language)

Returns linked entities for the CategoryAsset

Returns linked entities for the CategoryAsset

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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns linked entities for the CategoryAsset
        api_response = api_instance.get_linked_items_for_category_asset_item(id, link, language=language)
        print("The response of CategoryAssetApi->get_linked_items_for_category_asset_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->get_linked_items_for_category_asset_item: %s\n" % e)
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

# **get_list_of_category_asset_items**
> GetListOfCategoryAssetItems200Response get_list_of_category_asset_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)

Returns a collection of CategoryAsset records

Returns a collection of CategoryAsset records

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.get_list_of_category_asset_items200_response import GetListOfCategoryAssetItems200Response
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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)
    select = 'name,createdAt' # str | Available fields: asset, assetId, assetName, asset_afterSaveMessage, asset_colorDepth, asset_colorSpace, asset_createdAt, asset_createdBy, asset_createdById, asset_createdByName, asset_description, asset_descriptionDeDe, asset_fileId, asset_fileName, asset_filePathsData, asset_filterCreateImportJob, asset_filterUpdateImportJob, asset_hasChildren, asset_height, asset_hierarchyRoute, asset_hierarchySortOrder, asset_icon, asset_inheritedFields, asset_isActive, asset_isRoot, asset_library, asset_libraryId, asset_libraryName, asset_modifiedAt, asset_modifiedBy, asset_modifiedById, asset_modifiedByName, asset_name, asset_orientation, asset_preview, asset_private, asset_size, asset_sortOrder, asset_tags, asset_type, asset_url, asset_width, category, categoryId, categoryName, category__position, category__target, category_assignedUser, category_assignedUserId, category_assignedUserName, category_categoryParent, category_categoryParentId, category_categoryParentName, category_categoryRoute, category_categoryRouteName, category_childrenCount, category_code, category_createdAt, category_createdBy, category_createdById, category_createdByName, category_description, category_descriptionDeDe, category_filterCreateImportJob, category_filterUpdateImportJob, category_hasChildren, category_isActive, category_mainImageId, category_mainImageName, category_mainImagePathsData, category_modifiedAt, category_modifiedBy, category_modifiedById, category_modifiedByName, category_name, category_nameDeDe, category_ownerUser, category_ownerUserId, category_ownerUserName, category_sortOrder, category_sorting, createdAt, createdBy, createdById, createdByName, deleted, fileId, fileName, filePathsData, filterCreateImportJob, filterUpdateImportJob, icon, id, isInherited, isMainImage, modifiedAt, modifiedBy, modifiedById, modifiedByName, name, preview, sorting, tags (optional)
    where = None # List[object] | There are a lot of filter types supported. You can learn all of them if you trace what's requested by Atro UI in the network tab in your browser console (press F12 key to open the console). (optional)
    offset = 0 # int |  (optional)
    max_size = 50 # int |  (optional)
    sort_by = 'name' # str |  (optional)
    asc = true # bool |  (optional)

    try:
        # Returns a collection of CategoryAsset records
        api_response = api_instance.get_list_of_category_asset_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)
        print("The response of CategoryAssetApi->get_list_of_category_asset_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->get_list_of_category_asset_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 
 **select** | **str**| Available fields: asset, assetId, assetName, asset_afterSaveMessage, asset_colorDepth, asset_colorSpace, asset_createdAt, asset_createdBy, asset_createdById, asset_createdByName, asset_description, asset_descriptionDeDe, asset_fileId, asset_fileName, asset_filePathsData, asset_filterCreateImportJob, asset_filterUpdateImportJob, asset_hasChildren, asset_height, asset_hierarchyRoute, asset_hierarchySortOrder, asset_icon, asset_inheritedFields, asset_isActive, asset_isRoot, asset_library, asset_libraryId, asset_libraryName, asset_modifiedAt, asset_modifiedBy, asset_modifiedById, asset_modifiedByName, asset_name, asset_orientation, asset_preview, asset_private, asset_size, asset_sortOrder, asset_tags, asset_type, asset_url, asset_width, category, categoryId, categoryName, category__position, category__target, category_assignedUser, category_assignedUserId, category_assignedUserName, category_categoryParent, category_categoryParentId, category_categoryParentName, category_categoryRoute, category_categoryRouteName, category_childrenCount, category_code, category_createdAt, category_createdBy, category_createdById, category_createdByName, category_description, category_descriptionDeDe, category_filterCreateImportJob, category_filterUpdateImportJob, category_hasChildren, category_isActive, category_mainImageId, category_mainImageName, category_mainImagePathsData, category_modifiedAt, category_modifiedBy, category_modifiedById, category_modifiedByName, category_name, category_nameDeDe, category_ownerUser, category_ownerUserId, category_ownerUserName, category_sortOrder, category_sorting, createdAt, createdBy, createdById, createdByName, deleted, fileId, fileName, filePathsData, filterCreateImportJob, filterUpdateImportJob, icon, id, isInherited, isMainImage, modifiedAt, modifiedBy, modifiedById, modifiedByName, name, preview, sorting, tags | [optional] 
 **where** | [**List[object]**](object.md)| There are a lot of filter types supported. You can learn all of them if you trace what&#39;s requested by Atro UI in the network tab in your browser console (press F12 key to open the console). | [optional] 
 **offset** | **int**|  | [optional] 
 **max_size** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **asc** | **bool**|  | [optional] 

### Return type

[**GetListOfCategoryAssetItems200Response**](GetListOfCategoryAssetItems200Response.md)

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

# **link_category_asset**
> bool link_category_asset(id, link, link_account_request)

Link CategoryAsset to Entities

Link CategoryAsset to Entities

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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Link CategoryAsset to Entities
        api_response = api_instance.link_category_asset(id, link, link_account_request)
        print("The response of CategoryAssetApi->link_category_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->link_category_asset: %s\n" % e)
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

# **mass_delete_category_asset**
> bool mass_delete_category_asset(link_account_request)

Mass delete of CategoryAsset data

Mass delete of CategoryAsset data

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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Mass delete of CategoryAsset data
        api_response = api_instance.mass_delete_category_asset(link_account_request)
        print("The response of CategoryAssetApi->mass_delete_category_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->mass_delete_category_asset: %s\n" % e)
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

# **mass_update_category_asset**
> bool mass_update_category_asset(mass_update_account_request)

Mass update of CategoryAsset data

Mass update of CategoryAsset data

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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    mass_update_account_request = clientapi_atrocore.MassUpdateAccountRequest() # MassUpdateAccountRequest | 

    try:
        # Mass update of CategoryAsset data
        api_response = api_instance.mass_update_category_asset(mass_update_account_request)
        print("The response of CategoryAssetApi->mass_update_category_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->mass_update_category_asset: %s\n" % e)
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

# **remove_relation_for_category_asset**
> bool remove_relation_for_category_asset(link, ids, foreign_ids)

Remove relation for CategoryAsset

Remove relation for CategoryAsset

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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Remove relation for CategoryAsset
        api_response = api_instance.remove_relation_for_category_asset(link, ids, foreign_ids)
        print("The response of CategoryAssetApi->remove_relation_for_category_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->remove_relation_for_category_asset: %s\n" % e)
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

# **unfollow_category_asset**
> bool unfollow_category_asset(id)

Unfollow the CategoryAsset stream

Unfollow the CategoryAsset stream

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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unfollow the CategoryAsset stream
        api_response = api_instance.unfollow_category_asset(id)
        print("The response of CategoryAssetApi->unfollow_category_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->unfollow_category_asset: %s\n" % e)
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

# **unlink_category_asset**
> bool unlink_category_asset(id, link, ids)

Unlink CategoryAsset from Entities

Unlink CategoryAsset from Entities

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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 

    try:
        # Unlink CategoryAsset from Entities
        api_response = api_instance.unlink_category_asset(id, link, ids)
        print("The response of CategoryAssetApi->unlink_category_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->unlink_category_asset: %s\n" % e)
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

# **update_category_asset_item**
> CategoryAsset update_category_asset_item(id, create_category_asset_item_request)

Update a record of the CategoryAsset

Update a record of the CategoryAsset

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.category_asset import CategoryAsset
from clientapi_atrocore.models.create_category_asset_item_request import CreateCategoryAssetItemRequest
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
    api_instance = clientapi_atrocore.CategoryAssetApi(api_client)
    id = 'id_example' # str | 
    create_category_asset_item_request = clientapi_atrocore.CreateCategoryAssetItemRequest() # CreateCategoryAssetItemRequest | 

    try:
        # Update a record of the CategoryAsset
        api_response = api_instance.update_category_asset_item(id, create_category_asset_item_request)
        print("The response of CategoryAssetApi->update_category_asset_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CategoryAssetApi->update_category_asset_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_category_asset_item_request** | [**CreateCategoryAssetItemRequest**](CreateCategoryAssetItemRequest.md)|  | 

### Return type

[**CategoryAsset**](CategoryAsset.md)

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

