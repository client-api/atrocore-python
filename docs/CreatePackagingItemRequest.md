# CreatePackagingItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**products_ids** | **List[str]** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_packaging_item_request import CreatePackagingItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePackagingItemRequest from a JSON string
create_packaging_item_request_instance = CreatePackagingItemRequest.from_json(json)
# print the JSON string representation of the object
print CreatePackagingItemRequest.to_json()

# convert the object into a dict
create_packaging_item_request_dict = create_packaging_item_request_instance.to_dict()
# create an instance of CreatePackagingItemRequest from a dict
create_packaging_item_request_form_dict = create_packaging_item_request.from_dict(create_packaging_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


