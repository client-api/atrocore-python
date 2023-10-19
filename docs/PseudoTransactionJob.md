# PseudoTransactionJob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**entity_type** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**input_data** | **object** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**parent_name** | **str** |  | [optional] 
**md5** | **str** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.pseudo_transaction_job import PseudoTransactionJob

# TODO update the JSON string below
json = "{}"
# create an instance of PseudoTransactionJob from a JSON string
pseudo_transaction_job_instance = PseudoTransactionJob.from_json(json)
# print the JSON string representation of the object
print PseudoTransactionJob.to_json()

# convert the object into a dict
pseudo_transaction_job_dict = pseudo_transaction_job_instance.to_dict()
# create an instance of PseudoTransactionJob from a dict
pseudo_transaction_job_form_dict = pseudo_transaction_job.from_dict(pseudo_transaction_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


