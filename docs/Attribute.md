# Attribute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**name_de_de** | **str** |  | 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**owner_user_name** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**assigned_user_name** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**teams_names** | **object** |  | [optional] 
**attribute_group_id** | **str** |  | [optional] 
**attribute_group_name** | **str** |  | [optional] 
**attribute_tab_id** | **str** |  | [optional] 
**attribute_tab_name** | **str** |  | [optional] 
**extensible_enum_id** | **str** |  | [optional] 
**extensible_enum_name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**type** | **str** |  | 
**asset_type** | **str** |  | [optional] 
**is_multilang** | **bool** |  | [optional] 
**pattern** | **str** |  | [optional] 
**unique** | **bool** |  | [optional] 
**prohibited_empty_value** | **bool** |  | [optional] 
**virtual_product_field** | **bool** |  | [optional] 
**measure_id** | **str** |  | [optional] 
**measure_name** | **str** |  | [optional] 
**default_unit** | **str** |  | [optional] 
**default_scope** | **str** |  | [optional] 
**default_channel_id** | **str** |  | [optional] 
**default_channel_name** | **str** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**sort_order_in_attribute_group** | **int** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**sort_order_in_product** | **int** |  | [optional] 
**tooltip** | **str** |  | [optional] 
**tooltip_de_de** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_de_de** | **str** |  | [optional] 
**amount_of_digits_after_comma** | **int** |  | [optional] 
**use_disabled_textarea_in_view_mode** | **bool** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.attribute import Attribute

# TODO update the JSON string below
json = "{}"
# create an instance of Attribute from a JSON string
attribute_instance = Attribute.from_json(json)
# print the JSON string representation of the object
print Attribute.to_json()

# convert the object into a dict
attribute_dict = attribute_instance.to_dict()
# create an instance of Attribute from a dict
attribute_form_dict = attribute.from_dict(attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


