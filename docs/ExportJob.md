# ExportJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**trial** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**export_feed_id** | **str** |  | [optional] 
**export_feed_name** | **str** |  | [optional] 
**file_id** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**state** | **str** |  | 
**state_message** | **str** |  | [optional] 
**start** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**editable** | **bool** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**owner_user_name** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**assigned_user_name** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**teams_names** | **object** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.export_job import ExportJob

# TODO update the JSON string below
json = "{}"
# create an instance of ExportJob from a JSON string
export_job_instance = ExportJob.from_json(json)
# print the JSON string representation of the object
print ExportJob.to_json()

# convert the object into a dict
export_job_dict = export_job_instance.to_dict()
# create an instance of ExportJob from a dict
export_job_form_dict = export_job.from_dict(export_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


