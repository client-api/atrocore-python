# CreateProductItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_de_de** | **str** |  | 
**classifications_ids** | **List[str]** |  | [optional] 
**brand_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**amount** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**price_currency** | **str** |  | [optional] 
**product_status** | **str** |  | 
**tax_id** | **str** |  | [optional] 
**ean** | **str** |  | [optional] 
**mpn** | **str** |  | [optional] 
**packaging_id** | **str** |  | [optional] 
**uvp** | **str** |  | [optional] 
**tag** | **List[str]** |  | [optional] 
**long_description** | **str** |  | [optional] 
**long_description_de_de** | **str** |  | [optional] 
**product_serie_id** | **str** |  | [optional] 
**parents_ids** | **List[str]** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**catalog_id** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**sorting** | **int** |  | [optional] 
**contents_ids** | **List[str]** |  | [optional] 
**is_inherit_assigned_user** | **bool** |  | [optional] 
**is_inherit_owner_user** | **bool** |  | [optional] 
**is_inherit_teams** | **bool** |  | [optional] 
**task_status** | **List[str]** |  | [optional] 
**attachments** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_product_item_request import CreateProductItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductItemRequest from a JSON string
create_product_item_request_instance = CreateProductItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateProductItemRequest.to_json()

# convert the object into a dict
create_product_item_request_dict = create_product_item_request_instance.to_dict()
# create an instance of CreateProductItemRequest from a dict
create_product_item_request_form_dict = create_product_item_request.from_dict(create_product_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


