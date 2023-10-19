# NextNumber


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**field_name** | **str** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.next_number import NextNumber

# TODO update the JSON string below
json = "{}"
# create an instance of NextNumber from a JSON string
next_number_instance = NextNumber.from_json(json)
# print the JSON string representation of the object
print NextNumber.to_json()

# convert the object into a dict
next_number_dict = next_number_instance.to_dict()
# create an instance of NextNumber from a dict
next_number_form_dict = next_number.from_dict(next_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


