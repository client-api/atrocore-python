# ProductChannel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**channel_name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.product_channel import ProductChannel

# TODO update the JSON string below
json = "{}"
# create an instance of ProductChannel from a JSON string
product_channel_instance = ProductChannel.from_json(json)
# print the JSON string representation of the object
print ProductChannel.to_json()

# convert the object into a dict
product_channel_dict = product_channel_instance.to_dict()
# create an instance of ProductChannel from a dict
product_channel_form_dict = product_channel.from_dict(product_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


