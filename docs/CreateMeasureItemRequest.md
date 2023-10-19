# CreateMeasureItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_de_de** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_measure_item_request import CreateMeasureItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMeasureItemRequest from a JSON string
create_measure_item_request_instance = CreateMeasureItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateMeasureItemRequest.to_json()

# convert the object into a dict
create_measure_item_request_dict = create_measure_item_request_instance.to_dict()
# create an instance of CreateMeasureItemRequest from a dict
create_measure_item_request_form_dict = create_measure_item_request.from_dict(create_measure_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


