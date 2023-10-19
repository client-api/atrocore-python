# ProductAttributeValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**product_id** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**attribute_id** | **str** |  | [optional] 
**attribute_name** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**scope** | **str** |  | 
**channel_id** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**is_variant_specific_attribute** | **bool** |  | [optional] 
**count_bytes_instead_of_characters** | **bool** |  | [optional] 
**amount_of_digits_after_comma** | **int** |  | [optional] 
**value** | **str** |  | [optional] 
**attribute_type** | **str** |  | [optional] 
**attribute_asset_type** | **str** |  | [optional] 
**attribute_tooltip** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**is_inherit_assigned_user** | **bool** |  | [optional] 
**is_inherit_owner_user** | **bool** |  | [optional] 
**is_inherit_teams** | **bool** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**owner_user_name** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**assigned_user_name** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**teams_names** | **object** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.product_attribute_value import ProductAttributeValue

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAttributeValue from a JSON string
product_attribute_value_instance = ProductAttributeValue.from_json(json)
# print the JSON string representation of the object
print ProductAttributeValue.to_json()

# convert the object into a dict
product_attribute_value_dict = product_attribute_value_instance.to_dict()
# create an instance of ProductAttributeValue from a dict
product_attribute_value_form_dict = product_attribute_value.from_dict(product_attribute_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


