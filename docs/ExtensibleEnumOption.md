# ExtensibleEnumOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**name_de_de** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**extensible_enum_id** | **str** |  | [optional] 
**extensible_enum_name** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.extensible_enum_option import ExtensibleEnumOption

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensibleEnumOption from a JSON string
extensible_enum_option_instance = ExtensibleEnumOption.from_json(json)
# print the JSON string representation of the object
print ExtensibleEnumOption.to_json()

# convert the object into a dict
extensible_enum_option_dict = extensible_enum_option_instance.to_dict()
# create an instance of ExtensibleEnumOption from a dict
extensible_enum_option_form_dict = extensible_enum_option.from_dict(extensible_enum_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


