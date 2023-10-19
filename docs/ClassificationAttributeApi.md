# clientapi_atrocore.ClassificationAttributeApi

All URIs are relative to *https://demo.atropim.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation_for_classification_attribute**](ClassificationAttributeApi.md#add_relation_for_classification_attribute) | **POST** /ClassificationAttribute/{link}/relation | Add relation for ClassificationAttribute
[**create_classification_attribute_item**](ClassificationAttributeApi.md#create_classification_attribute_item) | **POST** /ClassificationAttribute | Create a record of the ClassificationAttribute
[**delete_classification_attribute_item**](ClassificationAttributeApi.md#delete_classification_attribute_item) | **DELETE** /ClassificationAttribute/{id} | Delete a record of the ClassificationAttribute
[**follow_classification_attribute**](ClassificationAttributeApi.md#follow_classification_attribute) | **PUT** /ClassificationAttribute/{id}/subscription | Follow the ClassificationAttribute stream
[**get_classification_attribute_item**](ClassificationAttributeApi.md#get_classification_attribute_item) | **GET** /ClassificationAttribute/{id} | Returns a record of the ClassificationAttribute
[**get_linked_items_for_classification_attribute_item**](ClassificationAttributeApi.md#get_linked_items_for_classification_attribute_item) | **GET** /ClassificationAttribute/{id}/{link} | Returns linked entities for the ClassificationAttribute
[**get_list_of_classification_attribute_items**](ClassificationAttributeApi.md#get_list_of_classification_attribute_items) | **GET** /ClassificationAttribute | Returns a collection of ClassificationAttribute records
[**link_classification_attribute**](ClassificationAttributeApi.md#link_classification_attribute) | **POST** /ClassificationAttribute/{id}/{link} | Link ClassificationAttribute to Entities
[**mass_delete_classification_attribute**](ClassificationAttributeApi.md#mass_delete_classification_attribute) | **POST** /ClassificationAttribute/action/massDelete | Mass delete of ClassificationAttribute data
[**mass_update_classification_attribute**](ClassificationAttributeApi.md#mass_update_classification_attribute) | **PUT** /ClassificationAttribute/action/massUpdate | Mass update of ClassificationAttribute data
[**remove_relation_for_classification_attribute**](ClassificationAttributeApi.md#remove_relation_for_classification_attribute) | **DELETE** /ClassificationAttribute/{link}/relation | Remove relation for ClassificationAttribute
[**unfollow_classification_attribute**](ClassificationAttributeApi.md#unfollow_classification_attribute) | **DELETE** /ClassificationAttribute/{id}/subscription | Unfollow the ClassificationAttribute stream
[**unlink_classification_attribute**](ClassificationAttributeApi.md#unlink_classification_attribute) | **DELETE** /ClassificationAttribute/{id}/{link} | Unlink ClassificationAttribute from Entities
[**update_classification_attribute_item**](ClassificationAttributeApi.md#update_classification_attribute_item) | **PUT** /ClassificationAttribute/{id} | Update a record of the ClassificationAttribute


# **add_relation_for_classification_attribute**
> bool add_relation_for_classification_attribute(link, ids, foreign_ids)

Add relation for ClassificationAttribute

Add relation for ClassificationAttribute

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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Add relation for ClassificationAttribute
        api_response = api_instance.add_relation_for_classification_attribute(link, ids, foreign_ids)
        print("The response of ClassificationAttributeApi->add_relation_for_classification_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->add_relation_for_classification_attribute: %s\n" % e)
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

# **create_classification_attribute_item**
> ClassificationAttribute create_classification_attribute_item(create_classification_attribute_item_request)

Create a record of the ClassificationAttribute

Create a record of the ClassificationAttribute

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.classification_attribute import ClassificationAttribute
from clientapi_atrocore.models.create_classification_attribute_item_request import CreateClassificationAttributeItemRequest
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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    create_classification_attribute_item_request = clientapi_atrocore.CreateClassificationAttributeItemRequest() # CreateClassificationAttributeItemRequest | 

    try:
        # Create a record of the ClassificationAttribute
        api_response = api_instance.create_classification_attribute_item(create_classification_attribute_item_request)
        print("The response of ClassificationAttributeApi->create_classification_attribute_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->create_classification_attribute_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_classification_attribute_item_request** | [**CreateClassificationAttributeItemRequest**](CreateClassificationAttributeItemRequest.md)|  | 

### Return type

[**ClassificationAttribute**](ClassificationAttribute.md)

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

# **delete_classification_attribute_item**
> bool delete_classification_attribute_item(id)

Delete a record of the ClassificationAttribute

Delete a record of the ClassificationAttribute

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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a record of the ClassificationAttribute
        api_response = api_instance.delete_classification_attribute_item(id)
        print("The response of ClassificationAttributeApi->delete_classification_attribute_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->delete_classification_attribute_item: %s\n" % e)
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

# **follow_classification_attribute**
> FollowAccount200Response follow_classification_attribute(id)

Follow the ClassificationAttribute stream

Follow the ClassificationAttribute stream

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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Follow the ClassificationAttribute stream
        api_response = api_instance.follow_classification_attribute(id)
        print("The response of ClassificationAttributeApi->follow_classification_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->follow_classification_attribute: %s\n" % e)
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

# **get_classification_attribute_item**
> ClassificationAttribute get_classification_attribute_item(id, language=language)

Returns a record of the ClassificationAttribute

Returns a record of the ClassificationAttribute

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.classification_attribute import ClassificationAttribute
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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    id = 'id_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns a record of the ClassificationAttribute
        api_response = api_instance.get_classification_attribute_item(id, language=language)
        print("The response of ClassificationAttributeApi->get_classification_attribute_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->get_classification_attribute_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 

### Return type

[**ClassificationAttribute**](ClassificationAttribute.md)

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

# **get_linked_items_for_classification_attribute_item**
> GetLinkedItemsForAccountItem200Response get_linked_items_for_classification_attribute_item(id, link, language=language)

Returns linked entities for the ClassificationAttribute

Returns linked entities for the ClassificationAttribute

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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns linked entities for the ClassificationAttribute
        api_response = api_instance.get_linked_items_for_classification_attribute_item(id, link, language=language)
        print("The response of ClassificationAttributeApi->get_linked_items_for_classification_attribute_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->get_linked_items_for_classification_attribute_item: %s\n" % e)
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

# **get_list_of_classification_attribute_items**
> GetListOfClassificationAttributeItems200Response get_list_of_classification_attribute_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)

Returns a collection of ClassificationAttribute records

Returns a collection of ClassificationAttribute records

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.get_list_of_classification_attribute_items200_response import GetListOfClassificationAttributeItems200Response
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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)
    select = 'name,createdAt' # str | Available fields: assignedUser, assignedUserId, assignedUserName, attribute, attributeExtensibleEnumId, attributeGroupId, attributeGroupName, attributeId, attributeName, attributeNameDeDe, attributeType, attribute_amountOfDigitsAfterComma, attribute_assetType, attribute_assignedUser, attribute_assignedUserId, attribute_assignedUserName, attribute_attributeGroup, attribute_attributeGroupId, attribute_attributeGroupName, attribute_attributeTab, attribute_attributeTabId, attribute_attributeTabName, attribute_code, attribute_countBytesInsteadOfCharacters, attribute_createdAt, attribute_createdBy, attribute_createdById, attribute_createdByName, attribute_data, attribute_defaultChannel, attribute_defaultChannelId, attribute_defaultChannelName, attribute_defaultScope, attribute_defaultUnit, attribute_description, attribute_descriptionDeDe, attribute_extensibleEnum, attribute_extensibleEnumId, attribute_extensibleEnumName, attribute_filterCreateImportJob, attribute_filterUpdateImportJob, attribute_hasChildren, attribute_hierarchyRoute, attribute_hierarchySortOrder, attribute_inheritedFields, attribute_isMultilang, attribute_isRequired, attribute_isRoot, attribute_max, attribute_maxLength, attribute_measure, attribute_measureId, attribute_measureName, attribute_min, attribute_modifiedAt, attribute_modifiedBy, attribute_modifiedById, attribute_modifiedByName, attribute_name, attribute_nameDeDe, attribute_ownerUser, attribute_ownerUserId, attribute_ownerUserName, attribute_pattern, attribute_prohibitedEmptyValue, attribute_sortOrder, attribute_sortOrderInAttributeGroup, attribute_sortOrderInProduct, attribute_tooltip, attribute_tooltipDeDe, attribute_type, attribute_unique, attribute_useDisabledTextareaInViewMode, attribute_virtualProductField, boolValue, channel, channelId, channelName, classification, classificationId, classificationName, classification_assignedUser, classification_assignedUserId, classification_assignedUserName, classification_code, classification_createdAt, classification_createdBy, classification_createdById, classification_createdByName, classification_description, classification_descriptionDeDe, classification_filterCreateImportJob, classification_filterUpdateImportJob, classification_isActive, classification_modifiedAt, classification_modifiedBy, classification_modifiedById, classification_modifiedByName, classification_name, classification_nameDeDe, classification_ownerUser, classification_ownerUserId, classification_ownerUserName, classification_release, classification_synonyms, classification_synonymsDeDe, countBytesInsteadOfCharacters, createdAt, createdBy, createdById, createdByName, data, dateValue, datetimeValue, deleted, filterCreateImportJob, filterUpdateImportJob, floatValue, floatValue1, id, intValue, intValue1, isInherited, isRequired, language, languages, max, maxLength, min, modifiedAt, modifiedBy, modifiedById, modifiedByName, name, ownerUser, ownerUserId, ownerUserName, scope, sortOrder, teams, teamsIds, teamsNames, textValue, value, valueAllUnits, valueCurrency, valueFrom, valueId, valueName, valueNames, valueOptionData, valueOptionsData, valuePathsData, valueTo, valueUnit, valueUnitId, varcharValue (optional)
    where = None # List[object] | There are a lot of filter types supported. You can learn all of them if you trace what's requested by Atro UI in the network tab in your browser console (press F12 key to open the console). (optional)
    offset = 0 # int |  (optional)
    max_size = 50 # int |  (optional)
    sort_by = 'name' # str |  (optional)
    asc = true # bool |  (optional)

    try:
        # Returns a collection of ClassificationAttribute records
        api_response = api_instance.get_list_of_classification_attribute_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)
        print("The response of ClassificationAttributeApi->get_list_of_classification_attribute_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->get_list_of_classification_attribute_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 
 **select** | **str**| Available fields: assignedUser, assignedUserId, assignedUserName, attribute, attributeExtensibleEnumId, attributeGroupId, attributeGroupName, attributeId, attributeName, attributeNameDeDe, attributeType, attribute_amountOfDigitsAfterComma, attribute_assetType, attribute_assignedUser, attribute_assignedUserId, attribute_assignedUserName, attribute_attributeGroup, attribute_attributeGroupId, attribute_attributeGroupName, attribute_attributeTab, attribute_attributeTabId, attribute_attributeTabName, attribute_code, attribute_countBytesInsteadOfCharacters, attribute_createdAt, attribute_createdBy, attribute_createdById, attribute_createdByName, attribute_data, attribute_defaultChannel, attribute_defaultChannelId, attribute_defaultChannelName, attribute_defaultScope, attribute_defaultUnit, attribute_description, attribute_descriptionDeDe, attribute_extensibleEnum, attribute_extensibleEnumId, attribute_extensibleEnumName, attribute_filterCreateImportJob, attribute_filterUpdateImportJob, attribute_hasChildren, attribute_hierarchyRoute, attribute_hierarchySortOrder, attribute_inheritedFields, attribute_isMultilang, attribute_isRequired, attribute_isRoot, attribute_max, attribute_maxLength, attribute_measure, attribute_measureId, attribute_measureName, attribute_min, attribute_modifiedAt, attribute_modifiedBy, attribute_modifiedById, attribute_modifiedByName, attribute_name, attribute_nameDeDe, attribute_ownerUser, attribute_ownerUserId, attribute_ownerUserName, attribute_pattern, attribute_prohibitedEmptyValue, attribute_sortOrder, attribute_sortOrderInAttributeGroup, attribute_sortOrderInProduct, attribute_tooltip, attribute_tooltipDeDe, attribute_type, attribute_unique, attribute_useDisabledTextareaInViewMode, attribute_virtualProductField, boolValue, channel, channelId, channelName, classification, classificationId, classificationName, classification_assignedUser, classification_assignedUserId, classification_assignedUserName, classification_code, classification_createdAt, classification_createdBy, classification_createdById, classification_createdByName, classification_description, classification_descriptionDeDe, classification_filterCreateImportJob, classification_filterUpdateImportJob, classification_isActive, classification_modifiedAt, classification_modifiedBy, classification_modifiedById, classification_modifiedByName, classification_name, classification_nameDeDe, classification_ownerUser, classification_ownerUserId, classification_ownerUserName, classification_release, classification_synonyms, classification_synonymsDeDe, countBytesInsteadOfCharacters, createdAt, createdBy, createdById, createdByName, data, dateValue, datetimeValue, deleted, filterCreateImportJob, filterUpdateImportJob, floatValue, floatValue1, id, intValue, intValue1, isInherited, isRequired, language, languages, max, maxLength, min, modifiedAt, modifiedBy, modifiedById, modifiedByName, name, ownerUser, ownerUserId, ownerUserName, scope, sortOrder, teams, teamsIds, teamsNames, textValue, value, valueAllUnits, valueCurrency, valueFrom, valueId, valueName, valueNames, valueOptionData, valueOptionsData, valuePathsData, valueTo, valueUnit, valueUnitId, varcharValue | [optional] 
 **where** | [**List[object]**](object.md)| There are a lot of filter types supported. You can learn all of them if you trace what&#39;s requested by Atro UI in the network tab in your browser console (press F12 key to open the console). | [optional] 
 **offset** | **int**|  | [optional] 
 **max_size** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **asc** | **bool**|  | [optional] 

### Return type

[**GetListOfClassificationAttributeItems200Response**](GetListOfClassificationAttributeItems200Response.md)

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

# **link_classification_attribute**
> bool link_classification_attribute(id, link, link_account_request)

Link ClassificationAttribute to Entities

Link ClassificationAttribute to Entities

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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Link ClassificationAttribute to Entities
        api_response = api_instance.link_classification_attribute(id, link, link_account_request)
        print("The response of ClassificationAttributeApi->link_classification_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->link_classification_attribute: %s\n" % e)
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

# **mass_delete_classification_attribute**
> bool mass_delete_classification_attribute(link_account_request)

Mass delete of ClassificationAttribute data

Mass delete of ClassificationAttribute data

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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Mass delete of ClassificationAttribute data
        api_response = api_instance.mass_delete_classification_attribute(link_account_request)
        print("The response of ClassificationAttributeApi->mass_delete_classification_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->mass_delete_classification_attribute: %s\n" % e)
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

# **mass_update_classification_attribute**
> bool mass_update_classification_attribute(mass_update_account_request)

Mass update of ClassificationAttribute data

Mass update of ClassificationAttribute data

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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    mass_update_account_request = clientapi_atrocore.MassUpdateAccountRequest() # MassUpdateAccountRequest | 

    try:
        # Mass update of ClassificationAttribute data
        api_response = api_instance.mass_update_classification_attribute(mass_update_account_request)
        print("The response of ClassificationAttributeApi->mass_update_classification_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->mass_update_classification_attribute: %s\n" % e)
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

# **remove_relation_for_classification_attribute**
> bool remove_relation_for_classification_attribute(link, ids, foreign_ids)

Remove relation for ClassificationAttribute

Remove relation for ClassificationAttribute

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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Remove relation for ClassificationAttribute
        api_response = api_instance.remove_relation_for_classification_attribute(link, ids, foreign_ids)
        print("The response of ClassificationAttributeApi->remove_relation_for_classification_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->remove_relation_for_classification_attribute: %s\n" % e)
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

# **unfollow_classification_attribute**
> bool unfollow_classification_attribute(id)

Unfollow the ClassificationAttribute stream

Unfollow the ClassificationAttribute stream

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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unfollow the ClassificationAttribute stream
        api_response = api_instance.unfollow_classification_attribute(id)
        print("The response of ClassificationAttributeApi->unfollow_classification_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->unfollow_classification_attribute: %s\n" % e)
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

# **unlink_classification_attribute**
> bool unlink_classification_attribute(id, link, ids)

Unlink ClassificationAttribute from Entities

Unlink ClassificationAttribute from Entities

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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 

    try:
        # Unlink ClassificationAttribute from Entities
        api_response = api_instance.unlink_classification_attribute(id, link, ids)
        print("The response of ClassificationAttributeApi->unlink_classification_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->unlink_classification_attribute: %s\n" % e)
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

# **update_classification_attribute_item**
> ClassificationAttribute update_classification_attribute_item(id, create_classification_attribute_item_request)

Update a record of the ClassificationAttribute

Update a record of the ClassificationAttribute

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.classification_attribute import ClassificationAttribute
from clientapi_atrocore.models.create_classification_attribute_item_request import CreateClassificationAttributeItemRequest
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
    api_instance = clientapi_atrocore.ClassificationAttributeApi(api_client)
    id = 'id_example' # str | 
    create_classification_attribute_item_request = clientapi_atrocore.CreateClassificationAttributeItemRequest() # CreateClassificationAttributeItemRequest | 

    try:
        # Update a record of the ClassificationAttribute
        api_response = api_instance.update_classification_attribute_item(id, create_classification_attribute_item_request)
        print("The response of ClassificationAttributeApi->update_classification_attribute_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassificationAttributeApi->update_classification_attribute_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_classification_attribute_item_request** | [**CreateClassificationAttributeItemRequest**](CreateClassificationAttributeItemRequest.md)|  | 

### Return type

[**ClassificationAttribute**](ClassificationAttribute.md)

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

