# CreateAuthTokenItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**portal_id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**last_access** | **str** |  | [optional] 
**lifetime** | **int** |  | [optional] 
**idle_time** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_auth_token_item_request import CreateAuthTokenItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthTokenItemRequest from a JSON string
create_auth_token_item_request_instance = CreateAuthTokenItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateAuthTokenItemRequest.to_json()

# convert the object into a dict
create_auth_token_item_request_dict = create_auth_token_item_request_instance.to_dict()
# create an instance of CreateAuthTokenItemRequest from a dict
create_auth_token_item_request_form_dict = create_auth_token_item_request.from_dict(create_auth_token_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


