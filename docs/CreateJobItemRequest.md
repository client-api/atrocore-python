# CreateJobItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue_item_id** | **str** |  | [optional] 
**name** | **str** |  | 
**status** | **str** |  | [optional] 
**execute_time** | **str** |  | 
**method** | **str** |  | 
**data** | **object** |  | [optional] 
**scheduled_job_id** | **str** |  | [optional] 
**scheduled_job_job** | **str** |  | [optional] 
**pid** | **int** |  | [optional] 
**attempts** | **int** |  | [optional] 
**target_id** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 
**failed_attempts** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_job_item_request import CreateJobItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobItemRequest from a JSON string
create_job_item_request_instance = CreateJobItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateJobItemRequest.to_json()

# convert the object into a dict
create_job_item_request_dict = create_job_item_request_instance.to_dict()
# create an instance of CreateJobItemRequest from a dict
create_job_item_request_form_dict = create_job_item_request.from_dict(create_job_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


