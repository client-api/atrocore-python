# GetModulesLogs200ResponseListInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**post** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**target_type** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**parent_name** | **str** |  | [optional] 
**related_id** | **str** |  | [optional] 
**related_name** | **str** |  | [optional] 
**attachments** | **str** |  | [optional] 
**number** | **int** |  | [optional] 
**is_global** | **bool** |  | [optional] 
**created_by_gender** | **str** |  | [optional] 
**notified_user_id_list** | **object** |  | [optional] 
**is_internal** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**attribute_id** | **str** |  | [optional] 
**pav_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.get_modules_logs200_response_list_inner import GetModulesLogs200ResponseListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetModulesLogs200ResponseListInner from a JSON string
get_modules_logs200_response_list_inner_instance = GetModulesLogs200ResponseListInner.from_json(json)
# print the JSON string representation of the object
print GetModulesLogs200ResponseListInner.to_json()

# convert the object into a dict
get_modules_logs200_response_list_inner_dict = get_modules_logs200_response_list_inner_instance.to_dict()
# create an instance of GetModulesLogs200ResponseListInner from a dict
get_modules_logs200_response_list_inner_form_dict = get_modules_logs200_response_list_inner.from_dict(get_modules_logs200_response_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


