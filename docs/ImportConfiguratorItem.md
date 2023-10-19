# ImportConfiguratorItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**entity_identifier** | **bool** |  | [optional] 
**column** | **List[str]** |  | [optional] 
**import_by** | **List[str]** |  | [optional] 
**create_if_not_exist** | **bool** |  | [optional] 
**replace_array** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**foreign_column** | **List[str]** |  | [optional] 
**foreign_import_by** | **List[str]** |  | [optional] 
**attribute_id** | **str** |  | [optional] 
**attribute_name** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**default_container** | **str** |  | [optional] 
**default** | **str** |  | [optional] 
**default_from** | **str** |  | [optional] 
**default_to** | **str** |  | [optional] 
**default_currency** | **str** |  | [optional] 
**default_id** | **str** |  | [optional] 
**default_name** | **str** |  | [optional] 
**default_paths_data** | **object** |  | [optional] 
**default_ids** | **List[str]** |  | [optional] 
**default_names** | **object** |  | [optional] 
**entity** | **str** |  | [optional] 
**source_fields** | **List[str]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**import_feed_id** | **str** |  | [optional] 
**import_feed_name** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**attribute_value** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.import_configurator_item import ImportConfiguratorItem

# TODO update the JSON string below
json = "{}"
# create an instance of ImportConfiguratorItem from a JSON string
import_configurator_item_instance = ImportConfiguratorItem.from_json(json)
# print the JSON string representation of the object
print ImportConfiguratorItem.to_json()

# convert the object into a dict
import_configurator_item_dict = import_configurator_item_instance.to_dict()
# create an instance of ImportConfiguratorItem from a dict
import_configurator_item_form_dict = import_configurator_item.from_dict(import_configurator_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


