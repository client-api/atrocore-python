# ImportJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**trial** | **int** |  | [optional] 
**import_feed_id** | **str** |  | [optional] 
**import_feed_name** | **str** |  | [optional] 
**sort_order** | **str** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**state** | **str** |  | 
**message** | **str** |  | [optional] 
**start** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**created_count** | **int** |  | [optional] 
**updated_count** | **int** |  | [optional] 
**deleted_count** | **int** |  | [optional] 
**errors_count** | **int** |  | [optional] 
**attachment_id** | **str** |  | [optional] 
**attachment_name** | **str** |  | [optional] 
**uploaded_file_id** | **str** |  | [optional] 
**uploaded_file_name** | **str** |  | [optional] 
**converted_file_id** | **str** |  | [optional] 
**converted_file_name** | **str** |  | [optional] 
**errors_attachment_id** | **str** |  | [optional] 
**errors_attachment_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.import_job import ImportJob

# TODO update the JSON string below
json = "{}"
# create an instance of ImportJob from a JSON string
import_job_instance = ImportJob.from_json(json)
# print the JSON string representation of the object
print ImportJob.to_json()

# convert the object into a dict
import_job_dict = import_job_instance.to_dict()
# create an instance of ImportJob from a dict
import_job_form_dict = import_job.from_dict(import_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


