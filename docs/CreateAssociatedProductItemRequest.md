# CreateAssociatedProductItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**association_id** | **str** |  | [optional] 
**main_product_id** | **str** |  | [optional] 
**related_product_id** | **str** |  | [optional] 
**backward_association_id** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**sorting** | **int** |  | [optional] 
**main_product_image_id** | **str** |  | [optional] 
**related_product_image_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_associated_product_item_request import CreateAssociatedProductItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAssociatedProductItemRequest from a JSON string
create_associated_product_item_request_instance = CreateAssociatedProductItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateAssociatedProductItemRequest.to_json()

# convert the object into a dict
create_associated_product_item_request_dict = create_associated_product_item_request_instance.to_dict()
# create an instance of CreateAssociatedProductItemRequest from a dict
create_associated_product_item_request_form_dict = create_associated_product_item_request.from_dict(create_associated_product_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


