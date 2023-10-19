# GetListOfQueueItemItems200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**list** | [**List[QueueItem]**](QueueItem.md) |  | [optional] 

## Example

```python
from clientapi_atrocore.models.get_list_of_queue_item_items200_response import GetListOfQueueItemItems200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetListOfQueueItemItems200Response from a JSON string
get_list_of_queue_item_items200_response_instance = GetListOfQueueItemItems200Response.from_json(json)
# print the JSON string representation of the object
print GetListOfQueueItemItems200Response.to_json()

# convert the object into a dict
get_list_of_queue_item_items200_response_dict = get_list_of_queue_item_items200_response_instance.to_dict()
# create an instance of GetListOfQueueItemItems200Response from a dict
get_list_of_queue_item_items200_response_form_dict = get_list_of_queue_item_items200_response.from_dict(get_list_of_queue_item_items200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


