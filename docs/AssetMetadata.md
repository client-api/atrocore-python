# AssetMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**value** | **str** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**asset_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.asset_metadata import AssetMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AssetMetadata from a JSON string
asset_metadata_instance = AssetMetadata.from_json(json)
# print the JSON string representation of the object
print AssetMetadata.to_json()

# convert the object into a dict
asset_metadata_dict = asset_metadata_instance.to_dict()
# create an instance of AssetMetadata from a dict
asset_metadata_form_dict = asset_metadata.from_dict(asset_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


