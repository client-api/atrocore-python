# GetInstalledModules200ResponseListInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**current_version** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**is_system** | **bool** |  | [optional] 
**is_composer** | **bool** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.get_installed_modules200_response_list_inner import GetInstalledModules200ResponseListInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInstalledModules200ResponseListInner from a JSON string
get_installed_modules200_response_list_inner_instance = GetInstalledModules200ResponseListInner.from_json(json)
# print the JSON string representation of the object
print GetInstalledModules200ResponseListInner.to_json()

# convert the object into a dict
get_installed_modules200_response_list_inner_dict = get_installed_modules200_response_list_inner_instance.to_dict()
# create an instance of GetInstalledModules200ResponseListInner from a dict
get_installed_modules200_response_list_inner_form_dict = get_installed_modules200_response_list_inner.from_dict(get_installed_modules200_response_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


