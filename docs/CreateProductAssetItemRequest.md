# CreateProductAssetItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**is_main_image** | **bool** |  | [optional] 
**sorting** | **int** |  | [optional] 
**scope** | **str** |  | 
**channel_id** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**preview** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_product_asset_item_request import CreateProductAssetItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductAssetItemRequest from a JSON string
create_product_asset_item_request_instance = CreateProductAssetItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateProductAssetItemRequest.to_json()

# convert the object into a dict
create_product_asset_item_request_dict = create_product_asset_item_request_instance.to_dict()
# create an instance of CreateProductAssetItemRequest from a dict
create_product_asset_item_request_form_dict = create_product_asset_item_request.from_dict(create_product_asset_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


