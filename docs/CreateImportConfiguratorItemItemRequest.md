# CreateImportConfiguratorItemItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**scope** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**default_container** | **str** |  | [optional] 
**default** | **str** |  | [optional] 
**default_from** | **str** |  | [optional] 
**default_to** | **str** |  | [optional] 
**default_currency** | **str** |  | [optional] 
**default_id** | **str** |  | [optional] 
**default_paths_data** | **object** |  | [optional] 
**default_ids** | **List[str]** |  | [optional] 
**entity** | **str** |  | [optional] 
**source_fields** | **List[str]** |  | [optional] 
**import_feed_id** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**attribute_value** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_import_configurator_item_item_request import CreateImportConfiguratorItemItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateImportConfiguratorItemItemRequest from a JSON string
create_import_configurator_item_item_request_instance = CreateImportConfiguratorItemItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateImportConfiguratorItemItemRequest.to_json()

# convert the object into a dict
create_import_configurator_item_item_request_dict = create_import_configurator_item_item_request_instance.to_dict()
# create an instance of CreateImportConfiguratorItemItemRequest from a dict
create_import_configurator_item_item_request_form_dict = create_import_configurator_item_item_request.from_dict(create_import_configurator_item_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


