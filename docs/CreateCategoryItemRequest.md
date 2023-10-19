# CreateCategoryItemRequest


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
**children_count** | **int** |  | [optional] 
**category_parent_id** | **str** |  | [optional] 
**category_route** | **str** |  | [optional] 
**has_children** | **bool** |  | [optional] 
**sorting** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_category_item_request import CreateCategoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCategoryItemRequest from a JSON string
create_category_item_request_instance = CreateCategoryItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateCategoryItemRequest.to_json()

# convert the object into a dict
create_category_item_request_dict = create_category_item_request_instance.to_dict()
# create an instance of CreateCategoryItemRequest from a dict
create_category_item_request_form_dict = create_category_item_request.from_dict(create_category_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


