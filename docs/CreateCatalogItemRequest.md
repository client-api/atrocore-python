# CreateCatalogItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_de_de** | **str** |  | 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_de_de** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**products_count** | **int** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_catalog_item_request import CreateCatalogItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCatalogItemRequest from a JSON string
create_catalog_item_request_instance = CreateCatalogItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateCatalogItemRequest.to_json()

# convert the object into a dict
create_catalog_item_request_dict = create_catalog_item_request_instance.to_dict()
# create an instance of CreateCatalogItemRequest from a dict
create_catalog_item_request_form_dict = create_catalog_item_request.from_dict(create_catalog_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


