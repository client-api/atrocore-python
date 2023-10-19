# CreateAuthLogRecordItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**portal_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**auth_token_id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**is_denied** | **bool** |  | [optional] 
**denial_reason** | **str** |  | [optional] 
**request_time** | **str** |  | [optional] 
**request_url** | **str** |  | [optional] 
**request_method** | **str** |  | [optional] 
**auth_token_is_active** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_auth_log_record_item_request import CreateAuthLogRecordItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthLogRecordItemRequest from a JSON string
create_auth_log_record_item_request_instance = CreateAuthLogRecordItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateAuthLogRecordItemRequest.to_json()

# convert the object into a dict
create_auth_log_record_item_request_dict = create_auth_log_record_item_request_instance.to_dict()
# create an instance of CreateAuthLogRecordItemRequest from a dict
create_auth_log_record_item_request_form_dict = create_auth_log_record_item_request.from_dict(create_auth_log_record_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


