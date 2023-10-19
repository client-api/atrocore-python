# Preferences


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**locale** | **str** |  | [optional] 
**locale_id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**decimal_mark** | **str** |  | [optional] 
**time_format** | **str** |  | [optional] 
**thousand_separator** | **str** |  | [optional] 
**week_start** | **int** |  | [optional] 
**date_format** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**default_currency** | **str** |  | [optional] 
**dashboard_layout** | **object** |  | [optional] 
**dashlets_options** | **object** |  | [optional] 
**shared_calendar_user_list** | **object** |  | [optional] 
**calendar_view_data_list** | **object** |  | [optional] 
**preset_filters** | **object** |  | [optional] 
**receive_assignment_email_notifications** | **bool** |  | [optional] 
**receive_mention_email_notifications** | **bool** |  | [optional] 
**receive_stream_email_notifications** | **bool** |  | [optional] 
**assignment_notifications** | **bool** |  | [optional] 
**auto_follow_entity_type_list** | **List[str]** |  | [optional] 
**theme** | **str** |  | [optional] 
**use_custom_tab_list** | **bool** |  | [optional] 
**tab_list** | **List[str]** |  | [optional] 
**is_portal_user** | **bool** |  | [optional] 
**follow_entity_on_stream_post** | **bool** |  | [optional] 
**follow_created_entities** | **bool** |  | [optional] 
**follow_created_entity_type_list** | **List[str]** |  | [optional] 
**scope_colors_disabled** | **bool** |  | [optional] 
**tab_colors_disabled** | **bool** |  | [optional] 

## Example

```python
from clientapi_atrocore.models.preferences import Preferences

# TODO update the JSON string below
json = "{}"
# create an instance of Preferences from a JSON string
preferences_instance = Preferences.from_json(json)
# print the JSON string representation of the object
print Preferences.to_json()

# convert the object into a dict
preferences_dict = preferences_instance.to_dict()
# create an instance of Preferences from a dict
preferences_form_dict = preferences.from_dict(preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


