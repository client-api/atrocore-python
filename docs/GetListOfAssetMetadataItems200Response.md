# GetListOfAssetMetadataItems200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**list** | [**List[AssetMetadata]**](AssetMetadata.md) |  | [optional] 

## Example

```python
from clientapi_atrocore.models.get_list_of_asset_metadata_items200_response import GetListOfAssetMetadataItems200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetListOfAssetMetadataItems200Response from a JSON string
get_list_of_asset_metadata_items200_response_instance = GetListOfAssetMetadataItems200Response.from_json(json)
# print the JSON string representation of the object
print GetListOfAssetMetadataItems200Response.to_json()

# convert the object into a dict
get_list_of_asset_metadata_items200_response_dict = get_list_of_asset_metadata_items200_response_instance.to_dict()
# create an instance of GetListOfAssetMetadataItems200Response from a dict
get_list_of_asset_metadata_items200_response_form_dict = get_list_of_asset_metadata_items200_response.from_dict(get_list_of_asset_metadata_items200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


