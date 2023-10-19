# Sharing


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**available** | **bool** |  | [optional] 
**entity_type** | **str** |  | 
**entity_id** | **str** |  | 
**type** | **str** |  | 
**valid_till** | **str** |  | [optional] 
**allowed_usage** | **int** |  | [optional] 
**used** | **int** |  | [optional] 
**link** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.sharing import Sharing

# TODO update the JSON string below
json = "{}"
# create an instance of Sharing from a JSON string
sharing_instance = Sharing.from_json(json)
# print the JSON string representation of the object
print Sharing.to_json()

# convert the object into a dict
sharing_dict = sharing_instance.to_dict()
# create an instance of Sharing from a dict
sharing_form_dict = sharing.from_dict(sharing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


