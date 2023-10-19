# CreateAssetItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**asset_categories_ids** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_de_de** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**file_id** | **str** |  | [optional] 
**files** | **str** |  | 
**size** | **str** |  | [optional] 
**parents_ids** | **List[str]** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_asset_item_request import CreateAssetItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetItemRequest from a JSON string
create_asset_item_request_instance = CreateAssetItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateAssetItemRequest.to_json()

# convert the object into a dict
create_asset_item_request_dict = create_asset_item_request_instance.to_dict()
# create an instance of CreateAssetItemRequest from a dict
create_asset_item_request_form_dict = create_asset_item_request.from_dict(create_asset_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


