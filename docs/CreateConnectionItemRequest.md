# CreateConnectionItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**host** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**ftp_ssl** | **bool** |  | [optional] 
**oauth_grant_type** | **str** |  | [optional] 
**oauth_url** | **str** |  | [optional] 
**oauth_client_id** | **str** |  | [optional] 
**oauth_client_secret** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_connection_item_request import CreateConnectionItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectionItemRequest from a JSON string
create_connection_item_request_instance = CreateConnectionItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateConnectionItemRequest.to_json()

# convert the object into a dict
create_connection_item_request_dict = create_connection_item_request_instance.to_dict()
# create an instance of CreateConnectionItemRequest from a dict
create_connection_item_request_form_dict = create_connection_item_request.from_dict(create_connection_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


