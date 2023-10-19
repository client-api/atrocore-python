# Library


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**assigned_user_name** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**teams_names** | **object** |  | [optional] 
**code** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**owner_user_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.library import Library

# TODO update the JSON string below
json = "{}"
# create an instance of Library from a JSON string
library_instance = Library.from_json(json)
# print the JSON string representation of the object
print Library.to_json()

# convert the object into a dict
library_dict = library_instance.to_dict()
# create an instance of Library from a dict
library_form_dict = library.from_dict(library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


