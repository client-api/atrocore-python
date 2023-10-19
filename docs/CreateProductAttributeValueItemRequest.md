# CreateProductAttributeValueItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | [optional] 
**attribute_id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**scope** | **str** |  | 
**channel_id** | **str** |  | [optional] 
**is_variant_specific_attribute** | **bool** |  | [optional] 
**count_bytes_instead_of_characters** | **bool** |  | [optional] 
**amount_of_digits_after_comma** | **int** |  | [optional] 
**value** | **str** |  | [optional] 
**attribute_type** | **str** |  | [optional] 
**attribute_asset_type** | **str** |  | [optional] 
**attribute_tooltip** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**is_inherit_assigned_user** | **bool** |  | [optional] 
**is_inherit_owner_user** | **bool** |  | [optional] 
**is_inherit_teams** | **bool** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_product_attribute_value_item_request import CreateProductAttributeValueItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductAttributeValueItemRequest from a JSON string
create_product_attribute_value_item_request_instance = CreateProductAttributeValueItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateProductAttributeValueItemRequest.to_json()

# convert the object into a dict
create_product_attribute_value_item_request_dict = create_product_attribute_value_item_request_instance.to_dict()
# create an instance of CreateProductAttributeValueItemRequest from a dict
create_product_attribute_value_item_request_form_dict = create_product_attribute_value_item_request.from_dict(create_product_attribute_value_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


