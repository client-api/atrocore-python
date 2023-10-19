# clientapi_atrocore.AssociatedProductApi

All URIs are relative to *https://demo.atropim.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation_for_associated_product**](AssociatedProductApi.md#add_relation_for_associated_product) | **POST** /AssociatedProduct/{link}/relation | Add relation for AssociatedProduct
[**create_associated_product_item**](AssociatedProductApi.md#create_associated_product_item) | **POST** /AssociatedProduct | Create a record of the AssociatedProduct
[**delete_associated_product_item**](AssociatedProductApi.md#delete_associated_product_item) | **DELETE** /AssociatedProduct/{id} | Delete a record of the AssociatedProduct
[**follow_associated_product**](AssociatedProductApi.md#follow_associated_product) | **PUT** /AssociatedProduct/{id}/subscription | Follow the AssociatedProduct stream
[**get_associated_product_item**](AssociatedProductApi.md#get_associated_product_item) | **GET** /AssociatedProduct/{id} | Returns a record of the AssociatedProduct
[**get_linked_items_for_associated_product_item**](AssociatedProductApi.md#get_linked_items_for_associated_product_item) | **GET** /AssociatedProduct/{id}/{link} | Returns linked entities for the AssociatedProduct
[**get_list_of_associated_product_items**](AssociatedProductApi.md#get_list_of_associated_product_items) | **GET** /AssociatedProduct | Returns a collection of AssociatedProduct records
[**link_associated_product**](AssociatedProductApi.md#link_associated_product) | **POST** /AssociatedProduct/{id}/{link} | Link AssociatedProduct to Entities
[**mass_delete_associated_product**](AssociatedProductApi.md#mass_delete_associated_product) | **POST** /AssociatedProduct/action/massDelete | Mass delete of AssociatedProduct data
[**mass_update_associated_product**](AssociatedProductApi.md#mass_update_associated_product) | **PUT** /AssociatedProduct/action/massUpdate | Mass update of AssociatedProduct data
[**remove_relation_for_associated_product**](AssociatedProductApi.md#remove_relation_for_associated_product) | **DELETE** /AssociatedProduct/{link}/relation | Remove relation for AssociatedProduct
[**unfollow_associated_product**](AssociatedProductApi.md#unfollow_associated_product) | **DELETE** /AssociatedProduct/{id}/subscription | Unfollow the AssociatedProduct stream
[**unlink_associated_product**](AssociatedProductApi.md#unlink_associated_product) | **DELETE** /AssociatedProduct/{id}/{link} | Unlink AssociatedProduct from Entities
[**update_associated_product_item**](AssociatedProductApi.md#update_associated_product_item) | **PUT** /AssociatedProduct/{id} | Update a record of the AssociatedProduct


# **add_relation_for_associated_product**
> bool add_relation_for_associated_product(link, ids, foreign_ids)

Add relation for AssociatedProduct

Add relation for AssociatedProduct

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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Add relation for AssociatedProduct
        api_response = api_instance.add_relation_for_associated_product(link, ids, foreign_ids)
        print("The response of AssociatedProductApi->add_relation_for_associated_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->add_relation_for_associated_product: %s\n" % e)
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

# **create_associated_product_item**
> AssociatedProduct create_associated_product_item(create_associated_product_item_request)

Create a record of the AssociatedProduct

Create a record of the AssociatedProduct

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.associated_product import AssociatedProduct
from clientapi_atrocore.models.create_associated_product_item_request import CreateAssociatedProductItemRequest
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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    create_associated_product_item_request = clientapi_atrocore.CreateAssociatedProductItemRequest() # CreateAssociatedProductItemRequest | 

    try:
        # Create a record of the AssociatedProduct
        api_response = api_instance.create_associated_product_item(create_associated_product_item_request)
        print("The response of AssociatedProductApi->create_associated_product_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->create_associated_product_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_associated_product_item_request** | [**CreateAssociatedProductItemRequest**](CreateAssociatedProductItemRequest.md)|  | 

### Return type

[**AssociatedProduct**](AssociatedProduct.md)

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

# **delete_associated_product_item**
> bool delete_associated_product_item(id)

Delete a record of the AssociatedProduct

Delete a record of the AssociatedProduct

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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a record of the AssociatedProduct
        api_response = api_instance.delete_associated_product_item(id)
        print("The response of AssociatedProductApi->delete_associated_product_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->delete_associated_product_item: %s\n" % e)
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

# **follow_associated_product**
> FollowAccount200Response follow_associated_product(id)

Follow the AssociatedProduct stream

Follow the AssociatedProduct stream

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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    id = 'id_example' # str | 

    try:
        # Follow the AssociatedProduct stream
        api_response = api_instance.follow_associated_product(id)
        print("The response of AssociatedProductApi->follow_associated_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->follow_associated_product: %s\n" % e)
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

# **get_associated_product_item**
> AssociatedProduct get_associated_product_item(id, language=language)

Returns a record of the AssociatedProduct

Returns a record of the AssociatedProduct

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.associated_product import AssociatedProduct
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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    id = 'id_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns a record of the AssociatedProduct
        api_response = api_instance.get_associated_product_item(id, language=language)
        print("The response of AssociatedProductApi->get_associated_product_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->get_associated_product_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 

### Return type

[**AssociatedProduct**](AssociatedProduct.md)

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

# **get_linked_items_for_associated_product_item**
> GetLinkedItemsForAccountItem200Response get_linked_items_for_associated_product_item(id, link, language=language)

Returns linked entities for the AssociatedProduct

Returns linked entities for the AssociatedProduct

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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns linked entities for the AssociatedProduct
        api_response = api_instance.get_linked_items_for_associated_product_item(id, link, language=language)
        print("The response of AssociatedProductApi->get_linked_items_for_associated_product_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->get_linked_items_for_associated_product_item: %s\n" % e)
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

# **get_list_of_associated_product_items**
> GetListOfAssociatedProductItems200Response get_list_of_associated_product_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)

Returns a collection of AssociatedProduct records

Returns a collection of AssociatedProduct records

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.get_list_of_associated_product_items200_response import GetListOfAssociatedProductItems200Response
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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)
    select = 'name,createdAt' # str | Available fields: association, associationId, associationName, association_assignedUser, association_assignedUserId, association_assignedUserName, association_backwardAssociation, association_backwardAssociationId, association_backwardAssociationName, association_code, association_createdAt, association_createdBy, association_createdById, association_createdByName, association_description, association_descriptionDeDe, association_filterCreateImportJob, association_filterUpdateImportJob, association_isActive, association_modifiedAt, association_modifiedBy, association_modifiedById, association_modifiedByName, association_name, association_nameDeDe, association_ownerUser, association_ownerUserId, association_ownerUserName, backwardAssociatedProduct, backwardAssociatedProductId, backwardAssociation, backwardAssociationId, backwardAssociationName, createdAt, createdBy, createdById, createdByName, deleted, filterCreateImportJob, filterUpdateImportJob, id, isInherited, mainProduct, mainProductId, mainProductImageId, mainProductImageName, mainProductImagePathsData, mainProductName, mainProduct_amount, mainProduct_assignedUser, mainProduct_assignedUserId, mainProduct_assignedUserName, mainProduct_brand, mainProduct_brandId, mainProduct_brandName, mainProduct_catalog, mainProduct_catalogId, mainProduct_catalogName, mainProduct_createdAt, mainProduct_createdBy, mainProduct_createdById, mainProduct_createdByName, mainProduct_data, mainProduct_ean, mainProduct_filterCreateImportJob, mainProduct_filterUpdateImportJob, mainProduct_hasChildren, mainProduct_hierarchyRoute, mainProduct_hierarchySortOrder, mainProduct_inheritedFields, mainProduct_isActive, mainProduct_isInheritAssignedUser, mainProduct_isInheritOwnerUser, mainProduct_isInheritTeams, mainProduct_isRoot, mainProduct_longDescription, mainProduct_longDescriptionDeDe, mainProduct_mainImageId, mainProduct_mainImageName, mainProduct_mainImagePathsData, mainProduct_modifiedAt, mainProduct_modifiedAtExpanded, mainProduct_modifiedBy, mainProduct_modifiedById, mainProduct_modifiedByName, mainProduct_mpn, mainProduct_name, mainProduct_nameDeDe, mainProduct_ownerUser, mainProduct_ownerUserId, mainProduct_ownerUserName, mainProduct_packaging, mainProduct_packagingId, mainProduct_packagingName, mainProduct_price, mainProduct_priceCurrency, mainProduct_productSerie, mainProduct_productSerieId, mainProduct_productSerieName, mainProduct_productStatus, mainProduct_scope, mainProduct_sku, mainProduct_sortOrder, mainProduct_sorting, mainProduct_tag, mainProduct_taskStatus, mainProduct_tax, mainProduct_taxId, mainProduct_taxName, mainProduct_uvp, modifiedAt, modifiedBy, modifiedById, modifiedByName, name, relatedProduct, relatedProductId, relatedProductImageId, relatedProductImageName, relatedProductImagePathsData, relatedProductName, relatedProduct_amount, relatedProduct_assignedUser, relatedProduct_assignedUserId, relatedProduct_assignedUserName, relatedProduct_brand, relatedProduct_brandId, relatedProduct_brandName, relatedProduct_catalog, relatedProduct_catalogId, relatedProduct_catalogName, relatedProduct_createdAt, relatedProduct_createdBy, relatedProduct_createdById, relatedProduct_createdByName, relatedProduct_data, relatedProduct_ean, relatedProduct_filterCreateImportJob, relatedProduct_filterUpdateImportJob, relatedProduct_hasChildren, relatedProduct_hierarchyRoute, relatedProduct_hierarchySortOrder, relatedProduct_inheritedFields, relatedProduct_isActive, relatedProduct_isInheritAssignedUser, relatedProduct_isInheritOwnerUser, relatedProduct_isInheritTeams, relatedProduct_isRoot, relatedProduct_longDescription, relatedProduct_longDescriptionDeDe, relatedProduct_mainImageId, relatedProduct_mainImageName, relatedProduct_mainImagePathsData, relatedProduct_modifiedAt, relatedProduct_modifiedAtExpanded, relatedProduct_modifiedBy, relatedProduct_modifiedById, relatedProduct_modifiedByName, relatedProduct_mpn, relatedProduct_name, relatedProduct_nameDeDe, relatedProduct_ownerUser, relatedProduct_ownerUserId, relatedProduct_ownerUserName, relatedProduct_packaging, relatedProduct_packagingId, relatedProduct_packagingName, relatedProduct_price, relatedProduct_priceCurrency, relatedProduct_productSerie, relatedProduct_productSerieId, relatedProduct_productSerieName, relatedProduct_productStatus, relatedProduct_scope, relatedProduct_sku, relatedProduct_sortOrder, relatedProduct_sorting, relatedProduct_tag, relatedProduct_taskStatus, relatedProduct_tax, relatedProduct_taxId, relatedProduct_taxName, relatedProduct_uvp, sorting (optional)
    where = None # List[object] | There are a lot of filter types supported. You can learn all of them if you trace what's requested by Atro UI in the network tab in your browser console (press F12 key to open the console). (optional)
    offset = 0 # int |  (optional)
    max_size = 50 # int |  (optional)
    sort_by = 'name' # str |  (optional)
    asc = true # bool |  (optional)

    try:
        # Returns a collection of AssociatedProduct records
        api_response = api_instance.get_list_of_associated_product_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)
        print("The response of AssociatedProductApi->get_list_of_associated_product_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->get_list_of_associated_product_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 
 **select** | **str**| Available fields: association, associationId, associationName, association_assignedUser, association_assignedUserId, association_assignedUserName, association_backwardAssociation, association_backwardAssociationId, association_backwardAssociationName, association_code, association_createdAt, association_createdBy, association_createdById, association_createdByName, association_description, association_descriptionDeDe, association_filterCreateImportJob, association_filterUpdateImportJob, association_isActive, association_modifiedAt, association_modifiedBy, association_modifiedById, association_modifiedByName, association_name, association_nameDeDe, association_ownerUser, association_ownerUserId, association_ownerUserName, backwardAssociatedProduct, backwardAssociatedProductId, backwardAssociation, backwardAssociationId, backwardAssociationName, createdAt, createdBy, createdById, createdByName, deleted, filterCreateImportJob, filterUpdateImportJob, id, isInherited, mainProduct, mainProductId, mainProductImageId, mainProductImageName, mainProductImagePathsData, mainProductName, mainProduct_amount, mainProduct_assignedUser, mainProduct_assignedUserId, mainProduct_assignedUserName, mainProduct_brand, mainProduct_brandId, mainProduct_brandName, mainProduct_catalog, mainProduct_catalogId, mainProduct_catalogName, mainProduct_createdAt, mainProduct_createdBy, mainProduct_createdById, mainProduct_createdByName, mainProduct_data, mainProduct_ean, mainProduct_filterCreateImportJob, mainProduct_filterUpdateImportJob, mainProduct_hasChildren, mainProduct_hierarchyRoute, mainProduct_hierarchySortOrder, mainProduct_inheritedFields, mainProduct_isActive, mainProduct_isInheritAssignedUser, mainProduct_isInheritOwnerUser, mainProduct_isInheritTeams, mainProduct_isRoot, mainProduct_longDescription, mainProduct_longDescriptionDeDe, mainProduct_mainImageId, mainProduct_mainImageName, mainProduct_mainImagePathsData, mainProduct_modifiedAt, mainProduct_modifiedAtExpanded, mainProduct_modifiedBy, mainProduct_modifiedById, mainProduct_modifiedByName, mainProduct_mpn, mainProduct_name, mainProduct_nameDeDe, mainProduct_ownerUser, mainProduct_ownerUserId, mainProduct_ownerUserName, mainProduct_packaging, mainProduct_packagingId, mainProduct_packagingName, mainProduct_price, mainProduct_priceCurrency, mainProduct_productSerie, mainProduct_productSerieId, mainProduct_productSerieName, mainProduct_productStatus, mainProduct_scope, mainProduct_sku, mainProduct_sortOrder, mainProduct_sorting, mainProduct_tag, mainProduct_taskStatus, mainProduct_tax, mainProduct_taxId, mainProduct_taxName, mainProduct_uvp, modifiedAt, modifiedBy, modifiedById, modifiedByName, name, relatedProduct, relatedProductId, relatedProductImageId, relatedProductImageName, relatedProductImagePathsData, relatedProductName, relatedProduct_amount, relatedProduct_assignedUser, relatedProduct_assignedUserId, relatedProduct_assignedUserName, relatedProduct_brand, relatedProduct_brandId, relatedProduct_brandName, relatedProduct_catalog, relatedProduct_catalogId, relatedProduct_catalogName, relatedProduct_createdAt, relatedProduct_createdBy, relatedProduct_createdById, relatedProduct_createdByName, relatedProduct_data, relatedProduct_ean, relatedProduct_filterCreateImportJob, relatedProduct_filterUpdateImportJob, relatedProduct_hasChildren, relatedProduct_hierarchyRoute, relatedProduct_hierarchySortOrder, relatedProduct_inheritedFields, relatedProduct_isActive, relatedProduct_isInheritAssignedUser, relatedProduct_isInheritOwnerUser, relatedProduct_isInheritTeams, relatedProduct_isRoot, relatedProduct_longDescription, relatedProduct_longDescriptionDeDe, relatedProduct_mainImageId, relatedProduct_mainImageName, relatedProduct_mainImagePathsData, relatedProduct_modifiedAt, relatedProduct_modifiedAtExpanded, relatedProduct_modifiedBy, relatedProduct_modifiedById, relatedProduct_modifiedByName, relatedProduct_mpn, relatedProduct_name, relatedProduct_nameDeDe, relatedProduct_ownerUser, relatedProduct_ownerUserId, relatedProduct_ownerUserName, relatedProduct_packaging, relatedProduct_packagingId, relatedProduct_packagingName, relatedProduct_price, relatedProduct_priceCurrency, relatedProduct_productSerie, relatedProduct_productSerieId, relatedProduct_productSerieName, relatedProduct_productStatus, relatedProduct_scope, relatedProduct_sku, relatedProduct_sortOrder, relatedProduct_sorting, relatedProduct_tag, relatedProduct_taskStatus, relatedProduct_tax, relatedProduct_taxId, relatedProduct_taxName, relatedProduct_uvp, sorting | [optional] 
 **where** | [**List[object]**](object.md)| There are a lot of filter types supported. You can learn all of them if you trace what&#39;s requested by Atro UI in the network tab in your browser console (press F12 key to open the console). | [optional] 
 **offset** | **int**|  | [optional] 
 **max_size** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **asc** | **bool**|  | [optional] 

### Return type

[**GetListOfAssociatedProductItems200Response**](GetListOfAssociatedProductItems200Response.md)

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

# **link_associated_product**
> bool link_associated_product(id, link, link_account_request)

Link AssociatedProduct to Entities

Link AssociatedProduct to Entities

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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Link AssociatedProduct to Entities
        api_response = api_instance.link_associated_product(id, link, link_account_request)
        print("The response of AssociatedProductApi->link_associated_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->link_associated_product: %s\n" % e)
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

# **mass_delete_associated_product**
> bool mass_delete_associated_product(link_account_request)

Mass delete of AssociatedProduct data

Mass delete of AssociatedProduct data

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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Mass delete of AssociatedProduct data
        api_response = api_instance.mass_delete_associated_product(link_account_request)
        print("The response of AssociatedProductApi->mass_delete_associated_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->mass_delete_associated_product: %s\n" % e)
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

# **mass_update_associated_product**
> bool mass_update_associated_product(mass_update_account_request)

Mass update of AssociatedProduct data

Mass update of AssociatedProduct data

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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    mass_update_account_request = clientapi_atrocore.MassUpdateAccountRequest() # MassUpdateAccountRequest | 

    try:
        # Mass update of AssociatedProduct data
        api_response = api_instance.mass_update_associated_product(mass_update_account_request)
        print("The response of AssociatedProductApi->mass_update_associated_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->mass_update_associated_product: %s\n" % e)
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

# **remove_relation_for_associated_product**
> bool remove_relation_for_associated_product(link, ids, foreign_ids)

Remove relation for AssociatedProduct

Remove relation for AssociatedProduct

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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Remove relation for AssociatedProduct
        api_response = api_instance.remove_relation_for_associated_product(link, ids, foreign_ids)
        print("The response of AssociatedProductApi->remove_relation_for_associated_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->remove_relation_for_associated_product: %s\n" % e)
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

# **unfollow_associated_product**
> bool unfollow_associated_product(id)

Unfollow the AssociatedProduct stream

Unfollow the AssociatedProduct stream

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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unfollow the AssociatedProduct stream
        api_response = api_instance.unfollow_associated_product(id)
        print("The response of AssociatedProductApi->unfollow_associated_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->unfollow_associated_product: %s\n" % e)
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

# **unlink_associated_product**
> bool unlink_associated_product(id, link, ids)

Unlink AssociatedProduct from Entities

Unlink AssociatedProduct from Entities

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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 

    try:
        # Unlink AssociatedProduct from Entities
        api_response = api_instance.unlink_associated_product(id, link, ids)
        print("The response of AssociatedProductApi->unlink_associated_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->unlink_associated_product: %s\n" % e)
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

# **update_associated_product_item**
> AssociatedProduct update_associated_product_item(id, create_associated_product_item_request)

Update a record of the AssociatedProduct

Update a record of the AssociatedProduct

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.associated_product import AssociatedProduct
from clientapi_atrocore.models.create_associated_product_item_request import CreateAssociatedProductItemRequest
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
    api_instance = clientapi_atrocore.AssociatedProductApi(api_client)
    id = 'id_example' # str | 
    create_associated_product_item_request = clientapi_atrocore.CreateAssociatedProductItemRequest() # CreateAssociatedProductItemRequest | 

    try:
        # Update a record of the AssociatedProduct
        api_response = api_instance.update_associated_product_item(id, create_associated_product_item_request)
        print("The response of AssociatedProductApi->update_associated_product_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssociatedProductApi->update_associated_product_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_associated_product_item_request** | [**CreateAssociatedProductItemRequest**](CreateAssociatedProductItemRequest.md)|  | 

### Return type

[**AssociatedProduct**](AssociatedProduct.md)

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

