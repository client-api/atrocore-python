# Connection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**type** | **str** |  | 
**name** | **str** |  | 
**host** | **str** |  | [optional] 
**db_name** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**ftp_ssl** | **bool** |  | [optional] 
**oauth_grant_type** | **str** |  | [optional] 
**oauth_url** | **str** |  | [optional] 
**oauth_client_id** | **str** |  | [optional] 
**oauth_client_secret** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print Connection.to_json()

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_form_dict = connection.from_dict(connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


