# Job


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**queue_item_id** | **str** |  | [optional] 
**queue_item_name** | **str** |  | [optional] 
**name** | **str** |  | 
**status** | **str** |  | [optional] 
**execute_time** | **str** |  | 
**service_name** | **str** |  | 
**method** | **str** |  | 
**method_name** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**scheduled_job_id** | **str** |  | [optional] 
**scheduled_job_name** | **str** |  | [optional] 
**scheduled_job_job** | **str** |  | [optional] 
**pid** | **int** |  | [optional] 
**attempts** | **int** |  | [optional] 
**target_id** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 
**failed_attempts** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print Job.to_json()

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_form_dict = job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


