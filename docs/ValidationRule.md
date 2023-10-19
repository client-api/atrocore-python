# ValidationRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**asset_type_id** | **str** |  | [optional] 
**asset_type_name** | **str** |  | [optional] 
**type** | **str** |  | 
**ratio** | **str** |  | [optional] 
**validate_by** | **str** |  | 
**pattern** | **str** |  | [optional] 
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 
**color_depth** | **List[str]** |  | [optional] 
**color_space** | **List[str]** |  | [optional] 
**min_width** | **int** |  | [optional] 
**min_height** | **int** |  | [optional] 
**extension** | **List[str]** |  | [optional] 
**mime_list** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.validation_rule import ValidationRule

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationRule from a JSON string
validation_rule_instance = ValidationRule.from_json(json)
# print the JSON string representation of the object
print ValidationRule.to_json()

# convert the object into a dict
validation_rule_dict = validation_rule_instance.to_dict()
# create an instance of ValidationRule from a dict
validation_rule_form_dict = validation_rule.from_dict(validation_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


