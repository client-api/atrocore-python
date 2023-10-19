# Category


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
**position** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**children_count** | **int** |  | [optional] 
**category_parent_id** | **str** |  | [optional] 
**category_parent_name** | **str** |  | [optional] 
**category_route** | **str** |  | [optional] 
**category_route_name** | **str** |  | [optional] 
**has_children** | **bool** |  | [optional] 
**sorting** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.category import Category

# TODO update the JSON string below
json = "{}"
# create an instance of Category from a JSON string
category_instance = Category.from_json(json)
# print the JSON string representation of the object
print Category.to_json()

# convert the object into a dict
category_dict = category_instance.to_dict()
# create an instance of Category from a dict
category_form_dict = category.from_dict(category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


