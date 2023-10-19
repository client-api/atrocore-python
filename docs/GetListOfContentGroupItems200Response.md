# GetListOfContentGroupItems200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**list** | [**List[ContentGroup]**](ContentGroup.md) |  | [optional] 

## Example

```python
from clientapi_atrocore.models.get_list_of_content_group_items200_response import GetListOfContentGroupItems200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetListOfContentGroupItems200Response from a JSON string
get_list_of_content_group_items200_response_instance = GetListOfContentGroupItems200Response.from_json(json)
# print the JSON string representation of the object
print GetListOfContentGroupItems200Response.to_json()

# convert the object into a dict
get_list_of_content_group_items200_response_dict = get_list_of_content_group_items200_response_instance.to_dict()
# create an instance of GetListOfContentGroupItems200Response from a dict
get_list_of_content_group_items200_response_form_dict = get_list_of_content_group_items200_response.from_dict(get_list_of_content_group_items200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


