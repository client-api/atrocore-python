# CreateLocaleItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**language** | **str** |  | 
**decimal_mark** | **str** |  | 
**time_format** | **str** |  | 
**thousand_separator** | **str** |  | [optional] 
**week_start** | **str** |  | 
**date_format** | **str** |  | 
**time_zone** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_locale_item_request import CreateLocaleItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLocaleItemRequest from a JSON string
create_locale_item_request_instance = CreateLocaleItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateLocaleItemRequest.to_json()

# convert the object into a dict
create_locale_item_request_dict = create_locale_item_request_instance.to_dict()
# create an instance of CreateLocaleItemRequest from a dict
create_locale_item_request_form_dict = create_locale_item_request.from_dict(create_locale_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


