# CreateAssetTypeItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_de_de** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**assign_automatically** | **bool** |  | [optional] 
**types_to_exclude** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_asset_type_item_request import CreateAssetTypeItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssetTypeItemRequest from a JSON string
create_asset_type_item_request_instance = CreateAssetTypeItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateAssetTypeItemRequest.to_json()

# convert the object into a dict
create_asset_type_item_request_dict = create_asset_type_item_request_instance.to_dict()
# create an instance of CreateAssetTypeItemRequest from a dict
create_asset_type_item_request_form_dict = create_asset_type_item_request.from_dict(create_asset_type_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


