# CreateValidationRuleItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**asset_type_id** | **str** |  | [optional] 
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
from clientapi_atrocore.models.create_validation_rule_item_request import CreateValidationRuleItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateValidationRuleItemRequest from a JSON string
create_validation_rule_item_request_instance = CreateValidationRuleItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateValidationRuleItemRequest.to_json()

# convert the object into a dict
create_validation_rule_item_request_dict = create_validation_rule_item_request_instance.to_dict()
# create an instance of CreateValidationRuleItemRequest from a dict
create_validation_rule_item_request_form_dict = create_validation_rule_item_request.from_dict(create_validation_rule_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


