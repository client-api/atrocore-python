# PortalRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**data** | **object** |  | [optional] 
**field_data** | **object** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.portal_role import PortalRole

# TODO update the JSON string below
json = "{}"
# create an instance of PortalRole from a JSON string
portal_role_instance = PortalRole.from_json(json)
# print the JSON string representation of the object
print PortalRole.to_json()

# convert the object into a dict
portal_role_dict = portal_role_instance.to_dict()
# create an instance of PortalRole from a dict
portal_role_form_dict = portal_role.from_dict(portal_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


