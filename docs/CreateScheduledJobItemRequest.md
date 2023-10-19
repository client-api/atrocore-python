# CreateScheduledJobItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**job** | **str** |  | 
**status** | **str** |  | 
**scheduling** | **str** |  | 
**last_run** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**is_internal** | **bool** |  | [optional] 
**minimum_age** | **int** |  | [optional] 
**import_feed_id** | **str** |  | [optional] 
**import_feeds_ids** | **List[str]** |  | [optional] 
**maximum_hours_to_look_back** | **str** |  | [optional] 
**export_feed_id** | **str** |  | [optional] 
**export_feeds_ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_scheduled_job_item_request import CreateScheduledJobItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduledJobItemRequest from a JSON string
create_scheduled_job_item_request_instance = CreateScheduledJobItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateScheduledJobItemRequest.to_json()

# convert the object into a dict
create_scheduled_job_item_request_dict = create_scheduled_job_item_request_instance.to_dict()
# create an instance of CreateScheduledJobItemRequest from a dict
create_scheduled_job_item_request_form_dict = create_scheduled_job_item_request.from_dict(create_scheduled_job_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


