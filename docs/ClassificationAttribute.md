# ClassificationAttribute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**classification_id** | **str** |  | [optional] 
**classification_name** | **str** |  | [optional] 
**attribute_id** | **str** |  | [optional] 
**attribute_name** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**languages** | **str** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**scope** | **str** |  | 
**channel_id** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
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
from clientapi_atrocore.models.classification_attribute import ClassificationAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ClassificationAttribute from a JSON string
classification_attribute_instance = ClassificationAttribute.from_json(json)
# print the JSON string representation of the object
print ClassificationAttribute.to_json()

# convert the object into a dict
classification_attribute_dict = classification_attribute_instance.to_dict()
# create an instance of ClassificationAttribute from a dict
classification_attribute_form_dict = classification_attribute.from_dict(classification_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


