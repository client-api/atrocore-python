# AttributeGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**name_de_de** | **str** |  | 
**description** | **str** |  | [optional] 
**description_de_de** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**owner_user_name** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**assigned_user_name** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**teams_names** | **object** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.attribute_group import AttributeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeGroup from a JSON string
attribute_group_instance = AttributeGroup.from_json(json)
# print the JSON string representation of the object
print AttributeGroup.to_json()

# convert the object into a dict
attribute_group_dict = attribute_group_instance.to_dict()
# create an instance of AttributeGroup from a dict
attribute_group_form_dict = attribute_group.from_dict(attribute_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


