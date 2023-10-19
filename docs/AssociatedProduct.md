# AssociatedProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**association_id** | **str** |  | [optional] 
**association_name** | **str** |  | [optional] 
**main_product_id** | **str** |  | [optional] 
**main_product_name** | **str** |  | [optional] 
**related_product_id** | **str** |  | [optional] 
**related_product_name** | **str** |  | [optional] 
**backward_association_id** | **str** |  | [optional] 
**backward_association_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**sorting** | **int** |  | [optional] 
**main_product_image_id** | **str** |  | [optional] 
**main_product_image_name** | **str** |  | [optional] 
**related_product_image_id** | **str** |  | [optional] 
**related_product_image_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.associated_product import AssociatedProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AssociatedProduct from a JSON string
associated_product_instance = AssociatedProduct.from_json(json)
# print the JSON string representation of the object
print AssociatedProduct.to_json()

# convert the object into a dict
associated_product_dict = associated_product_instance.to_dict()
# create an instance of AssociatedProduct from a dict
associated_product_form_dict = associated_product.from_dict(associated_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


