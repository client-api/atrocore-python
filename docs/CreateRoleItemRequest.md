# CreateRoleItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**assignment_permission** | **str** |  | [optional] 
**portal_permission** | **str** |  | [optional] 
**data_privacy_permission** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**field_data** | **object** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_role_item_request import CreateRoleItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoleItemRequest from a JSON string
create_role_item_request_instance = CreateRoleItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateRoleItemRequest.to_json()

# convert the object into a dict
create_role_item_request_dict = create_role_item_request_instance.to_dict()
# create an instance of CreateRoleItemRequest from a dict
create_role_item_request_form_dict = create_role_item_request.from_dict(create_role_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


