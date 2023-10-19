# CreateQueueItemItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**stream** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**sort_order** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**pid** | **str** |  | [optional] 
**md5_hash** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**actions** | **object** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_queue_item_item_request import CreateQueueItemItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateQueueItemItemRequest from a JSON string
create_queue_item_item_request_instance = CreateQueueItemItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateQueueItemItemRequest.to_json()

# convert the object into a dict
create_queue_item_item_request_dict = create_queue_item_item_request_instance.to_dict()
# create an instance of CreateQueueItemItemRequest from a dict
create_queue_item_item_request_form_dict = create_queue_item_item_request.from_dict(create_queue_item_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


