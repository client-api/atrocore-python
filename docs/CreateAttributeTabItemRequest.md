# CreateAttributeTabItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_de_de** | **str** |  | 
**description** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_attribute_tab_item_request import CreateAttributeTabItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAttributeTabItemRequest from a JSON string
create_attribute_tab_item_request_instance = CreateAttributeTabItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateAttributeTabItemRequest.to_json()

# convert the object into a dict
create_attribute_tab_item_request_dict = create_attribute_tab_item_request_instance.to_dict()
# create an instance of CreateAttributeTabItemRequest from a dict
create_attribute_tab_item_request_form_dict = create_attribute_tab_item_request.from_dict(create_attribute_tab_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


