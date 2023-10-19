# CreateAttributeGroupItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_de_de** | **str** |  | 
**description** | **str** |  | [optional] 
**description_de_de** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_attribute_group_item_request import CreateAttributeGroupItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAttributeGroupItemRequest from a JSON string
create_attribute_group_item_request_instance = CreateAttributeGroupItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateAttributeGroupItemRequest.to_json()

# convert the object into a dict
create_attribute_group_item_request_dict = create_attribute_group_item_request_instance.to_dict()
# create an instance of CreateAttributeGroupItemRequest from a dict
create_attribute_group_item_request_form_dict = create_attribute_group_item_request.from_dict(create_attribute_group_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


