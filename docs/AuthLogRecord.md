# AuthLogRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**username** | **str** |  | [optional] 
**portal_id** | **str** |  | [optional] 
**portal_name** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**auth_token_id** | **str** |  | [optional] 
**auth_token_name** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**is_denied** | **bool** |  | [optional] 
**denial_reason** | **str** |  | [optional] 
**request_time** | **str** |  | [optional] 
**request_url** | **str** |  | [optional] 
**request_method** | **str** |  | [optional] 
**auth_token_is_active** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.auth_log_record import AuthLogRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AuthLogRecord from a JSON string
auth_log_record_instance = AuthLogRecord.from_json(json)
# print the JSON string representation of the object
print AuthLogRecord.to_json()

# convert the object into a dict
auth_log_record_dict = auth_log_record_instance.to_dict()
# create an instance of AuthLogRecord from a dict
auth_log_record_form_dict = auth_log_record.from_dict(auth_log_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


