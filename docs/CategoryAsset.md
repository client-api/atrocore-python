# CategoryAsset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**category_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**asset_name** | **str** |  | [optional] 
**is_main_image** | **bool** |  | [optional] 
**sorting** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**preview** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.category_asset import CategoryAsset

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAsset from a JSON string
category_asset_instance = CategoryAsset.from_json(json)
# print the JSON string representation of the object
print CategoryAsset.to_json()

# convert the object into a dict
category_asset_dict = category_asset_instance.to_dict()
# create an instance of CategoryAsset from a dict
category_asset_form_dict = category_asset.from_dict(category_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


