# CreateImportJobLogItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**import_job_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**row_number** | **int** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_import_job_log_item_request import CreateImportJobLogItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImportJobLogItemRequest from a JSON string
create_import_job_log_item_request_instance = CreateImportJobLogItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateImportJobLogItemRequest.to_json()

# convert the object into a dict
create_import_job_log_item_request_dict = create_import_job_log_item_request_instance.to_dict()
# create an instance of CreateImportJobLogItemRequest from a dict
create_import_job_log_item_request_form_dict = create_import_job_log_item_request.from_dict(create_import_job_log_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


