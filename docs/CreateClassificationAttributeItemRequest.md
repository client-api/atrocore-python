# CreateClassificationAttributeItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification_id** | **str** |  | [optional] 
**attribute_id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**languages** | **str** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**scope** | **str** |  | 
**channel_id** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_classification_attribute_item_request import CreateClassificationAttributeItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClassificationAttributeItemRequest from a JSON string
create_classification_attribute_item_request_instance = CreateClassificationAttributeItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateClassificationAttributeItemRequest.to_json()

# convert the object into a dict
create_classification_attribute_item_request_dict = create_classification_attribute_item_request_instance.to_dict()
# create an instance of CreateClassificationAttributeItemRequest from a dict
create_classification_attribute_item_request_form_dict = create_classification_attribute_item_request.from_dict(create_classification_attribute_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


