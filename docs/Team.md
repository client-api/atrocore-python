# Team


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**roles_ids** | **List[str]** |  | [optional] 
**roles_names** | **object** |  | [optional] 
**position_list** | **List[str]** |  | [optional] 
**user_role** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print Team.to_json()

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_form_dict = team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


