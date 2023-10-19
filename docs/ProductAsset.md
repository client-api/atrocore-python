# ProductAsset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**product_id** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**asset_name** | **str** |  | [optional] 
**is_main_image** | **bool** |  | [optional] 
**sorting** | **int** |  | [optional] 
**scope** | **str** |  | 
**channel_id** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
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
from clientapi_atrocore.models.product_asset import ProductAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAsset from a JSON string
product_asset_instance = ProductAsset.from_json(json)
# print the JSON string representation of the object
print ProductAsset.to_json()

# convert the object into a dict
product_asset_dict = product_asset_instance.to_dict()
# create an instance of ProductAsset from a dict
product_asset_form_dict = product_asset.from_dict(product_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


