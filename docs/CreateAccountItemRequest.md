# CreateAccountItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**assigned_import_feeds_ids** | **List[str]** |  | [optional] 
**assigned_export_feeds_ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_account_item_request import CreateAccountItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountItemRequest from a JSON string
create_account_item_request_instance = CreateAccountItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateAccountItemRequest.to_json()

# convert the object into a dict
create_account_item_request_dict = create_account_item_request_instance.to_dict()
# create an instance of CreateAccountItemRequest from a dict
create_account_item_request_form_dict = create_account_item_request.from_dict(create_account_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


