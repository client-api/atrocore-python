# Product


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**name_de_de** | **str** |  | 
**classifications_ids** | **List[str]** |  | [optional] 
**classifications_names** | **object** |  | [optional] 
**brand_id** | **str** |  | [optional] 
**brand_name** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**amount** | **str** |  | [optional] 
**price** | **str** |  | [optional] 
**price_currency** | **str** |  | [optional] 
**product_status** | **str** |  | 
**tax_id** | **str** |  | [optional] 
**tax_name** | **str** |  | [optional] 
**ean** | **str** |  | [optional] 
**mpn** | **str** |  | [optional] 
**packaging_id** | **str** |  | [optional] 
**packaging_name** | **str** |  | [optional] 
**uvp** | **str** |  | [optional] 
**tag** | **List[str]** |  | [optional] 
**long_description** | **str** |  | [optional] 
**long_description_de_de** | **str** |  | [optional] 
**product_serie_id** | **str** |  | [optional] 
**product_serie_name** | **str** |  | [optional] 
**parents_ids** | **List[str]** |  | [optional] 
**parents_names** | **object** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**catalog_id** | **str** |  | [optional] 
**catalog_name** | **str** |  | [optional] 
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
**sorting** | **int** |  | [optional] 
**contents_ids** | **List[str]** |  | [optional] 
**contents_names** | **object** |  | [optional] 
**is_inherit_assigned_user** | **bool** |  | [optional] 
**is_inherit_owner_user** | **bool** |  | [optional] 
**is_inherit_teams** | **bool** |  | [optional] 
**task_status** | **List[str]** |  | [optional] 
**attachments** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print Product.to_json()

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_form_dict = product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


