# GetListOfImportConfiguratorItemItems200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**list** | [**List[ImportConfiguratorItem]**](ImportConfiguratorItem.md) |  | [optional] 

## Example

```python
from clientapi_atrocore.models.get_list_of_import_configurator_item_items200_response import GetListOfImportConfiguratorItemItems200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetListOfImportConfiguratorItemItems200Response from a JSON string
get_list_of_import_configurator_item_items200_response_instance = GetListOfImportConfiguratorItemItems200Response.from_json(json)
# print the JSON string representation of the object
print GetListOfImportConfiguratorItemItems200Response.to_json()

# convert the object into a dict
get_list_of_import_configurator_item_items200_response_dict = get_list_of_import_configurator_item_items200_response_instance.to_dict()
# create an instance of GetListOfImportConfiguratorItemItems200Response from a dict
get_list_of_import_configurator_item_items200_response_form_dict = get_list_of_import_configurator_item_items200_response.from_dict(get_list_of_import_configurator_item_items200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


