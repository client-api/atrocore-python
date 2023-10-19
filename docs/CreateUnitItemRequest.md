# CreateUnitItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_de_de** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_de_de** | **str** |  | [optional] 
**measure_id** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**multiplier** | **str** |  | 
**convert_to_id** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_unit_item_request import CreateUnitItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUnitItemRequest from a JSON string
create_unit_item_request_instance = CreateUnitItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateUnitItemRequest.to_json()

# convert the object into a dict
create_unit_item_request_dict = create_unit_item_request_instance.to_dict()
# create an instance of CreateUnitItemRequest from a dict
create_unit_item_request_form_dict = create_unit_item_request.from_dict(create_unit_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


