# CreatePortalItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**logo_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**custom_id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**portal_roles_ids** | **List[str]** |  | [optional] 
**tab_list** | **List[str]** |  | [optional] 
**quick_create_list** | **List[str]** |  | [optional] 
**company_logo_id** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 
**locale_id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**time_format** | **str** |  | [optional] 
**week_start** | **int** |  | [optional] 
**default_currency** | **str** |  | [optional] 
**dashboard_layout** | **object** |  | [optional] 
**dashlets_options** | **object** |  | [optional] 
**custom_url** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_portal_item_request import CreatePortalItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePortalItemRequest from a JSON string
create_portal_item_request_instance = CreatePortalItemRequest.from_json(json)
# print the JSON string representation of the object
print CreatePortalItemRequest.to_json()

# convert the object into a dict
create_portal_item_request_dict = create_portal_item_request_instance.to_dict()
# create an instance of CreatePortalItemRequest from a dict
create_portal_item_request_form_dict = create_portal_item_request.from_dict(create_portal_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


