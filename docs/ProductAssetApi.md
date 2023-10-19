# clientapi_atrocore.ProductAssetApi

All URIs are relative to *https://demo.atropim.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation_for_product_asset**](ProductAssetApi.md#add_relation_for_product_asset) | **POST** /ProductAsset/{link}/relation | Add relation for ProductAsset
[**create_product_asset_item**](ProductAssetApi.md#create_product_asset_item) | **POST** /ProductAsset | Create a record of the ProductAsset
[**delete_product_asset_item**](ProductAssetApi.md#delete_product_asset_item) | **DELETE** /ProductAsset/{id} | Delete a record of the ProductAsset
[**follow_product_asset**](ProductAssetApi.md#follow_product_asset) | **PUT** /ProductAsset/{id}/subscription | Follow the ProductAsset stream
[**get_linked_items_for_product_asset_item**](ProductAssetApi.md#get_linked_items_for_product_asset_item) | **GET** /ProductAsset/{id}/{link} | Returns linked entities for the ProductAsset
[**get_list_of_product_asset_items**](ProductAssetApi.md#get_list_of_product_asset_items) | **GET** /ProductAsset | Returns a collection of ProductAsset records
[**get_product_asset_item**](ProductAssetApi.md#get_product_asset_item) | **GET** /ProductAsset/{id} | Returns a record of the ProductAsset
[**link_product_asset**](ProductAssetApi.md#link_product_asset) | **POST** /ProductAsset/{id}/{link} | Link ProductAsset to Entities
[**mass_delete_product_asset**](ProductAssetApi.md#mass_delete_product_asset) | **POST** /ProductAsset/action/massDelete | Mass delete of ProductAsset data
[**mass_update_product_asset**](ProductAssetApi.md#mass_update_product_asset) | **PUT** /ProductAsset/action/massUpdate | Mass update of ProductAsset data
[**remove_relation_for_product_asset**](ProductAssetApi.md#remove_relation_for_product_asset) | **DELETE** /ProductAsset/{link}/relation | Remove relation for ProductAsset
[**unfollow_product_asset**](ProductAssetApi.md#unfollow_product_asset) | **DELETE** /ProductAsset/{id}/subscription | Unfollow the ProductAsset stream
[**unlink_product_asset**](ProductAssetApi.md#unlink_product_asset) | **DELETE** /ProductAsset/{id}/{link} | Unlink ProductAsset from Entities
[**update_product_asset_item**](ProductAssetApi.md#update_product_asset_item) | **PUT** /ProductAsset/{id} | Update a record of the ProductAsset


# **add_relation_for_product_asset**
> bool add_relation_for_product_asset(link, ids, foreign_ids)

Add relation for ProductAsset

Add relation for ProductAsset

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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Add relation for ProductAsset
        api_response = api_instance.add_relation_for_product_asset(link, ids, foreign_ids)
        print("The response of ProductAssetApi->add_relation_for_product_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->add_relation_for_product_asset: %s\n" % e)
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

# **create_product_asset_item**
> ProductAsset create_product_asset_item(create_product_asset_item_request)

Create a record of the ProductAsset

Create a record of the ProductAsset

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.create_product_asset_item_request import CreateProductAssetItemRequest
from clientapi_atrocore.models.product_asset import ProductAsset
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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    create_product_asset_item_request = clientapi_atrocore.CreateProductAssetItemRequest() # CreateProductAssetItemRequest | 

    try:
        # Create a record of the ProductAsset
        api_response = api_instance.create_product_asset_item(create_product_asset_item_request)
        print("The response of ProductAssetApi->create_product_asset_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->create_product_asset_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_product_asset_item_request** | [**CreateProductAssetItemRequest**](CreateProductAssetItemRequest.md)|  | 

### Return type

[**ProductAsset**](ProductAsset.md)

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

# **delete_product_asset_item**
> bool delete_product_asset_item(id)

Delete a record of the ProductAsset

Delete a record of the ProductAsset

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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a record of the ProductAsset
        api_response = api_instance.delete_product_asset_item(id)
        print("The response of ProductAssetApi->delete_product_asset_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->delete_product_asset_item: %s\n" % e)
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

# **follow_product_asset**
> FollowAccount200Response follow_product_asset(id)

Follow the ProductAsset stream

Follow the ProductAsset stream

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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    id = 'id_example' # str | 

    try:
        # Follow the ProductAsset stream
        api_response = api_instance.follow_product_asset(id)
        print("The response of ProductAssetApi->follow_product_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->follow_product_asset: %s\n" % e)
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

# **get_linked_items_for_product_asset_item**
> GetLinkedItemsForAccountItem200Response get_linked_items_for_product_asset_item(id, link, language=language)

Returns linked entities for the ProductAsset

Returns linked entities for the ProductAsset

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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns linked entities for the ProductAsset
        api_response = api_instance.get_linked_items_for_product_asset_item(id, link, language=language)
        print("The response of ProductAssetApi->get_linked_items_for_product_asset_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->get_linked_items_for_product_asset_item: %s\n" % e)
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

# **get_list_of_product_asset_items**
> GetListOfProductAssetItems200Response get_list_of_product_asset_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)

Returns a collection of ProductAsset records

Returns a collection of ProductAsset records

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.get_list_of_product_asset_items200_response import GetListOfProductAssetItems200Response
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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)
    select = 'name,createdAt' # str | Available fields: asset, assetId, assetName, asset_afterSaveMessage, asset_colorDepth, asset_colorSpace, asset_createdAt, asset_createdBy, asset_createdById, asset_createdByName, asset_description, asset_descriptionDeDe, asset_fileId, asset_fileName, asset_filePathsData, asset_filterCreateImportJob, asset_filterUpdateImportJob, asset_hasChildren, asset_height, asset_hierarchyRoute, asset_hierarchySortOrder, asset_icon, asset_inheritedFields, asset_isActive, asset_isRoot, asset_library, asset_libraryId, asset_libraryName, asset_modifiedAt, asset_modifiedBy, asset_modifiedById, asset_modifiedByName, asset_name, asset_orientation, asset_preview, asset_private, asset_size, asset_sortOrder, asset_tags, asset_type, asset_url, asset_width, channel, channelId, channelName, createdAt, createdBy, createdById, createdByName, deleted, fileId, fileName, filePathsData, filterCreateImportJob, filterUpdateImportJob, icon, id, isInherited, isMainImage, modifiedAt, modifiedBy, modifiedById, modifiedByName, name, preview, product, productId, productName, product_amount, product_assignedUser, product_assignedUserId, product_assignedUserName, product_brand, product_brandId, product_brandName, product_catalog, product_catalogId, product_catalogName, product_createdAt, product_createdBy, product_createdById, product_createdByName, product_data, product_ean, product_filterCreateImportJob, product_filterUpdateImportJob, product_hasChildren, product_hierarchyRoute, product_hierarchySortOrder, product_inheritedFields, product_isActive, product_isInheritAssignedUser, product_isInheritOwnerUser, product_isInheritTeams, product_isRoot, product_longDescription, product_longDescriptionDeDe, product_mainImageId, product_mainImageName, product_mainImagePathsData, product_modifiedAt, product_modifiedAtExpanded, product_modifiedBy, product_modifiedById, product_modifiedByName, product_mpn, product_name, product_nameDeDe, product_ownerUser, product_ownerUserId, product_ownerUserName, product_packaging, product_packagingId, product_packagingName, product_price, product_priceCurrency, product_productSerie, product_productSerieId, product_productSerieName, product_productStatus, product_scope, product_sku, product_sortOrder, product_sorting, product_tag, product_taskStatus, product_tax, product_taxId, product_taxName, product_uvp, scope, sorting, tags (optional)
    where = None # List[object] | There are a lot of filter types supported. You can learn all of them if you trace what's requested by Atro UI in the network tab in your browser console (press F12 key to open the console). (optional)
    offset = 0 # int |  (optional)
    max_size = 50 # int |  (optional)
    sort_by = 'name' # str |  (optional)
    asc = true # bool |  (optional)

    try:
        # Returns a collection of ProductAsset records
        api_response = api_instance.get_list_of_product_asset_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)
        print("The response of ProductAssetApi->get_list_of_product_asset_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->get_list_of_product_asset_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 
 **select** | **str**| Available fields: asset, assetId, assetName, asset_afterSaveMessage, asset_colorDepth, asset_colorSpace, asset_createdAt, asset_createdBy, asset_createdById, asset_createdByName, asset_description, asset_descriptionDeDe, asset_fileId, asset_fileName, asset_filePathsData, asset_filterCreateImportJob, asset_filterUpdateImportJob, asset_hasChildren, asset_height, asset_hierarchyRoute, asset_hierarchySortOrder, asset_icon, asset_inheritedFields, asset_isActive, asset_isRoot, asset_library, asset_libraryId, asset_libraryName, asset_modifiedAt, asset_modifiedBy, asset_modifiedById, asset_modifiedByName, asset_name, asset_orientation, asset_preview, asset_private, asset_size, asset_sortOrder, asset_tags, asset_type, asset_url, asset_width, channel, channelId, channelName, createdAt, createdBy, createdById, createdByName, deleted, fileId, fileName, filePathsData, filterCreateImportJob, filterUpdateImportJob, icon, id, isInherited, isMainImage, modifiedAt, modifiedBy, modifiedById, modifiedByName, name, preview, product, productId, productName, product_amount, product_assignedUser, product_assignedUserId, product_assignedUserName, product_brand, product_brandId, product_brandName, product_catalog, product_catalogId, product_catalogName, product_createdAt, product_createdBy, product_createdById, product_createdByName, product_data, product_ean, product_filterCreateImportJob, product_filterUpdateImportJob, product_hasChildren, product_hierarchyRoute, product_hierarchySortOrder, product_inheritedFields, product_isActive, product_isInheritAssignedUser, product_isInheritOwnerUser, product_isInheritTeams, product_isRoot, product_longDescription, product_longDescriptionDeDe, product_mainImageId, product_mainImageName, product_mainImagePathsData, product_modifiedAt, product_modifiedAtExpanded, product_modifiedBy, product_modifiedById, product_modifiedByName, product_mpn, product_name, product_nameDeDe, product_ownerUser, product_ownerUserId, product_ownerUserName, product_packaging, product_packagingId, product_packagingName, product_price, product_priceCurrency, product_productSerie, product_productSerieId, product_productSerieName, product_productStatus, product_scope, product_sku, product_sortOrder, product_sorting, product_tag, product_taskStatus, product_tax, product_taxId, product_taxName, product_uvp, scope, sorting, tags | [optional] 
 **where** | [**List[object]**](object.md)| There are a lot of filter types supported. You can learn all of them if you trace what&#39;s requested by Atro UI in the network tab in your browser console (press F12 key to open the console). | [optional] 
 **offset** | **int**|  | [optional] 
 **max_size** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **asc** | **bool**|  | [optional] 

### Return type

[**GetListOfProductAssetItems200Response**](GetListOfProductAssetItems200Response.md)

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

# **get_product_asset_item**
> ProductAsset get_product_asset_item(id, language=language)

Returns a record of the ProductAsset

Returns a record of the ProductAsset

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.product_asset import ProductAsset
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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    id = 'id_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns a record of the ProductAsset
        api_response = api_instance.get_product_asset_item(id, language=language)
        print("The response of ProductAssetApi->get_product_asset_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->get_product_asset_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 

### Return type

[**ProductAsset**](ProductAsset.md)

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

# **link_product_asset**
> bool link_product_asset(id, link, link_account_request)

Link ProductAsset to Entities

Link ProductAsset to Entities

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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Link ProductAsset to Entities
        api_response = api_instance.link_product_asset(id, link, link_account_request)
        print("The response of ProductAssetApi->link_product_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->link_product_asset: %s\n" % e)
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

# **mass_delete_product_asset**
> bool mass_delete_product_asset(link_account_request)

Mass delete of ProductAsset data

Mass delete of ProductAsset data

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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Mass delete of ProductAsset data
        api_response = api_instance.mass_delete_product_asset(link_account_request)
        print("The response of ProductAssetApi->mass_delete_product_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->mass_delete_product_asset: %s\n" % e)
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

# **mass_update_product_asset**
> bool mass_update_product_asset(mass_update_account_request)

Mass update of ProductAsset data

Mass update of ProductAsset data

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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    mass_update_account_request = clientapi_atrocore.MassUpdateAccountRequest() # MassUpdateAccountRequest | 

    try:
        # Mass update of ProductAsset data
        api_response = api_instance.mass_update_product_asset(mass_update_account_request)
        print("The response of ProductAssetApi->mass_update_product_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->mass_update_product_asset: %s\n" % e)
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

# **remove_relation_for_product_asset**
> bool remove_relation_for_product_asset(link, ids, foreign_ids)

Remove relation for ProductAsset

Remove relation for ProductAsset

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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Remove relation for ProductAsset
        api_response = api_instance.remove_relation_for_product_asset(link, ids, foreign_ids)
        print("The response of ProductAssetApi->remove_relation_for_product_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->remove_relation_for_product_asset: %s\n" % e)
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

# **unfollow_product_asset**
> bool unfollow_product_asset(id)

Unfollow the ProductAsset stream

Unfollow the ProductAsset stream

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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unfollow the ProductAsset stream
        api_response = api_instance.unfollow_product_asset(id)
        print("The response of ProductAssetApi->unfollow_product_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->unfollow_product_asset: %s\n" % e)
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

# **unlink_product_asset**
> bool unlink_product_asset(id, link, ids)

Unlink ProductAsset from Entities

Unlink ProductAsset from Entities

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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 

    try:
        # Unlink ProductAsset from Entities
        api_response = api_instance.unlink_product_asset(id, link, ids)
        print("The response of ProductAssetApi->unlink_product_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->unlink_product_asset: %s\n" % e)
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

# **update_product_asset_item**
> ProductAsset update_product_asset_item(id, create_product_asset_item_request)

Update a record of the ProductAsset

Update a record of the ProductAsset

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.create_product_asset_item_request import CreateProductAssetItemRequest
from clientapi_atrocore.models.product_asset import ProductAsset
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
    api_instance = clientapi_atrocore.ProductAssetApi(api_client)
    id = 'id_example' # str | 
    create_product_asset_item_request = clientapi_atrocore.CreateProductAssetItemRequest() # CreateProductAssetItemRequest | 

    try:
        # Update a record of the ProductAsset
        api_response = api_instance.update_product_asset_item(id, create_product_asset_item_request)
        print("The response of ProductAssetApi->update_product_asset_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAssetApi->update_product_asset_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_product_asset_item_request** | [**CreateProductAssetItemRequest**](CreateProductAssetItemRequest.md)|  | 

### Return type

[**ProductAsset**](ProductAsset.md)

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

