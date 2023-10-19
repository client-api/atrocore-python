# CreateScheduledJobLogRecordItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**status** | **str** |  | [optional] 
**execution_time** | **str** |  | [optional] 
**scheduled_job_id** | **str** |  | [optional] 
**target_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_scheduled_job_log_record_item_request import CreateScheduledJobLogRecordItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduledJobLogRecordItemRequest from a JSON string
create_scheduled_job_log_record_item_request_instance = CreateScheduledJobLogRecordItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateScheduledJobLogRecordItemRequest.to_json()

# convert the object into a dict
create_scheduled_job_log_record_item_request_dict = create_scheduled_job_log_record_item_request_instance.to_dict()
# create an instance of CreateScheduledJobLogRecordItemRequest from a dict
create_scheduled_job_log_record_item_request_form_dict = create_scheduled_job_log_record_item_request.from_dict(create_scheduled_job_log_record_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


