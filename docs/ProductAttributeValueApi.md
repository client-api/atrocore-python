# clientapi_atrocore.ProductAttributeValueApi

All URIs are relative to *https://demo.atropim.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation_for_product_attribute_value**](ProductAttributeValueApi.md#add_relation_for_product_attribute_value) | **POST** /ProductAttributeValue/{link}/relation | Add relation for ProductAttributeValue
[**create_product_attribute_value_item**](ProductAttributeValueApi.md#create_product_attribute_value_item) | **POST** /ProductAttributeValue | Create a record of the ProductAttributeValue
[**delete_product_attribute_value_item**](ProductAttributeValueApi.md#delete_product_attribute_value_item) | **DELETE** /ProductAttributeValue/{id} | Delete a record of the ProductAttributeValue
[**follow_product_attribute_value**](ProductAttributeValueApi.md#follow_product_attribute_value) | **PUT** /ProductAttributeValue/{id}/subscription | Follow the ProductAttributeValue stream
[**get_linked_items_for_product_attribute_value_item**](ProductAttributeValueApi.md#get_linked_items_for_product_attribute_value_item) | **GET** /ProductAttributeValue/{id}/{link} | Returns linked entities for the ProductAttributeValue
[**get_list_of_product_attribute_value_items**](ProductAttributeValueApi.md#get_list_of_product_attribute_value_items) | **GET** /ProductAttributeValue | Returns a collection of ProductAttributeValue records
[**get_product_attribute_value_item**](ProductAttributeValueApi.md#get_product_attribute_value_item) | **GET** /ProductAttributeValue/{id} | Returns a record of the ProductAttributeValue
[**link_product_attribute_value**](ProductAttributeValueApi.md#link_product_attribute_value) | **POST** /ProductAttributeValue/{id}/{link} | Link ProductAttributeValue to Entities
[**mass_delete_product_attribute_value**](ProductAttributeValueApi.md#mass_delete_product_attribute_value) | **POST** /ProductAttributeValue/action/massDelete | Mass delete of ProductAttributeValue data
[**mass_update_product_attribute_value**](ProductAttributeValueApi.md#mass_update_product_attribute_value) | **PUT** /ProductAttributeValue/action/massUpdate | Mass update of ProductAttributeValue data
[**remove_relation_for_product_attribute_value**](ProductAttributeValueApi.md#remove_relation_for_product_attribute_value) | **DELETE** /ProductAttributeValue/{link}/relation | Remove relation for ProductAttributeValue
[**unfollow_product_attribute_value**](ProductAttributeValueApi.md#unfollow_product_attribute_value) | **DELETE** /ProductAttributeValue/{id}/subscription | Unfollow the ProductAttributeValue stream
[**unlink_product_attribute_value**](ProductAttributeValueApi.md#unlink_product_attribute_value) | **DELETE** /ProductAttributeValue/{id}/{link} | Unlink ProductAttributeValue from Entities
[**update_product_attribute_value_item**](ProductAttributeValueApi.md#update_product_attribute_value_item) | **PUT** /ProductAttributeValue/{id} | Update a record of the ProductAttributeValue


# **add_relation_for_product_attribute_value**
> bool add_relation_for_product_attribute_value(link, ids, foreign_ids)

Add relation for ProductAttributeValue

Add relation for ProductAttributeValue

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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Add relation for ProductAttributeValue
        api_response = api_instance.add_relation_for_product_attribute_value(link, ids, foreign_ids)
        print("The response of ProductAttributeValueApi->add_relation_for_product_attribute_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->add_relation_for_product_attribute_value: %s\n" % e)
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

# **create_product_attribute_value_item**
> ProductAttributeValue create_product_attribute_value_item(create_product_attribute_value_item_request)

Create a record of the ProductAttributeValue

Create a record of the ProductAttributeValue

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.create_product_attribute_value_item_request import CreateProductAttributeValueItemRequest
from clientapi_atrocore.models.product_attribute_value import ProductAttributeValue
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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    create_product_attribute_value_item_request = clientapi_atrocore.CreateProductAttributeValueItemRequest() # CreateProductAttributeValueItemRequest | 

    try:
        # Create a record of the ProductAttributeValue
        api_response = api_instance.create_product_attribute_value_item(create_product_attribute_value_item_request)
        print("The response of ProductAttributeValueApi->create_product_attribute_value_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->create_product_attribute_value_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_product_attribute_value_item_request** | [**CreateProductAttributeValueItemRequest**](CreateProductAttributeValueItemRequest.md)|  | 

### Return type

[**ProductAttributeValue**](ProductAttributeValue.md)

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

# **delete_product_attribute_value_item**
> bool delete_product_attribute_value_item(id)

Delete a record of the ProductAttributeValue

Delete a record of the ProductAttributeValue

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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a record of the ProductAttributeValue
        api_response = api_instance.delete_product_attribute_value_item(id)
        print("The response of ProductAttributeValueApi->delete_product_attribute_value_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->delete_product_attribute_value_item: %s\n" % e)
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

# **follow_product_attribute_value**
> FollowAccount200Response follow_product_attribute_value(id)

Follow the ProductAttributeValue stream

Follow the ProductAttributeValue stream

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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    id = 'id_example' # str | 

    try:
        # Follow the ProductAttributeValue stream
        api_response = api_instance.follow_product_attribute_value(id)
        print("The response of ProductAttributeValueApi->follow_product_attribute_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->follow_product_attribute_value: %s\n" % e)
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

# **get_linked_items_for_product_attribute_value_item**
> GetLinkedItemsForAccountItem200Response get_linked_items_for_product_attribute_value_item(id, link, language=language)

Returns linked entities for the ProductAttributeValue

Returns linked entities for the ProductAttributeValue

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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns linked entities for the ProductAttributeValue
        api_response = api_instance.get_linked_items_for_product_attribute_value_item(id, link, language=language)
        print("The response of ProductAttributeValueApi->get_linked_items_for_product_attribute_value_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->get_linked_items_for_product_attribute_value_item: %s\n" % e)
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

# **get_list_of_product_attribute_value_items**
> GetListOfProductAttributeValueItems200Response get_list_of_product_attribute_value_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)

Returns a collection of ProductAttributeValue records

Returns a collection of ProductAttributeValue records

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.get_list_of_product_attribute_value_items200_response import GetListOfProductAttributeValueItems200Response
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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)
    select = 'name,createdAt' # str | Available fields: amountOfDigitsAfterComma, assignedUser, assignedUserId, assignedUserName, attribute, attributeAssetType, attributeCode, attributeEntityType, attributeExtensibleEnumId, attributeGroup, attributeGroupId, attributeGroupName, attributeId, attributeIsMultilang, attributeMeasureId, attributeName, attributeTooltip, attributeType, attribute_amountOfDigitsAfterComma, attribute_assetType, attribute_assignedUser, attribute_assignedUserId, attribute_assignedUserName, attribute_attributeGroup, attribute_attributeGroupId, attribute_attributeGroupName, attribute_attributeTab, attribute_attributeTabId, attribute_attributeTabName, attribute_code, attribute_countBytesInsteadOfCharacters, attribute_createdAt, attribute_createdBy, attribute_createdById, attribute_createdByName, attribute_data, attribute_defaultChannel, attribute_defaultChannelId, attribute_defaultChannelName, attribute_defaultScope, attribute_defaultUnit, attribute_description, attribute_descriptionDeDe, attribute_extensibleEnum, attribute_extensibleEnumId, attribute_extensibleEnumName, attribute_filterCreateImportJob, attribute_filterUpdateImportJob, attribute_hasChildren, attribute_hierarchyRoute, attribute_hierarchySortOrder, attribute_inheritedFields, attribute_isMultilang, attribute_isRequired, attribute_isRoot, attribute_max, attribute_maxLength, attribute_measure, attribute_measureId, attribute_measureName, attribute_min, attribute_modifiedAt, attribute_modifiedBy, attribute_modifiedById, attribute_modifiedByName, attribute_name, attribute_nameDeDe, attribute_ownerUser, attribute_ownerUserId, attribute_ownerUserName, attribute_pattern, attribute_prohibitedEmptyValue, attribute_sortOrder, attribute_sortOrderInAttributeGroup, attribute_sortOrderInProduct, attribute_tooltip, attribute_tooltipDeDe, attribute_type, attribute_unique, attribute_useDisabledTextareaInViewMode, attribute_virtualProductField, boolValue, channel, channelCode, channelId, channelName, countBytesInsteadOfCharacters, createdAt, createdBy, createdById, createdByName, data, dateValue, datetimeValue, deleted, filterCreateImportJob, filterUpdateImportJob, floatValue, floatValue1, icons, id, intValue, intValue1, isInheritAssignedUser, isInheritOwnerUser, isInheritTeams, isInherited, isPavRelationInherited, isPavValueInherited, isRequired, isValueReadOnly, isVariantSpecificAttribute, language, mainLanguageId, max, maxLength, min, modifiedAt, modifiedBy, modifiedById, modifiedByName, name, ownerUser, ownerUserId, ownerUserName, product, productId, productName, product_amount, product_assignedUser, product_assignedUserId, product_assignedUserName, product_brand, product_brandId, product_brandName, product_catalog, product_catalogId, product_catalogName, product_createdAt, product_createdBy, product_createdById, product_createdByName, product_data, product_ean, product_filterCreateImportJob, product_filterUpdateImportJob, product_hasChildren, product_hierarchyRoute, product_hierarchySortOrder, product_inheritedFields, product_isActive, product_isInheritAssignedUser, product_isInheritOwnerUser, product_isInheritTeams, product_isRoot, product_longDescription, product_longDescriptionDeDe, product_mainImageId, product_mainImageName, product_mainImagePathsData, product_modifiedAt, product_modifiedAtExpanded, product_modifiedBy, product_modifiedById, product_modifiedByName, product_mpn, product_name, product_nameDeDe, product_ownerUser, product_ownerUserId, product_ownerUserName, product_packaging, product_packagingId, product_packagingName, product_price, product_priceCurrency, product_productSerie, product_productSerieId, product_productSerieName, product_productStatus, product_scope, product_sku, product_sortOrder, product_sorting, product_tag, product_taskStatus, product_tax, product_taxId, product_taxName, product_uvp, prohibitedEmptyValue, scope, sortOrder, teams, teamsIds, teamsNames, textValue, useDisabledTextareaInViewMode, value, valueAllUnits, valueCurrency, valueFrom, valueId, valueName, valueNames, valueOptionData, valueOptionsData, valuePathsData, valueTo, valueUnit, valueUnitId, varcharValue (optional)
    where = None # List[object] | There are a lot of filter types supported. You can learn all of them if you trace what's requested by Atro UI in the network tab in your browser console (press F12 key to open the console). (optional)
    offset = 0 # int |  (optional)
    max_size = 50 # int |  (optional)
    sort_by = 'name' # str |  (optional)
    asc = true # bool |  (optional)

    try:
        # Returns a collection of ProductAttributeValue records
        api_response = api_instance.get_list_of_product_attribute_value_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)
        print("The response of ProductAttributeValueApi->get_list_of_product_attribute_value_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->get_list_of_product_attribute_value_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 
 **select** | **str**| Available fields: amountOfDigitsAfterComma, assignedUser, assignedUserId, assignedUserName, attribute, attributeAssetType, attributeCode, attributeEntityType, attributeExtensibleEnumId, attributeGroup, attributeGroupId, attributeGroupName, attributeId, attributeIsMultilang, attributeMeasureId, attributeName, attributeTooltip, attributeType, attribute_amountOfDigitsAfterComma, attribute_assetType, attribute_assignedUser, attribute_assignedUserId, attribute_assignedUserName, attribute_attributeGroup, attribute_attributeGroupId, attribute_attributeGroupName, attribute_attributeTab, attribute_attributeTabId, attribute_attributeTabName, attribute_code, attribute_countBytesInsteadOfCharacters, attribute_createdAt, attribute_createdBy, attribute_createdById, attribute_createdByName, attribute_data, attribute_defaultChannel, attribute_defaultChannelId, attribute_defaultChannelName, attribute_defaultScope, attribute_defaultUnit, attribute_description, attribute_descriptionDeDe, attribute_extensibleEnum, attribute_extensibleEnumId, attribute_extensibleEnumName, attribute_filterCreateImportJob, attribute_filterUpdateImportJob, attribute_hasChildren, attribute_hierarchyRoute, attribute_hierarchySortOrder, attribute_inheritedFields, attribute_isMultilang, attribute_isRequired, attribute_isRoot, attribute_max, attribute_maxLength, attribute_measure, attribute_measureId, attribute_measureName, attribute_min, attribute_modifiedAt, attribute_modifiedBy, attribute_modifiedById, attribute_modifiedByName, attribute_name, attribute_nameDeDe, attribute_ownerUser, attribute_ownerUserId, attribute_ownerUserName, attribute_pattern, attribute_prohibitedEmptyValue, attribute_sortOrder, attribute_sortOrderInAttributeGroup, attribute_sortOrderInProduct, attribute_tooltip, attribute_tooltipDeDe, attribute_type, attribute_unique, attribute_useDisabledTextareaInViewMode, attribute_virtualProductField, boolValue, channel, channelCode, channelId, channelName, countBytesInsteadOfCharacters, createdAt, createdBy, createdById, createdByName, data, dateValue, datetimeValue, deleted, filterCreateImportJob, filterUpdateImportJob, floatValue, floatValue1, icons, id, intValue, intValue1, isInheritAssignedUser, isInheritOwnerUser, isInheritTeams, isInherited, isPavRelationInherited, isPavValueInherited, isRequired, isValueReadOnly, isVariantSpecificAttribute, language, mainLanguageId, max, maxLength, min, modifiedAt, modifiedBy, modifiedById, modifiedByName, name, ownerUser, ownerUserId, ownerUserName, product, productId, productName, product_amount, product_assignedUser, product_assignedUserId, product_assignedUserName, product_brand, product_brandId, product_brandName, product_catalog, product_catalogId, product_catalogName, product_createdAt, product_createdBy, product_createdById, product_createdByName, product_data, product_ean, product_filterCreateImportJob, product_filterUpdateImportJob, product_hasChildren, product_hierarchyRoute, product_hierarchySortOrder, product_inheritedFields, product_isActive, product_isInheritAssignedUser, product_isInheritOwnerUser, product_isInheritTeams, product_isRoot, product_longDescription, product_longDescriptionDeDe, product_mainImageId, product_mainImageName, product_mainImagePathsData, product_modifiedAt, product_modifiedAtExpanded, product_modifiedBy, product_modifiedById, product_modifiedByName, product_mpn, product_name, product_nameDeDe, product_ownerUser, product_ownerUserId, product_ownerUserName, product_packaging, product_packagingId, product_packagingName, product_price, product_priceCurrency, product_productSerie, product_productSerieId, product_productSerieName, product_productStatus, product_scope, product_sku, product_sortOrder, product_sorting, product_tag, product_taskStatus, product_tax, product_taxId, product_taxName, product_uvp, prohibitedEmptyValue, scope, sortOrder, teams, teamsIds, teamsNames, textValue, useDisabledTextareaInViewMode, value, valueAllUnits, valueCurrency, valueFrom, valueId, valueName, valueNames, valueOptionData, valueOptionsData, valuePathsData, valueTo, valueUnit, valueUnitId, varcharValue | [optional] 
 **where** | [**List[object]**](object.md)| There are a lot of filter types supported. You can learn all of them if you trace what&#39;s requested by Atro UI in the network tab in your browser console (press F12 key to open the console). | [optional] 
 **offset** | **int**|  | [optional] 
 **max_size** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **asc** | **bool**|  | [optional] 

### Return type

[**GetListOfProductAttributeValueItems200Response**](GetListOfProductAttributeValueItems200Response.md)

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

# **get_product_attribute_value_item**
> ProductAttributeValue get_product_attribute_value_item(id, language=language)

Returns a record of the ProductAttributeValue

Returns a record of the ProductAttributeValue

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.product_attribute_value import ProductAttributeValue
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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    id = 'id_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns a record of the ProductAttributeValue
        api_response = api_instance.get_product_attribute_value_item(id, language=language)
        print("The response of ProductAttributeValueApi->get_product_attribute_value_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->get_product_attribute_value_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 

### Return type

[**ProductAttributeValue**](ProductAttributeValue.md)

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

# **link_product_attribute_value**
> bool link_product_attribute_value(id, link, link_account_request)

Link ProductAttributeValue to Entities

Link ProductAttributeValue to Entities

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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Link ProductAttributeValue to Entities
        api_response = api_instance.link_product_attribute_value(id, link, link_account_request)
        print("The response of ProductAttributeValueApi->link_product_attribute_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->link_product_attribute_value: %s\n" % e)
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

# **mass_delete_product_attribute_value**
> bool mass_delete_product_attribute_value(link_account_request)

Mass delete of ProductAttributeValue data

Mass delete of ProductAttributeValue data

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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Mass delete of ProductAttributeValue data
        api_response = api_instance.mass_delete_product_attribute_value(link_account_request)
        print("The response of ProductAttributeValueApi->mass_delete_product_attribute_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->mass_delete_product_attribute_value: %s\n" % e)
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

# **mass_update_product_attribute_value**
> bool mass_update_product_attribute_value(mass_update_account_request)

Mass update of ProductAttributeValue data

Mass update of ProductAttributeValue data

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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    mass_update_account_request = clientapi_atrocore.MassUpdateAccountRequest() # MassUpdateAccountRequest | 

    try:
        # Mass update of ProductAttributeValue data
        api_response = api_instance.mass_update_product_attribute_value(mass_update_account_request)
        print("The response of ProductAttributeValueApi->mass_update_product_attribute_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->mass_update_product_attribute_value: %s\n" % e)
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

# **remove_relation_for_product_attribute_value**
> bool remove_relation_for_product_attribute_value(link, ids, foreign_ids)

Remove relation for ProductAttributeValue

Remove relation for ProductAttributeValue

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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Remove relation for ProductAttributeValue
        api_response = api_instance.remove_relation_for_product_attribute_value(link, ids, foreign_ids)
        print("The response of ProductAttributeValueApi->remove_relation_for_product_attribute_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->remove_relation_for_product_attribute_value: %s\n" % e)
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

# **unfollow_product_attribute_value**
> bool unfollow_product_attribute_value(id)

Unfollow the ProductAttributeValue stream

Unfollow the ProductAttributeValue stream

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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unfollow the ProductAttributeValue stream
        api_response = api_instance.unfollow_product_attribute_value(id)
        print("The response of ProductAttributeValueApi->unfollow_product_attribute_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->unfollow_product_attribute_value: %s\n" % e)
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

# **unlink_product_attribute_value**
> bool unlink_product_attribute_value(id, link, ids)

Unlink ProductAttributeValue from Entities

Unlink ProductAttributeValue from Entities

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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 

    try:
        # Unlink ProductAttributeValue from Entities
        api_response = api_instance.unlink_product_attribute_value(id, link, ids)
        print("The response of ProductAttributeValueApi->unlink_product_attribute_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->unlink_product_attribute_value: %s\n" % e)
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

# **update_product_attribute_value_item**
> ProductAttributeValue update_product_attribute_value_item(id, create_product_attribute_value_item_request)

Update a record of the ProductAttributeValue

Update a record of the ProductAttributeValue

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.create_product_attribute_value_item_request import CreateProductAttributeValueItemRequest
from clientapi_atrocore.models.product_attribute_value import ProductAttributeValue
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
    api_instance = clientapi_atrocore.ProductAttributeValueApi(api_client)
    id = 'id_example' # str | 
    create_product_attribute_value_item_request = clientapi_atrocore.CreateProductAttributeValueItemRequest() # CreateProductAttributeValueItemRequest | 

    try:
        # Update a record of the ProductAttributeValue
        api_response = api_instance.update_product_attribute_value_item(id, create_product_attribute_value_item_request)
        print("The response of ProductAttributeValueApi->update_product_attribute_value_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAttributeValueApi->update_product_attribute_value_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_product_attribute_value_item_request** | [**CreateProductAttributeValueItemRequest**](CreateProductAttributeValueItemRequest.md)|  | 

### Return type

[**ProductAttributeValue**](ProductAttributeValue.md)

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

