# ScheduledJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**job** | **str** |  | 
**status** | **str** |  | 
**scheduling** | **str** |  | 
**last_run** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**is_internal** | **bool** |  | [optional] 
**minimum_age** | **int** |  | [optional] 
**import_feed_id** | **str** |  | [optional] 
**import_feed_name** | **str** |  | [optional] 
**import_feeds_ids** | **List[str]** |  | [optional] 
**import_feeds_names** | **object** |  | [optional] 
**maximum_hours_to_look_back** | **str** |  | [optional] 
**export_feed_id** | **str** |  | [optional] 
**export_feed_name** | **str** |  | [optional] 
**export_feeds_ids** | **List[str]** |  | [optional] 
**export_feeds_names** | **object** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.scheduled_job import ScheduledJob

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledJob from a JSON string
scheduled_job_instance = ScheduledJob.from_json(json)
# print the JSON string representation of the object
print ScheduledJob.to_json()

# convert the object into a dict
scheduled_job_dict = scheduled_job_instance.to_dict()
# create an instance of ScheduledJob from a dict
scheduled_job_form_dict = scheduled_job.from_dict(scheduled_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


