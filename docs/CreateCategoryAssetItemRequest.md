# CreateCategoryAssetItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**is_main_image** | **bool** |  | [optional] 
**sorting** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**preview** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_category_asset_item_request import CreateCategoryAssetItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCategoryAssetItemRequest from a JSON string
create_category_asset_item_request_instance = CreateCategoryAssetItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateCategoryAssetItemRequest.to_json()

# convert the object into a dict
create_category_asset_item_request_dict = create_category_asset_item_request_instance.to_dict()
# create an instance of CreateCategoryAssetItemRequest from a dict
create_category_asset_item_request_form_dict = create_category_asset_item_request.from_dict(create_category_asset_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


