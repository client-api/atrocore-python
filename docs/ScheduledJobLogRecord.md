# ScheduledJobLogRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**status** | **str** |  | [optional] 
**execution_time** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**scheduled_job_id** | **str** |  | [optional] 
**scheduled_job_name** | **str** |  | [optional] 
**target_id** | **str** |  | [optional] 
**target_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.scheduled_job_log_record import ScheduledJobLogRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledJobLogRecord from a JSON string
scheduled_job_log_record_instance = ScheduledJobLogRecord.from_json(json)
# print the JSON string representation of the object
print ScheduledJobLogRecord.to_json()

# convert the object into a dict
scheduled_job_log_record_dict = scheduled_job_log_record_instance.to_dict()
# create an instance of ScheduledJobLogRecord from a dict
scheduled_job_log_record_form_dict = scheduled_job_log_record.from_dict(scheduled_job_log_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


