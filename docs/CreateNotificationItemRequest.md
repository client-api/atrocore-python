# CreateNotificationItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**data** | **object** |  | [optional] 
**note_data** | **object** |  | [optional] 
**type** | **str** |  | [optional] 
**read** | **bool** |  | [optional] 
**user_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**related_id** | **str** |  | [optional] 
**related_parent_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_notification_item_request import CreateNotificationItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotificationItemRequest from a JSON string
create_notification_item_request_instance = CreateNotificationItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateNotificationItemRequest.to_json()

# convert the object into a dict
create_notification_item_request_dict = create_notification_item_request_instance.to_dict()
# create an instance of CreateNotificationItemRequest from a dict
create_notification_item_request_form_dict = create_notification_item_request.from_dict(create_notification_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


