# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**is_admin** | **bool** |  | [optional] 
**user_name** | **str** |  | 
**name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**password_confirm** | **str** |  | [optional] 
**salutation_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | 
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
**default_team_name** | **str** |  | [optional] 
**acceptance_status** | **str** |  | [optional] 
**team_role** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**teams_names** | **object** |  | [optional] 
**roles_ids** | **List[str]** |  | [optional] 
**roles_names** | **object** |  | [optional] 
**portal_id** | **str** |  | [optional] 
**portal_name** | **str** |  | [optional] 
**portal_roles_ids** | **List[str]** |  | [optional] 
**portal_roles_names** | **object** |  | [optional] 
**avatar_id** | **str** |  | [optional] 
**avatar_name** | **str** |  | [optional] 
**send_access_info** | **bool** |  | [optional] 
**gender** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**last_access** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


