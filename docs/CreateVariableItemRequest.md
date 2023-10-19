# CreateVariableItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**type** | **str** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_variable_item_request import CreateVariableItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVariableItemRequest from a JSON string
create_variable_item_request_instance = CreateVariableItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateVariableItemRequest.to_json()

# convert the object into a dict
create_variable_item_request_dict = create_variable_item_request_instance.to_dict()
# create an instance of CreateVariableItemRequest from a dict
create_variable_item_request_form_dict = create_variable_item_request.from_dict(create_variable_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


