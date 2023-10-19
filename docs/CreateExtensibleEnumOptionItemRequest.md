# CreateExtensibleEnumOptionItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**name_de_de** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**extensible_enum_id** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_extensible_enum_option_item_request import CreateExtensibleEnumOptionItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExtensibleEnumOptionItemRequest from a JSON string
create_extensible_enum_option_item_request_instance = CreateExtensibleEnumOptionItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateExtensibleEnumOptionItemRequest.to_json()

# convert the object into a dict
create_extensible_enum_option_item_request_dict = create_extensible_enum_option_item_request_instance.to_dict()
# create an instance of CreateExtensibleEnumOptionItemRequest from a dict
create_extensible_enum_option_item_request_form_dict = create_extensible_enum_option_item_request.from_dict(create_extensible_enum_option_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


