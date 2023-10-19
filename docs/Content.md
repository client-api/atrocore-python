# Content


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**meta_title** | **str** |  | [optional] 
**meta_description** | **str** |  | [optional] 
**products_ids** | **List[str]** |  | [optional] 
**products_names** | **object** |  | [optional] 
**content_group_id** | **str** |  | [optional] 
**content_group_name** | **str** |  | [optional] 
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

## Example

```python
from clientapi_atrocore.models.content import Content

# TODO update the JSON string below
json = "{}"
# create an instance of Content from a JSON string
content_instance = Content.from_json(json)
# print the JSON string representation of the object
print Content.to_json()

# convert the object into a dict
content_dict = content_instance.to_dict()
# create an instance of Content from a dict
content_form_dict = content.from_dict(content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


