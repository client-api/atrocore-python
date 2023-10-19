# CreateClassificationItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**name_de_de** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_de_de** | **str** |  | [optional] 
**synonyms** | **List[str]** |  | [optional] 
**synonyms_de_de** | **List[str]** |  | [optional] 
**code** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_classification_item_request import CreateClassificationItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClassificationItemRequest from a JSON string
create_classification_item_request_instance = CreateClassificationItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateClassificationItemRequest.to_json()

# convert the object into a dict
create_classification_item_request_dict = create_classification_item_request_instance.to_dict()
# create an instance of CreateClassificationItemRequest from a dict
create_classification_item_request_form_dict = create_classification_item_request.from_dict(create_classification_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


