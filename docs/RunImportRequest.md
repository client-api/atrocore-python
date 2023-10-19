# RunImportRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_feed_id** | **str** |  | [optional] 
**attachment_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.run_import_request import RunImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunImportRequest from a JSON string
run_import_request_instance = RunImportRequest.from_json(json)
# print the JSON string representation of the object
print RunImportRequest.to_json()

# convert the object into a dict
run_import_request_dict = run_import_request_instance.to_dict()
# create an instance of RunImportRequest from a dict
run_import_request_form_dict = run_import_request.from_dict(run_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


