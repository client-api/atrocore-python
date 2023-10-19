# AssetCategory


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
**code** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**assets_ids** | **List[str]** |  | [optional] 
**assets_names** | **object** |  | [optional] 
**parents_ids** | **List[str]** |  | [optional] 
**parents_names** | **object** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.asset_category import AssetCategory

# TODO update the JSON string below
json = "{}"
# create an instance of AssetCategory from a JSON string
asset_category_instance = AssetCategory.from_json(json)
# print the JSON string representation of the object
print AssetCategory.to_json()

# convert the object into a dict
asset_category_dict = asset_category_instance.to_dict()
# create an instance of AssetCategory from a dict
asset_category_form_dict = asset_category.from_dict(asset_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


