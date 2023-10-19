# CreateImportJobItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**trial** | **int** |  | [optional] 
**import_feed_id** | **str** |  | [optional] 
**sort_order** | **str** |  | [optional] 
**state** | **str** |  | 
**message** | **str** |  | [optional] 
**start** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**created_count** | **int** |  | [optional] 
**updated_count** | **int** |  | [optional] 
**deleted_count** | **int** |  | [optional] 
**errors_count** | **int** |  | [optional] 
**attachment_id** | **str** |  | [optional] 
**uploaded_file_id** | **str** |  | [optional] 
**converted_file_id** | **str** |  | [optional] 
**errors_attachment_id** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_import_job_item_request import CreateImportJobItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImportJobItemRequest from a JSON string
create_import_job_item_request_instance = CreateImportJobItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateImportJobItemRequest.to_json()

# convert the object into a dict
create_import_job_item_request_dict = create_import_job_item_request_instance.to_dict()
# create an instance of CreateImportJobItemRequest from a dict
create_import_job_item_request_form_dict = create_import_job_item_request.from_dict(create_import_job_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


