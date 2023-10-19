# Portal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**logo_id** | **str** |  | [optional] 
**logo_name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**custom_id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**portal_roles_ids** | **List[str]** |  | [optional] 
**portal_roles_names** | **object** |  | [optional] 
**tab_list** | **List[str]** |  | [optional] 
**quick_create_list** | **List[str]** |  | [optional] 
**company_logo_id** | **str** |  | [optional] 
**company_logo_name** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 
**locale_id** | **str** |  | [optional] 
**locale_name** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**time_format** | **str** |  | [optional] 
**week_start** | **int** |  | [optional] 
**default_currency** | **str** |  | [optional] 
**dashboard_layout** | **object** |  | [optional] 
**dashlets_options** | **object** |  | [optional] 
**custom_url** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.portal import Portal

# TODO update the JSON string below
json = "{}"
# create an instance of Portal from a JSON string
portal_instance = Portal.from_json(json)
# print the JSON string representation of the object
print Portal.to_json()

# convert the object into a dict
portal_dict = portal_instance.to_dict()
# create an instance of Portal from a dict
portal_form_dict = portal.from_dict(portal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


