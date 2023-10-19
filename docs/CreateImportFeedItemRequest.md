# CreateImportFeedItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**max_per_job** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**repeat_processing** | **str** |  | 
**type** | **str** |  | 
**data** | **object** |  | [optional] 
**file_id** | **str** |  | [optional] 
**sheet** | **int** |  | [optional] 
**file_field_delimiter** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**file_text_qualifier** | **str** |  | [optional] 
**file_data_action** | **str** |  | [optional] 
**is_file_header_row** | **bool** |  | [optional] 
**decimal_mark** | **str** |  | 
**thousand_separator** | **str** |  | [optional] 
**adapter** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**entity** | **str** |  | 
**excluded_nodes** | **List[str]** |  | [optional] 
**kept_string_nodes** | **List[str]** |  | [optional] 
**delimiter** | **str** |  | 
**field_delimiter_for_relation** | **str** |  | 
**empty_value** | **str** |  | [optional] 
**null_value** | **str** |  | [optional] 
**mark_for_no_relation** | **str** |  | [optional] 
**source_fields** | **List[str]** |  | [optional] 
**connection_id** | **str** |  | [optional] 
**last_time** | **str** |  | [optional] 
**assigned_accounts_ids** | **List[str]** |  | [optional] 
**last_status** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_import_feed_item_request import CreateImportFeedItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImportFeedItemRequest from a JSON string
create_import_feed_item_request_instance = CreateImportFeedItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateImportFeedItemRequest.to_json()

# convert the object into a dict
create_import_feed_item_request_dict = create_import_feed_item_request_instance.to_dict()
# create an instance of CreateImportFeedItemRequest from a dict
create_import_feed_item_request_form_dict = create_import_feed_item_request.from_dict(create_import_feed_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


