# ExportConfiguratorItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**attribute_value** | **str** |  | [optional] 
**zip** | **bool** |  | [optional] 
**file_name_template** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**column** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**column_type** | **str** |  | 
**export_into_separate_columns** | **bool** |  | [optional] 
**export_by** | **List[str]** |  | [optional] 
**filter_field** | **str** |  | [optional] 
**filter_field_value** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 
**value_modifier** | **List[str]** |  | [optional] 
**attribute_name_value** | **str** |  | [optional] 
**is_attribute_multi_lang** | **bool** |  | [optional] 
**language** | **str** |  | [optional] 
**entity** | **str** |  | [optional] 
**remove** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**export_feed_id** | **str** |  | [optional] 
**export_feed_name** | **str** |  | [optional] 
**mask** | **str** |  | [optional] 
**editable** | **bool** |  | [optional] 
**offset_relation** | **int** |  | [optional] 
**limit_relation** | **int** |  | [optional] 
**sort_field_relation** | **str** |  | [optional] 
**sort_order_relation** | **str** |  | [optional] 
**fixed_value** | **str** |  | [optional] 
**attribute_id** | **str** |  | [optional] 
**attribute_name** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.export_configurator_item import ExportConfiguratorItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExportConfiguratorItem from a JSON string
export_configurator_item_instance = ExportConfiguratorItem.from_json(json)
# print the JSON string representation of the object
print ExportConfiguratorItem.to_json()

# convert the object into a dict
export_configurator_item_dict = export_configurator_item_instance.to_dict()
# create an instance of ExportConfiguratorItem from a dict
export_configurator_item_form_dict = export_configurator_item.from_dict(export_configurator_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


