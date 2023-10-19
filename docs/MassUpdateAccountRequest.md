# MassUpdateAccountRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | [optional] 
**ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.mass_update_account_request import MassUpdateAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MassUpdateAccountRequest from a JSON string
mass_update_account_request_instance = MassUpdateAccountRequest.from_json(json)
# print the JSON string representation of the object
print MassUpdateAccountRequest.to_json()

# convert the object into a dict
mass_update_account_request_dict = mass_update_account_request_instance.to_dict()
# create an instance of MassUpdateAccountRequest from a dict
mass_update_account_request_form_dict = mass_update_account_request.from_dict(mass_update_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


