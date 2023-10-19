# CreateProductChannelItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modified_by_id** | **str** |  | [optional] 
**product_id** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_product_channel_item_request import CreateProductChannelItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductChannelItemRequest from a JSON string
create_product_channel_item_request_instance = CreateProductChannelItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateProductChannelItemRequest.to_json()

# convert the object into a dict
create_product_channel_item_request_dict = create_product_channel_item_request_instance.to_dict()
# create an instance of CreateProductChannelItemRequest from a dict
create_product_channel_item_request_form_dict = create_product_channel_item_request.from_dict(create_product_channel_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


