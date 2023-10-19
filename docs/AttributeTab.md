# AttributeTab


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**name** | **str** |  | 
**name_de_de** | **str** |  | 
**description** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**modified_at** | **str** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**modified_by_name** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.attribute_tab import AttributeTab

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeTab from a JSON string
attribute_tab_instance = AttributeTab.from_json(json)
# print the JSON string representation of the object
print AttributeTab.to_json()

# convert the object into a dict
attribute_tab_dict = attribute_tab_instance.to_dict()
# create an instance of AttributeTab from a dict
attribute_tab_form_dict = attribute_tab.from_dict(attribute_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


