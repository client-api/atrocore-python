# Settings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**app_id** | **str** |  | [optional] 
**is_stream_side** | **bool** |  | [optional] 
**is_stream_panel_first** | **bool** |  | [optional] 
**language_list** | **List[str]** |  | 
**main_language** | **str** |  | 
**input_language_list** | **List[str]** |  | 
**is_multilang_active** | **bool** |  | [optional] 
**use_cache** | **bool** |  | [optional] 
**records_per_page** | **int** |  | 
**records_per_page_small** | **int** |  | 
**currency_list** | **List[str]** |  | 
**default_currency** | **str** |  | 
**base_currency** | **str** |  | 
**currency_rates** | **str** |  | [optional] 
**outbound_email_from_name** | **str** |  | [optional] 
**outbound_email_from_address** | **str** |  | [optional] 
**smtp_server** | **str** |  | [optional] 
**smtp_port** | **int** |  | [optional] 
**smtp_auth** | **bool** |  | [optional] 
**smtp_auth_mechanism** | **str** |  | [optional] 
**smtp_security** | **str** |  | [optional] 
**smtp_username** | **str** |  | 
**smtp_password** | **str** |  | [optional] 
**tab_list** | **List[str]** |  | [optional] 
**quick_create_list** | **List[str]** |  | [optional] 
**locale** | **str** |  | 
**global_search_entity_list** | **List[str]** |  | [optional] 
**company_logo_id** | **str** |  | [optional] 
**company_logo_name** | **str** |  | [optional] 
**favicon_id** | **str** |  | [optional] 
**favicon_name** | **str** |  | [optional] 
**assignment_email_notifications** | **bool** |  | [optional] 
**assignment_notifications** | **bool** |  | [optional] 
**post_email_notifications** | **bool** |  | [optional] 
**update_email_notifications** | **bool** |  | [optional] 
**mention_email_notifications** | **bool** |  | [optional] 
**stream_email_notifications** | **bool** |  | [optional] 
**portal_stream_email_notifications** | **bool** |  | [optional] 
**b2c_mode** | **bool** |  | [optional] 
**avatars_disabled** | **bool** |  | [optional] 
**follow_created_entities** | **bool** |  | [optional] 
**admin_panel_iframe_url** | **str** |  | [optional] 
**display_list_view_record_count** | **bool** |  | [optional] 
**user_themes_disabled** | **bool** |  | [optional] 
**theme** | **str** |  | [optional] 
**auth_token_lifetime** | **str** |  | [optional] 
**auth_token_max_idle_time** | **str** |  | [optional] 
**auth_token_prevent_concurrent** | **bool** |  | [optional] 
**dashboard_layout** | **object** |  | [optional] 
**dashlets_options** | **object** |  | [optional] 
**site_url** | **str** |  | [optional] 
**application_name** | **str** |  | [optional] 
**readable_date_format_disabled** | **bool** |  | [optional] 
**currency_format** | **str** |  | [optional] 
**currency_decimal_places** | **int** |  | [optional] 
**notification_sounds_disabled** | **bool** |  | [optional] 
**calendar_entity_list** | **List[str]** |  | [optional] 
**activities_entity_list** | **List[str]** |  | [optional] 
**history_entity_list** | **List[str]** |  | [optional] 
**acl_strict_mode** | **bool** |  | [optional] 
**last_viewed_count** | **int** |  | 
**admin_notifications** | **bool** |  | [optional] 
**admin_notifications_new_version** | **bool** |  | [optional] 
**admin_notifications_new_extension_version** | **bool** |  | [optional] 
**text_filter_use_contains_for_varchar** | **bool** |  | [optional] 
**scope_colors_disabled** | **bool** |  | [optional] 
**tab_colors_disabled** | **bool** |  | [optional] 
**tab_icons_disabled** | **bool** |  | [optional] 
**email_address_is_opted_out_by_default** | **bool** |  | [optional] 
**cleanup_deleted_records** | **bool** |  | [optional] 
**custom_stylesheet_path** | **str** |  | [optional] 
**custom_stylesheet** | **str** |  | [optional] 
**custom_stylesheets_list** | **object** |  | [optional] 
**navigation_manu_background_color** | **str** |  | [optional] 
**navigation_menu_font_color** | **str** |  | [optional] 
**link_font_color** | **str** |  | [optional] 
**primary_color** | **str** |  | [optional] 
**secondary_color** | **str** |  | [optional] 
**primary_font_color** | **str** |  | [optional] 
**secondary_font_color** | **str** |  | [optional] 
**label_color** | **str** |  | [optional] 
**anchor_navigation_background** | **str** |  | [optional] 
**icon_color** | **str** |  | [optional] 
**primary_border_color** | **str** |  | [optional] 
**secondary_border_color** | **str** |  | [optional] 
**panel_title_color** | **str** |  | [optional] 
**header_title_color** | **str** |  | [optional] 
**success** | **str** |  | [optional] 
**notice** | **str** |  | [optional] 
**information** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**attachment_duplicates** | **str** |  | 
**file_name_regex_pattern** | **str** |  | [optional] 
**product_can_linked_with_non_leaf_categories** | **bool** |  | [optional] 
**behavior_on_catalog_change** | **str** |  | 
**behavior_on_category_delete** | **str** |  | 
**behavior_on_category_tree_unlink_from_catalog** | **str** |  | 
**behavior_on_classification_change** | **str** |  | 

## Example

```python
from clientapi_atrocore.models.settings import Settings

# TODO update the JSON string below
json = "{}"
# create an instance of Settings from a JSON string
settings_instance = Settings.from_json(json)
# print the JSON string representation of the object
print Settings.to_json()

# convert the object into a dict
settings_dict = settings_instance.to_dict()
# create an instance of Settings from a dict
settings_form_dict = settings.from_dict(settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


