# ProductSerie


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**assigned_user_name** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**teams_names** | **object** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**owner_user_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.product_serie import ProductSerie

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSerie from a JSON string
product_serie_instance = ProductSerie.from_json(json)
# print the JSON string representation of the object
print ProductSerie.to_json()

# convert the object into a dict
product_serie_dict = product_serie_instance.to_dict()
# create an instance of ProductSerie from a dict
product_serie_form_dict = product_serie.from_dict(product_serie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


