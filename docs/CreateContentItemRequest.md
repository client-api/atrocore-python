# CreateContentItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**meta_title** | **str** |  | [optional] 
**meta_description** | **str** |  | [optional] 
**products_ids** | **List[str]** |  | [optional] 
**content_group_id** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_content_item_request import CreateContentItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContentItemRequest from a JSON string
create_content_item_request_instance = CreateContentItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateContentItemRequest.to_json()

# convert the object into a dict
create_content_item_request_dict = create_content_item_request_instance.to_dict()
# create an instance of CreateContentItemRequest from a dict
create_content_item_request_form_dict = create_content_item_request.from_dict(create_content_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


