# Notification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**number** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**note_data** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**read** | **bool** |  | [optional] 
**user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**related_id** | **str** |  | [optional] 
**related_name** | **str** |  | [optional] 
**related_parent_id** | **str** |  | [optional] 
**related_parent_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print Notification.to_json()

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_form_dict = notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


