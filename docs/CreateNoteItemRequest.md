# CreateNoteItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**related_id** | **str** |  | [optional] 
**attachments** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**is_global** | **bool** |  | [optional] 
**created_by_gender** | **str** |  | [optional] 
**notified_user_id_list** | **object** |  | [optional] 
**is_internal** | **bool** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**attribute_id** | **str** |  | [optional] 
**pav_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_note_item_request import CreateNoteItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNoteItemRequest from a JSON string
create_note_item_request_instance = CreateNoteItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateNoteItemRequest.to_json()

# convert the object into a dict
create_note_item_request_dict = create_note_item_request_instance.to_dict()
# create an instance of CreateNoteItemRequest from a dict
create_note_item_request_form_dict = create_note_item_request.from_dict(create_note_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


