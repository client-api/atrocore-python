# CreateAssetCategoryItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**assets_ids** | **List[str]** |  | [optional] 
**parents_ids** | **List[str]** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_asset_category_item_request import CreateAssetCategoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetCategoryItemRequest from a JSON string
create_asset_category_item_request_instance = CreateAssetCategoryItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateAssetCategoryItemRequest.to_json()

# convert the object into a dict
create_asset_category_item_request_dict = create_asset_category_item_request_instance.to_dict()
# create an instance of CreateAssetCategoryItemRequest from a dict
create_asset_category_item_request_form_dict = create_asset_category_item_request.from_dict(create_asset_category_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


