# clientapi_atrocore.ScheduledJobLogRecordApi

All URIs are relative to *https://demo.atropim.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation_for_scheduled_job_log_record**](ScheduledJobLogRecordApi.md#add_relation_for_scheduled_job_log_record) | **POST** /ScheduledJobLogRecord/{link}/relation | Add relation for ScheduledJobLogRecord
[**create_scheduled_job_log_record_item**](ScheduledJobLogRecordApi.md#create_scheduled_job_log_record_item) | **POST** /ScheduledJobLogRecord | Create a record of the ScheduledJobLogRecord
[**delete_scheduled_job_log_record_item**](ScheduledJobLogRecordApi.md#delete_scheduled_job_log_record_item) | **DELETE** /ScheduledJobLogRecord/{id} | Delete a record of the ScheduledJobLogRecord
[**follow_scheduled_job_log_record**](ScheduledJobLogRecordApi.md#follow_scheduled_job_log_record) | **PUT** /ScheduledJobLogRecord/{id}/subscription | Follow the ScheduledJobLogRecord stream
[**get_linked_items_for_scheduled_job_log_record_item**](ScheduledJobLogRecordApi.md#get_linked_items_for_scheduled_job_log_record_item) | **GET** /ScheduledJobLogRecord/{id}/{link} | Returns linked entities for the ScheduledJobLogRecord
[**get_list_of_scheduled_job_log_record_items**](ScheduledJobLogRecordApi.md#get_list_of_scheduled_job_log_record_items) | **GET** /ScheduledJobLogRecord | Returns a collection of ScheduledJobLogRecord records
[**get_scheduled_job_log_record_item**](ScheduledJobLogRecordApi.md#get_scheduled_job_log_record_item) | **GET** /ScheduledJobLogRecord/{id} | Returns a record of the ScheduledJobLogRecord
[**link_scheduled_job_log_record**](ScheduledJobLogRecordApi.md#link_scheduled_job_log_record) | **POST** /ScheduledJobLogRecord/{id}/{link} | Link ScheduledJobLogRecord to Entities
[**mass_delete_scheduled_job_log_record**](ScheduledJobLogRecordApi.md#mass_delete_scheduled_job_log_record) | **POST** /ScheduledJobLogRecord/action/massDelete | Mass delete of ScheduledJobLogRecord data
[**mass_update_scheduled_job_log_record**](ScheduledJobLogRecordApi.md#mass_update_scheduled_job_log_record) | **PUT** /ScheduledJobLogRecord/action/massUpdate | Mass update of ScheduledJobLogRecord data
[**remove_relation_for_scheduled_job_log_record**](ScheduledJobLogRecordApi.md#remove_relation_for_scheduled_job_log_record) | **DELETE** /ScheduledJobLogRecord/{link}/relation | Remove relation for ScheduledJobLogRecord
[**unfollow_scheduled_job_log_record**](ScheduledJobLogRecordApi.md#unfollow_scheduled_job_log_record) | **DELETE** /ScheduledJobLogRecord/{id}/subscription | Unfollow the ScheduledJobLogRecord stream
[**unlink_scheduled_job_log_record**](ScheduledJobLogRecordApi.md#unlink_scheduled_job_log_record) | **DELETE** /ScheduledJobLogRecord/{id}/{link} | Unlink ScheduledJobLogRecord from Entities
[**update_scheduled_job_log_record_item**](ScheduledJobLogRecordApi.md#update_scheduled_job_log_record_item) | **PUT** /ScheduledJobLogRecord/{id} | Update a record of the ScheduledJobLogRecord


# **add_relation_for_scheduled_job_log_record**
> bool add_relation_for_scheduled_job_log_record(link, ids, foreign_ids)

Add relation for ScheduledJobLogRecord

Add relation for ScheduledJobLogRecord

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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Add relation for ScheduledJobLogRecord
        api_response = api_instance.add_relation_for_scheduled_job_log_record(link, ids, foreign_ids)
        print("The response of ScheduledJobLogRecordApi->add_relation_for_scheduled_job_log_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->add_relation_for_scheduled_job_log_record: %s\n" % e)
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

# **create_scheduled_job_log_record_item**
> ScheduledJobLogRecord create_scheduled_job_log_record_item(create_scheduled_job_log_record_item_request)

Create a record of the ScheduledJobLogRecord

Create a record of the ScheduledJobLogRecord

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.create_scheduled_job_log_record_item_request import CreateScheduledJobLogRecordItemRequest
from clientapi_atrocore.models.scheduled_job_log_record import ScheduledJobLogRecord
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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    create_scheduled_job_log_record_item_request = clientapi_atrocore.CreateScheduledJobLogRecordItemRequest() # CreateScheduledJobLogRecordItemRequest | 

    try:
        # Create a record of the ScheduledJobLogRecord
        api_response = api_instance.create_scheduled_job_log_record_item(create_scheduled_job_log_record_item_request)
        print("The response of ScheduledJobLogRecordApi->create_scheduled_job_log_record_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->create_scheduled_job_log_record_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_scheduled_job_log_record_item_request** | [**CreateScheduledJobLogRecordItemRequest**](CreateScheduledJobLogRecordItemRequest.md)|  | 

### Return type

[**ScheduledJobLogRecord**](ScheduledJobLogRecord.md)

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

# **delete_scheduled_job_log_record_item**
> bool delete_scheduled_job_log_record_item(id)

Delete a record of the ScheduledJobLogRecord

Delete a record of the ScheduledJobLogRecord

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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a record of the ScheduledJobLogRecord
        api_response = api_instance.delete_scheduled_job_log_record_item(id)
        print("The response of ScheduledJobLogRecordApi->delete_scheduled_job_log_record_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->delete_scheduled_job_log_record_item: %s\n" % e)
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

# **follow_scheduled_job_log_record**
> FollowAccount200Response follow_scheduled_job_log_record(id)

Follow the ScheduledJobLogRecord stream

Follow the ScheduledJobLogRecord stream

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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    id = 'id_example' # str | 

    try:
        # Follow the ScheduledJobLogRecord stream
        api_response = api_instance.follow_scheduled_job_log_record(id)
        print("The response of ScheduledJobLogRecordApi->follow_scheduled_job_log_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->follow_scheduled_job_log_record: %s\n" % e)
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

# **get_linked_items_for_scheduled_job_log_record_item**
> GetLinkedItemsForAccountItem200Response get_linked_items_for_scheduled_job_log_record_item(id, link, language=language)

Returns linked entities for the ScheduledJobLogRecord

Returns linked entities for the ScheduledJobLogRecord

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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns linked entities for the ScheduledJobLogRecord
        api_response = api_instance.get_linked_items_for_scheduled_job_log_record_item(id, link, language=language)
        print("The response of ScheduledJobLogRecordApi->get_linked_items_for_scheduled_job_log_record_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->get_linked_items_for_scheduled_job_log_record_item: %s\n" % e)
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

# **get_list_of_scheduled_job_log_record_items**
> GetListOfScheduledJobLogRecordItems200Response get_list_of_scheduled_job_log_record_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)

Returns a collection of ScheduledJobLogRecord records

Returns a collection of ScheduledJobLogRecord records

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.get_list_of_scheduled_job_log_record_items200_response import GetListOfScheduledJobLogRecordItems200Response
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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)
    select = 'name,createdAt' # str | Available fields: createdAt, deleted, executionTime, filterCreateImportJob, filterUpdateImportJob, id, name, scheduledJob, scheduledJobId, scheduledJobName, status, targetId, targetName, targetType (optional)
    where = None # List[object] | There are a lot of filter types supported. You can learn all of them if you trace what's requested by Atro UI in the network tab in your browser console (press F12 key to open the console). (optional)
    offset = 0 # int |  (optional)
    max_size = 50 # int |  (optional)
    sort_by = 'name' # str |  (optional)
    asc = true # bool |  (optional)

    try:
        # Returns a collection of ScheduledJobLogRecord records
        api_response = api_instance.get_list_of_scheduled_job_log_record_items(language=language, select=select, where=where, offset=offset, max_size=max_size, sort_by=sort_by, asc=asc)
        print("The response of ScheduledJobLogRecordApi->get_list_of_scheduled_job_log_record_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->get_list_of_scheduled_job_log_record_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 
 **select** | **str**| Available fields: createdAt, deleted, executionTime, filterCreateImportJob, filterUpdateImportJob, id, name, scheduledJob, scheduledJobId, scheduledJobName, status, targetId, targetName, targetType | [optional] 
 **where** | [**List[object]**](object.md)| There are a lot of filter types supported. You can learn all of them if you trace what&#39;s requested by Atro UI in the network tab in your browser console (press F12 key to open the console). | [optional] 
 **offset** | **int**|  | [optional] 
 **max_size** | **int**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **asc** | **bool**|  | [optional] 

### Return type

[**GetListOfScheduledJobLogRecordItems200Response**](GetListOfScheduledJobLogRecordItems200Response.md)

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

# **get_scheduled_job_log_record_item**
> ScheduledJobLogRecord get_scheduled_job_log_record_item(id, language=language)

Returns a record of the ScheduledJobLogRecord

Returns a record of the ScheduledJobLogRecord

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.scheduled_job_log_record import ScheduledJobLogRecord
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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    id = 'id_example' # str | 
    language = 'language_example' # str | Set this parameter for data to be returned for a specified language (optional)

    try:
        # Returns a record of the ScheduledJobLogRecord
        api_response = api_instance.get_scheduled_job_log_record_item(id, language=language)
        print("The response of ScheduledJobLogRecordApi->get_scheduled_job_log_record_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->get_scheduled_job_log_record_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **language** | **str**| Set this parameter for data to be returned for a specified language | [optional] 

### Return type

[**ScheduledJobLogRecord**](ScheduledJobLogRecord.md)

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

# **link_scheduled_job_log_record**
> bool link_scheduled_job_log_record(id, link, link_account_request)

Link ScheduledJobLogRecord to Entities

Link ScheduledJobLogRecord to Entities

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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Link ScheduledJobLogRecord to Entities
        api_response = api_instance.link_scheduled_job_log_record(id, link, link_account_request)
        print("The response of ScheduledJobLogRecordApi->link_scheduled_job_log_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->link_scheduled_job_log_record: %s\n" % e)
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

# **mass_delete_scheduled_job_log_record**
> bool mass_delete_scheduled_job_log_record(link_account_request)

Mass delete of ScheduledJobLogRecord data

Mass delete of ScheduledJobLogRecord data

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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    link_account_request = clientapi_atrocore.LinkAccountRequest() # LinkAccountRequest | 

    try:
        # Mass delete of ScheduledJobLogRecord data
        api_response = api_instance.mass_delete_scheduled_job_log_record(link_account_request)
        print("The response of ScheduledJobLogRecordApi->mass_delete_scheduled_job_log_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->mass_delete_scheduled_job_log_record: %s\n" % e)
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

# **mass_update_scheduled_job_log_record**
> bool mass_update_scheduled_job_log_record(mass_update_account_request)

Mass update of ScheduledJobLogRecord data

Mass update of ScheduledJobLogRecord data

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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    mass_update_account_request = clientapi_atrocore.MassUpdateAccountRequest() # MassUpdateAccountRequest | 

    try:
        # Mass update of ScheduledJobLogRecord data
        api_response = api_instance.mass_update_scheduled_job_log_record(mass_update_account_request)
        print("The response of ScheduledJobLogRecordApi->mass_update_scheduled_job_log_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->mass_update_scheduled_job_log_record: %s\n" % e)
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

# **remove_relation_for_scheduled_job_log_record**
> bool remove_relation_for_scheduled_job_log_record(link, ids, foreign_ids)

Remove relation for ScheduledJobLogRecord

Remove relation for ScheduledJobLogRecord

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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 
    foreign_ids = ['foreign_ids_example'] # List[str] | 

    try:
        # Remove relation for ScheduledJobLogRecord
        api_response = api_instance.remove_relation_for_scheduled_job_log_record(link, ids, foreign_ids)
        print("The response of ScheduledJobLogRecordApi->remove_relation_for_scheduled_job_log_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->remove_relation_for_scheduled_job_log_record: %s\n" % e)
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

# **unfollow_scheduled_job_log_record**
> bool unfollow_scheduled_job_log_record(id)

Unfollow the ScheduledJobLogRecord stream

Unfollow the ScheduledJobLogRecord stream

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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unfollow the ScheduledJobLogRecord stream
        api_response = api_instance.unfollow_scheduled_job_log_record(id)
        print("The response of ScheduledJobLogRecordApi->unfollow_scheduled_job_log_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->unfollow_scheduled_job_log_record: %s\n" % e)
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

# **unlink_scheduled_job_log_record**
> bool unlink_scheduled_job_log_record(id, link, ids)

Unlink ScheduledJobLogRecord from Entities

Unlink ScheduledJobLogRecord from Entities

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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    id = 'id_example' # str | 
    link = 'link_example' # str | 
    ids = ['ids_example'] # List[str] | 

    try:
        # Unlink ScheduledJobLogRecord from Entities
        api_response = api_instance.unlink_scheduled_job_log_record(id, link, ids)
        print("The response of ScheduledJobLogRecordApi->unlink_scheduled_job_log_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->unlink_scheduled_job_log_record: %s\n" % e)
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

# **update_scheduled_job_log_record_item**
> ScheduledJobLogRecord update_scheduled_job_log_record_item(id, create_scheduled_job_log_record_item_request)

Update a record of the ScheduledJobLogRecord

Update a record of the ScheduledJobLogRecord

### Example

* Api Key Authentication (Authorization-Token):
```python
import time
import os
import clientapi_atrocore
from clientapi_atrocore.models.create_scheduled_job_log_record_item_request import CreateScheduledJobLogRecordItemRequest
from clientapi_atrocore.models.scheduled_job_log_record import ScheduledJobLogRecord
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
    api_instance = clientapi_atrocore.ScheduledJobLogRecordApi(api_client)
    id = 'id_example' # str | 
    create_scheduled_job_log_record_item_request = clientapi_atrocore.CreateScheduledJobLogRecordItemRequest() # CreateScheduledJobLogRecordItemRequest | 

    try:
        # Update a record of the ScheduledJobLogRecord
        api_response = api_instance.update_scheduled_job_log_record_item(id, create_scheduled_job_log_record_item_request)
        print("The response of ScheduledJobLogRecordApi->update_scheduled_job_log_record_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledJobLogRecordApi->update_scheduled_job_log_record_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **create_scheduled_job_log_record_item_request** | [**CreateScheduledJobLogRecordItemRequest**](CreateScheduledJobLogRecordItemRequest.md)|  | 

### Return type

[**ScheduledJobLogRecord**](ScheduledJobLogRecord.md)

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

