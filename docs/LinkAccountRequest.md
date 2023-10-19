# LinkAccountRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.link_account_request import LinkAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkAccountRequest from a JSON string
link_account_request_instance = LinkAccountRequest.from_json(json)
# print the JSON string representation of the object
print LinkAccountRequest.to_json()

# convert the object into a dict
link_account_request_dict = link_account_request_instance.to_dict()
# create an instance of LinkAccountRequest from a dict
link_account_request_form_dict = link_account_request.from_dict(link_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


