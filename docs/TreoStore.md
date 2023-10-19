# TreoStore


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**package_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**versions** | **object** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.treo_store import TreoStore

# TODO update the JSON string below
json = "{}"
# create an instance of TreoStore from a JSON string
treo_store_instance = TreoStore.from_json(json)
# print the JSON string representation of the object
print TreoStore.to_json()

# convert the object into a dict
treo_store_dict = treo_store_instance.to_dict()
# create an instance of TreoStore from a dict
treo_store_form_dict = treo_store.from_dict(treo_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


