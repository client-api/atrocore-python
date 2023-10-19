# CreateUserItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**password_confirm** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_portal_user** | **bool** |  | [optional] 
**is_super_admin** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**email_address** | **str** |  | 
**phone_number** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**auth_token_id** | **str** |  | [optional] 
**auth_log_record_id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**default_team_id** | **str** |  | [optional] 
**acceptance_status** | **str** |  | [optional] 
**team_role** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**roles_ids** | **List[str]** |  | [optional] 
**portal_id** | **str** |  | [optional] 
**portal_roles_ids** | **List[str]** |  | [optional] 
**avatar_id** | **str** |  | [optional] 
**send_access_info** | **bool** |  | [optional] 
**gender** | **str** |  | [optional] 
**last_access** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_user_item_request import CreateUserItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserItemRequest from a JSON string
create_user_item_request_instance = CreateUserItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateUserItemRequest.to_json()

# convert the object into a dict
create_user_item_request_dict = create_user_item_request_instance.to_dict()
# create an instance of CreateUserItemRequest from a dict
create_user_item_request_form_dict = create_user_item_request.from_dict(create_user_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


