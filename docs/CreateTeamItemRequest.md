# CreateTeamItemRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**roles_ids** | **List[str]** |  | [optional] 
**position_list** | **List[str]** |  | [optional] 
**user_role** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.create_team_item_request import CreateTeamItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamItemRequest from a JSON string
create_team_item_request_instance = CreateTeamItemRequest.from_json(json)
# print the JSON string representation of the object
print CreateTeamItemRequest.to_json()

# convert the object into a dict
create_team_item_request_dict = create_team_item_request_instance.to_dict()
# create an instance of CreateTeamItemRequest from a dict
create_team_item_request_form_dict = create_team_item_request.from_dict(create_team_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


