# CreateTaxItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_de_de** | **str** |  | 
**value** | **str** |  | 
**is_active** | **bool** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**products_ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_tax_item_request import CreateTaxItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTaxItemRequest from a JSON string
create_tax_item_request_instance = CreateTaxItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateTaxItemRequest.to_json()

# convert the object into a dict
create_tax_item_request_dict = create_tax_item_request_instance.to_dict()
# create an instance of CreateTaxItemRequest from a dict
create_tax_item_request_form_dict = create_tax_item_request.from_dict(create_tax_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


