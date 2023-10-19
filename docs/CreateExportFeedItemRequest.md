# CreateExportFeedItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**limit** | **int** |  | 
**separate_job** | **bool** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**language** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**file_type** | **str** |  | 
**is_file_header_row** | **bool** |  | [optional] 
**csv_field_delimiter** | **str** |  | [optional] 
**csv_text_qualifier** | **str** |  | [optional] 
**entity** | **str** |  | [optional] 
**convert_collection_to_string** | **bool** |  | [optional] 
**delimiter** | **str** |  | [optional] 
**replace_attribute_values** | **bool** |  | [optional] 
**convert_relations_to_string** | **bool** |  | [optional] 
**field_delimiter_for_relation** | **str** |  | [optional] 
**empty_value** | **str** |  | [optional] 
**null_value** | **str** |  | [optional] 
**mark_for_no_relation** | **str** |  | [optional] 
**decimal_mark** | **str** |  | [optional] 
**thousand_separator** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**sort_order_field** | **str** |  | [optional] 
**sort_order_direction** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**last_time** | **str** |  | [optional] 
**export_by_max_depth** | **str** |  | [optional] 
**assigned_accounts_ids** | **List[str]** |  | [optional] 
**last_status** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_export_feed_item_request import CreateExportFeedItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExportFeedItemRequest from a JSON string
create_export_feed_item_request_instance = CreateExportFeedItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateExportFeedItemRequest.to_json()

# convert the object into a dict
create_export_feed_item_request_dict = create_export_feed_item_request_instance.to_dict()
# create an instance of CreateExportFeedItemRequest from a dict
create_export_feed_item_request_form_dict = create_export_feed_item_request.from_dict(create_export_feed_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


