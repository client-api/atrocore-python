# GetListOfBrandItems200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**list** | [**List[Brand]**](Brand.md) |  | [optional] 

## Example

```python
from clientapi_atrocore.models.get_list_of_brand_items200_response import GetListOfBrandItems200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetListOfBrandItems200Response from a JSON string
get_list_of_brand_items200_response_instance = GetListOfBrandItems200Response.from_json(json)
# print the JSON string representation of the object
print GetListOfBrandItems200Response.to_json()

# convert the object into a dict
get_list_of_brand_items200_response_dict = get_list_of_brand_items200_response_instance.to_dict()
# create an instance of GetListOfBrandItems200Response from a dict
get_list_of_brand_items200_response_form_dict = get_list_of_brand_items200_response.from_dict(get_list_of_brand_items200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


