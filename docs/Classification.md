# Classification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**name_de_de** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_de_de** | **str** |  | [optional] 
**synonyms** | **List[str]** |  | [optional] 
**synonyms_de_de** | **List[str]** |  | [optional] 
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

## Example

```python
from clientapi_atrocore.models.classification import Classification

# TODO update the JSON string below
json = "{}"
# create an instance of Classification from a JSON string
classification_instance = Classification.from_json(json)
# print the JSON string representation of the object
print Classification.to_json()

# convert the object into a dict
classification_dict = classification_instance.to_dict()
# create an instance of Classification from a dict
classification_form_dict = classification.from_dict(classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


