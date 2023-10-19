# AssetType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**name_de_de** | **str** |  | 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**assign_automatically** | **bool** |  | [optional] 
**types_to_exclude** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.asset_type import AssetType

# TODO update the JSON string below
json = "{}"
# create an instance of AssetType from a JSON string
asset_type_instance = AssetType.from_json(json)
# print the JSON string representation of the object
print AssetType.to_json()

# convert the object into a dict
asset_type_dict = asset_type_instance.to_dict()
# create an instance of AssetType from a dict
asset_type_form_dict = asset_type.from_dict(asset_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


