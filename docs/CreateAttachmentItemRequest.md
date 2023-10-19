# CreateAttachmentItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**size** | **str** |  | [optional] 
**field** | **str** |  | [optional] 
**contents** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**storage** | **str** |  | [optional] 
**storage_file_path** | **str** |  | [optional] 
**storage_thumb_path** | **str** |  | [optional] 
**var_global** | **bool** |  | [optional] 
**md5** | **str** |  | [optional] 
**paths_data** | **object** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_attachment_item_request import CreateAttachmentItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAttachmentItemRequest from a JSON string
create_attachment_item_request_instance = CreateAttachmentItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateAttachmentItemRequest.to_json()

# convert the object into a dict
create_attachment_item_request_dict = create_attachment_item_request_instance.to_dict()
# create an instance of CreateAttachmentItemRequest from a dict
create_attachment_item_request_form_dict = create_attachment_item_request.from_dict(create_attachment_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


