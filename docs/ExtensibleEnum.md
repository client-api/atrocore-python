# ExtensibleEnum


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**multilingual** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.extensible_enum import ExtensibleEnum

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensibleEnum from a JSON string
extensible_enum_instance = ExtensibleEnum.from_json(json)
# print the JSON string representation of the object
print ExtensibleEnum.to_json()

# convert the object into a dict
extensible_enum_dict = extensible_enum_instance.to_dict()
# create an instance of ExtensibleEnum from a dict
extensible_enum_form_dict = extensible_enum.from_dict(extensible_enum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


