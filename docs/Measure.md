# Measure


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**name_de_de** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.measure import Measure

# TODO update the JSON string below
json = "{}"
# create an instance of Measure from a JSON string
measure_instance = Measure.from_json(json)
# print the JSON string representation of the object
print Measure.to_json()

# convert the object into a dict
measure_dict = measure_instance.to_dict()
# create an instance of Measure from a dict
measure_form_dict = measure.from_dict(measure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


