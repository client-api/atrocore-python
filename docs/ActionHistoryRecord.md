# ActionHistoryRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**number** | **int** |  | [optional] 
**target_id** | **str** |  | [optional] 
**target_name** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**action** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**auth_token_id** | **str** |  | [optional] 
**auth_token_name** | **str** |  | [optional] 
**auth_log_record_id** | **str** |  | [optional] 
**auth_log_record_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.action_history_record import ActionHistoryRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ActionHistoryRecord from a JSON string
action_history_record_instance = ActionHistoryRecord.from_json(json)
# print the JSON string representation of the object
print ActionHistoryRecord.to_json()

# convert the object into a dict
action_history_record_dict = action_history_record_instance.to_dict()
# create an instance of ActionHistoryRecord from a dict
action_history_record_form_dict = action_history_record.from_dict(action_history_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


