# CreateLibraryItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**code** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_library_item_request import CreateLibraryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLibraryItemRequest from a JSON string
create_library_item_request_instance = CreateLibraryItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateLibraryItemRequest.to_json()

# convert the object into a dict
create_library_item_request_dict = create_library_item_request_instance.to_dict()
# create an instance of CreateLibraryItemRequest from a dict
create_library_item_request_form_dict = create_library_item_request.from_dict(create_library_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


