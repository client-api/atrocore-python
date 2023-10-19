# Asset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**preview** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**after_save_message** | **str** |  | [optional] 
**height** | **int** |  | [optional] 
**width** | **int** |  | [optional] 
**color_space** | **str** |  | [optional] 
**color_depth** | **str** |  | [optional] 
**orientation** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**library_id** | **str** |  | [optional] 
**library_name** | **str** |  | [optional] 
**asset_categories_ids** | **List[str]** |  | [optional] 
**asset_categories_names** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_de_de** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**file_id** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**files** | **str** |  | 
**size** | **str** |  | [optional] 
**parents_ids** | **List[str]** |  | [optional] 
**parents_names** | **object** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.asset import Asset

# TODO update the JSON string below
json = "{}"
# create an instance of Asset from a JSON string
asset_instance = Asset.from_json(json)
# print the JSON string representation of the object
print Asset.to_json()

# convert the object into a dict
asset_dict = asset_instance.to_dict()
# create an instance of Asset from a dict
asset_form_dict = asset.from_dict(asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


