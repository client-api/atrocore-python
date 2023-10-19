# ImportJobLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**import_job_id** | **str** |  | [optional] 
**import_job_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**entity_name** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**row_number** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.import_job_log import ImportJobLog

# TODO update the JSON string below
json = "{}"
# create an instance of ImportJobLog from a JSON string
import_job_log_instance = ImportJobLog.from_json(json)
# print the JSON string representation of the object
print ImportJobLog.to_json()

# convert the object into a dict
import_job_log_dict = import_job_log_instance.to_dict()
# create an instance of ImportJobLog from a dict
import_job_log_form_dict = import_job_log.from_dict(import_job_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


