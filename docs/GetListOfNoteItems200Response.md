# GetListOfNoteItems200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**list** | [**List[Note]**](Note.md) |  | [optional] 

## Example

```python
from clientapi_atrocore.models.get_list_of_note_items200_response import GetListOfNoteItems200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetListOfNoteItems200Response from a JSON string
get_list_of_note_items200_response_instance = GetListOfNoteItems200Response.from_json(json)
# print the JSON string representation of the object
print GetListOfNoteItems200Response.to_json()

# convert the object into a dict
get_list_of_note_items200_response_dict = get_list_of_note_items200_response_instance.to_dict()
# create an instance of GetListOfNoteItems200Response from a dict
get_list_of_note_items200_response_form_dict = get_list_of_note_items200_response.from_dict(get_list_of_note_items200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


