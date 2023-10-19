# CreateExportConfiguratorItemItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**export_feed_id** | **str** |  | [optional] 
**mask** | **str** |  | [optional] 
**editable** | **bool** |  | [optional] 
**offset_relation** | **int** |  | [optional] 
**limit_relation** | **int** |  | [optional] 
**sort_field_relation** | **str** |  | [optional] 
**sort_order_relation** | **str** |  | [optional] 
**fixed_value** | **str** |  | [optional] 
**attribute_id** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_export_configurator_item_item_request import CreateExportConfiguratorItemItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExportConfiguratorItemItemRequest from a JSON string
create_export_configurator_item_item_request_instance = CreateExportConfiguratorItemItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateExportConfiguratorItemItemRequest.to_json()

# convert the object into a dict
create_export_configurator_item_item_request_dict = create_export_configurator_item_item_request_instance.to_dict()
# create an instance of CreateExportConfiguratorItemItemRequest from a dict
create_export_configurator_item_item_request_form_dict = create_export_configurator_item_item_request.from_dict(create_export_configurator_item_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


