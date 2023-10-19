# CreateExportJobItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**trial** | **int** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**export_feed_id** | **str** |  | [optional] 
**file_id** | **str** |  | [optional] 
**state** | **str** |  | 
**state_message** | **str** |  | [optional] 
**start** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**editable** | **bool** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_export_job_item_request import CreateExportJobItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExportJobItemRequest from a JSON string
create_export_job_item_request_instance = CreateExportJobItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateExportJobItemRequest.to_json()

# convert the object into a dict
create_export_job_item_request_dict = create_export_job_item_request_instance.to_dict()
# create an instance of CreateExportJobItemRequest from a dict
create_export_job_item_request_form_dict = create_export_job_item_request.from_dict(create_export_job_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


