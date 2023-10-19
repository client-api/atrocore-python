# QueueItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**service_name** | **str** |  | 
**stream** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**parent_name** | **str** |  | [optional] 
**sort_order** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**pid** | **str** |  | [optional] 
**md5_hash** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**actions** | **object** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 
**owner_user_id** | **str** |  | [optional] 
**owner_user_name** | **str** |  | [optional] 
**assigned_user_id** | **str** |  | [optional] 
**assigned_user_name** | **str** |  | [optional] 
**teams_ids** | **List[str]** |  | [optional] 
**teams_names** | **object** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.queue_item import QueueItem

# TODO update the JSON string below
json = "{}"
# create an instance of QueueItem from a JSON string
queue_item_instance = QueueItem.from_json(json)
# print the JSON string representation of the object
print QueueItem.to_json()

# convert the object into a dict
queue_item_dict = queue_item_instance.to_dict()
# create an instance of QueueItem from a dict
queue_item_form_dict = queue_item.from_dict(queue_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


