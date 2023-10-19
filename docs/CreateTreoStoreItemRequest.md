# CreateTreoStoreItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**package_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**versions** | **object** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_treo_store_item_request import CreateTreoStoreItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTreoStoreItemRequest from a JSON string
create_treo_store_item_request_instance = CreateTreoStoreItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateTreoStoreItemRequest.to_json()

# convert the object into a dict
create_treo_store_item_request_dict = create_treo_store_item_request_instance.to_dict()
# create an instance of CreateTreoStoreItemRequest from a dict
create_treo_store_item_request_form_dict = create_treo_store_item_request.from_dict(create_treo_store_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


