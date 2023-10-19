# AuthToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**token** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**portal_id** | **str** |  | [optional] 
**portal_name** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**last_access** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**lifetime** | **int** |  | [optional] 
**idle_time** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.auth_token import AuthToken

# TODO update the JSON string below
json = "{}"
# create an instance of AuthToken from a JSON string
auth_token_instance = AuthToken.from_json(json)
# print the JSON string representation of the object
print AuthToken.to_json()

# convert the object into a dict
auth_token_dict = auth_token_instance.to_dict()
# create an instance of AuthToken from a dict
auth_token_form_dict = auth_token.from_dict(auth_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


