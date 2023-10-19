# CreateSharingItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**available** | **bool** |  | [optional] 
**entity_type** | **str** |  | 
**entity_id** | **str** |  | 
**type** | **str** |  | 
**valid_till** | **str** |  | [optional] 
**allowed_usage** | **int** |  | [optional] 
**used** | **int** |  | [optional] 
**link** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_sharing_item_request import CreateSharingItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSharingItemRequest from a JSON string
create_sharing_item_request_instance = CreateSharingItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateSharingItemRequest.to_json()

# convert the object into a dict
create_sharing_item_request_dict = create_sharing_item_request_instance.to_dict()
# create an instance of CreateSharingItemRequest from a dict
create_sharing_item_request_form_dict = create_sharing_item_request.from_dict(create_sharing_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


