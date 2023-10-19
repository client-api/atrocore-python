# CreateContentGroupItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**contents_ids** | **List[str]** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_content_group_item_request import CreateContentGroupItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContentGroupItemRequest from a JSON string
create_content_group_item_request_instance = CreateContentGroupItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateContentGroupItemRequest.to_json()

# convert the object into a dict
create_content_group_item_request_dict = create_content_group_item_request_instance.to_dict()
# create an instance of CreateContentGroupItemRequest from a dict
create_content_group_item_request_form_dict = create_content_group_item_request.from_dict(create_content_group_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


