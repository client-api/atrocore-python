# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class Settings(BaseModel):
    """
    Settings
    """
    id: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    app_id: Optional[StrictStr] = Field(None, alias="appId")
    is_stream_side: Optional[StrictBool] = Field(None, alias="isStreamSide")
    is_stream_panel_first: Optional[StrictBool] = Field(None, alias="isStreamPanelFirst")
    language_list: conlist(StrictStr) = Field(..., alias="languageList")
    main_language: StrictStr = Field(..., alias="mainLanguage")
    input_language_list: conlist(StrictStr) = Field(..., alias="inputLanguageList")
    is_multilang_active: Optional[StrictBool] = Field(None, alias="isMultilangActive")
    use_cache: Optional[StrictBool] = Field(None, alias="useCache")
    records_per_page: StrictInt = Field(..., alias="recordsPerPage")
    records_per_page_small: StrictInt = Field(..., alias="recordsPerPageSmall")
    currency_list: conlist(StrictStr) = Field(..., alias="currencyList")
    default_currency: StrictStr = Field(..., alias="defaultCurrency")
    base_currency: StrictStr = Field(..., alias="baseCurrency")
    currency_rates: Optional[StrictStr] = Field(None, alias="currencyRates")
    outbound_email_from_name: Optional[StrictStr] = Field(None, alias="outboundEmailFromName")
    outbound_email_from_address: Optional[StrictStr] = Field(None, alias="outboundEmailFromAddress")
    smtp_server: Optional[StrictStr] = Field(None, alias="smtpServer")
    smtp_port: Optional[StrictInt] = Field(None, alias="smtpPort")
    smtp_auth: Optional[StrictBool] = Field(None, alias="smtpAuth")
    smtp_auth_mechanism: Optional[StrictStr] = Field(None, alias="smtpAuthMechanism")
    smtp_security: Optional[StrictStr] = Field(None, alias="smtpSecurity")
    smtp_username: StrictStr = Field(..., alias="smtpUsername")
    smtp_password: Optional[StrictStr] = Field(None, alias="smtpPassword")
    tab_list: Optional[conlist(StrictStr)] = Field(None, alias="tabList")
    quick_create_list: Optional[conlist(StrictStr)] = Field(None, alias="quickCreateList")
    locale: StrictStr = Field(...)
    global_search_entity_list: Optional[conlist(StrictStr)] = Field(None, alias="globalSearchEntityList")
    company_logo_id: Optional[StrictStr] = Field(None, alias="companyLogoId")
    company_logo_name: Optional[StrictStr] = Field(None, alias="companyLogoName")
    favicon_id: Optional[StrictStr] = Field(None, alias="faviconId")
    favicon_name: Optional[StrictStr] = Field(None, alias="faviconName")
    assignment_email_notifications: Optional[StrictBool] = Field(None, alias="assignmentEmailNotifications")
    assignment_notifications: Optional[StrictBool] = Field(None, alias="assignmentNotifications")
    post_email_notifications: Optional[StrictBool] = Field(None, alias="postEmailNotifications")
    update_email_notifications: Optional[StrictBool] = Field(None, alias="updateEmailNotifications")
    mention_email_notifications: Optional[StrictBool] = Field(None, alias="mentionEmailNotifications")
    stream_email_notifications: Optional[StrictBool] = Field(None, alias="streamEmailNotifications")
    portal_stream_email_notifications: Optional[StrictBool] = Field(None, alias="portalStreamEmailNotifications")
    b2c_mode: Optional[StrictBool] = Field(None, alias="b2cMode")
    avatars_disabled: Optional[StrictBool] = Field(None, alias="avatarsDisabled")
    follow_created_entities: Optional[StrictBool] = Field(None, alias="followCreatedEntities")
    admin_panel_iframe_url: Optional[StrictStr] = Field(None, alias="adminPanelIframeUrl")
    display_list_view_record_count: Optional[StrictBool] = Field(None, alias="displayListViewRecordCount")
    user_themes_disabled: Optional[StrictBool] = Field(None, alias="userThemesDisabled")
    theme: Optional[StrictStr] = None
    auth_token_lifetime: Optional[StrictStr] = Field(None, alias="authTokenLifetime")
    auth_token_max_idle_time: Optional[StrictStr] = Field(None, alias="authTokenMaxIdleTime")
    auth_token_prevent_concurrent: Optional[StrictBool] = Field(None, alias="authTokenPreventConcurrent")
    dashboard_layout: Optional[Dict[str, Any]] = Field(None, alias="dashboardLayout")
    dashlets_options: Optional[Dict[str, Any]] = Field(None, alias="dashletsOptions")
    site_url: Optional[StrictStr] = Field(None, alias="siteUrl")
    application_name: Optional[StrictStr] = Field(None, alias="applicationName")
    readable_date_format_disabled: Optional[StrictBool] = Field(None, alias="readableDateFormatDisabled")
    currency_format: Optional[StrictStr] = Field(None, alias="currencyFormat")
    currency_decimal_places: Optional[StrictInt] = Field(None, alias="currencyDecimalPlaces")
    notification_sounds_disabled: Optional[StrictBool] = Field(None, alias="notificationSoundsDisabled")
    calendar_entity_list: Optional[conlist(StrictStr)] = Field(None, alias="calendarEntityList")
    activities_entity_list: Optional[conlist(StrictStr)] = Field(None, alias="activitiesEntityList")
    history_entity_list: Optional[conlist(StrictStr)] = Field(None, alias="historyEntityList")
    acl_strict_mode: Optional[StrictBool] = Field(None, alias="aclStrictMode")
    last_viewed_count: StrictInt = Field(..., alias="lastViewedCount")
    admin_notifications: Optional[StrictBool] = Field(None, alias="adminNotifications")
    admin_notifications_new_version: Optional[StrictBool] = Field(None, alias="adminNotificationsNewVersion")
    admin_notifications_new_extension_version: Optional[StrictBool] = Field(None, alias="adminNotificationsNewExtensionVersion")
    text_filter_use_contains_for_varchar: Optional[StrictBool] = Field(None, alias="textFilterUseContainsForVarchar")
    scope_colors_disabled: Optional[StrictBool] = Field(None, alias="scopeColorsDisabled")
    tab_colors_disabled: Optional[StrictBool] = Field(None, alias="tabColorsDisabled")
    tab_icons_disabled: Optional[StrictBool] = Field(None, alias="tabIconsDisabled")
    email_address_is_opted_out_by_default: Optional[StrictBool] = Field(None, alias="emailAddressIsOptedOutByDefault")
    cleanup_deleted_records: Optional[StrictBool] = Field(None, alias="cleanupDeletedRecords")
    custom_stylesheet_path: Optional[StrictStr] = Field(None, alias="customStylesheetPath")
    custom_stylesheet: Optional[StrictStr] = Field(None, alias="customStylesheet")
    custom_stylesheets_list: Optional[Dict[str, Any]] = Field(None, alias="customStylesheetsList")
    navigation_manu_background_color: Optional[StrictStr] = Field(None, alias="navigationManuBackgroundColor")
    navigation_menu_font_color: Optional[StrictStr] = Field(None, alias="navigationMenuFontColor")
    link_font_color: Optional[StrictStr] = Field(None, alias="linkFontColor")
    primary_color: Optional[StrictStr] = Field(None, alias="primaryColor")
    secondary_color: Optional[StrictStr] = Field(None, alias="secondaryColor")
    primary_font_color: Optional[StrictStr] = Field(None, alias="primaryFontColor")
    secondary_font_color: Optional[StrictStr] = Field(None, alias="secondaryFontColor")
    label_color: Optional[StrictStr] = Field(None, alias="labelColor")
    anchor_navigation_background: Optional[StrictStr] = Field(None, alias="anchorNavigationBackground")
    icon_color: Optional[StrictStr] = Field(None, alias="iconColor")
    primary_border_color: Optional[StrictStr] = Field(None, alias="primaryBorderColor")
    secondary_border_color: Optional[StrictStr] = Field(None, alias="secondaryBorderColor")
    panel_title_color: Optional[StrictStr] = Field(None, alias="panelTitleColor")
    header_title_color: Optional[StrictStr] = Field(None, alias="headerTitleColor")
    success: Optional[StrictStr] = None
    notice: Optional[StrictStr] = None
    information: Optional[StrictStr] = None
    error: Optional[StrictStr] = None
    attachment_duplicates: StrictStr = Field(..., alias="attachmentDuplicates")
    file_name_regex_pattern: Optional[StrictStr] = Field(None, alias="fileNameRegexPattern")
    product_can_linked_with_non_leaf_categories: Optional[StrictBool] = Field(None, alias="productCanLinkedWithNonLeafCategories")
    behavior_on_catalog_change: StrictStr = Field(..., alias="behaviorOnCatalogChange")
    behavior_on_category_delete: StrictStr = Field(..., alias="behaviorOnCategoryDelete")
    behavior_on_category_tree_unlink_from_catalog: StrictStr = Field(..., alias="behaviorOnCategoryTreeUnlinkFromCatalog")
    behavior_on_classification_change: StrictStr = Field(..., alias="behaviorOnClassificationChange")
    __properties = ["id", "deleted", "appId", "isStreamSide", "isStreamPanelFirst", "languageList", "mainLanguage", "inputLanguageList", "isMultilangActive", "useCache", "recordsPerPage", "recordsPerPageSmall", "currencyList", "defaultCurrency", "baseCurrency", "currencyRates", "outboundEmailFromName", "outboundEmailFromAddress", "smtpServer", "smtpPort", "smtpAuth", "smtpAuthMechanism", "smtpSecurity", "smtpUsername", "smtpPassword", "tabList", "quickCreateList", "locale", "globalSearchEntityList", "companyLogoId", "companyLogoName", "faviconId", "faviconName", "assignmentEmailNotifications", "assignmentNotifications", "postEmailNotifications", "updateEmailNotifications", "mentionEmailNotifications", "streamEmailNotifications", "portalStreamEmailNotifications", "b2cMode", "avatarsDisabled", "followCreatedEntities", "adminPanelIframeUrl", "displayListViewRecordCount", "userThemesDisabled", "theme", "authTokenLifetime", "authTokenMaxIdleTime", "authTokenPreventConcurrent", "dashboardLayout", "dashletsOptions", "siteUrl", "applicationName", "readableDateFormatDisabled", "currencyFormat", "currencyDecimalPlaces", "notificationSoundsDisabled", "calendarEntityList", "activitiesEntityList", "historyEntityList", "aclStrictMode", "lastViewedCount", "adminNotifications", "adminNotificationsNewVersion", "adminNotificationsNewExtensionVersion", "textFilterUseContainsForVarchar", "scopeColorsDisabled", "tabColorsDisabled", "tabIconsDisabled", "emailAddressIsOptedOutByDefault", "cleanupDeletedRecords", "customStylesheetPath", "customStylesheet", "customStylesheetsList", "navigationManuBackgroundColor", "navigationMenuFontColor", "linkFontColor", "primaryColor", "secondaryColor", "primaryFontColor", "secondaryFontColor", "labelColor", "anchorNavigationBackground", "iconColor", "primaryBorderColor", "secondaryBorderColor", "panelTitleColor", "headerTitleColor", "success", "notice", "information", "error", "attachmentDuplicates", "fileNameRegexPattern", "productCanLinkedWithNonLeafCategories", "behaviorOnCatalogChange", "behaviorOnCategoryDelete", "behaviorOnCategoryTreeUnlinkFromCatalog", "behaviorOnClassificationChange"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Settings:
        """Create an instance of Settings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Settings:
        """Create an instance of Settings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Settings.parse_obj(obj)

        _obj = Settings.parse_obj({
            "id": obj.get("id"),
            "deleted": obj.get("deleted"),
            "app_id": obj.get("appId"),
            "is_stream_side": obj.get("isStreamSide"),
            "is_stream_panel_first": obj.get("isStreamPanelFirst"),
            "language_list": obj.get("languageList"),
            "main_language": obj.get("mainLanguage"),
            "input_language_list": obj.get("inputLanguageList"),
            "is_multilang_active": obj.get("isMultilangActive"),
            "use_cache": obj.get("useCache"),
            "records_per_page": obj.get("recordsPerPage"),
            "records_per_page_small": obj.get("recordsPerPageSmall"),
            "currency_list": obj.get("currencyList"),
            "default_currency": obj.get("defaultCurrency"),
            "base_currency": obj.get("baseCurrency"),
            "currency_rates": obj.get("currencyRates"),
            "outbound_email_from_name": obj.get("outboundEmailFromName"),
            "outbound_email_from_address": obj.get("outboundEmailFromAddress"),
            "smtp_server": obj.get("smtpServer"),
            "smtp_port": obj.get("smtpPort"),
            "smtp_auth": obj.get("smtpAuth"),
            "smtp_auth_mechanism": obj.get("smtpAuthMechanism"),
            "smtp_security": obj.get("smtpSecurity"),
            "smtp_username": obj.get("smtpUsername"),
            "smtp_password": obj.get("smtpPassword"),
            "tab_list": obj.get("tabList"),
            "quick_create_list": obj.get("quickCreateList"),
            "locale": obj.get("locale"),
            "global_search_entity_list": obj.get("globalSearchEntityList"),
            "company_logo_id": obj.get("companyLogoId"),
            "company_logo_name": obj.get("companyLogoName"),
            "favicon_id": obj.get("faviconId"),
            "favicon_name": obj.get("faviconName"),
            "assignment_email_notifications": obj.get("assignmentEmailNotifications"),
            "assignment_notifications": obj.get("assignmentNotifications"),
            "post_email_notifications": obj.get("postEmailNotifications"),
            "update_email_notifications": obj.get("updateEmailNotifications"),
            "mention_email_notifications": obj.get("mentionEmailNotifications"),
            "stream_email_notifications": obj.get("streamEmailNotifications"),
            "portal_stream_email_notifications": obj.get("portalStreamEmailNotifications"),
            "b2c_mode": obj.get("b2cMode"),
            "avatars_disabled": obj.get("avatarsDisabled"),
            "follow_created_entities": obj.get("followCreatedEntities"),
            "admin_panel_iframe_url": obj.get("adminPanelIframeUrl"),
            "display_list_view_record_count": obj.get("displayListViewRecordCount"),
            "user_themes_disabled": obj.get("userThemesDisabled"),
            "theme": obj.get("theme"),
            "auth_token_lifetime": obj.get("authTokenLifetime"),
            "auth_token_max_idle_time": obj.get("authTokenMaxIdleTime"),
            "auth_token_prevent_concurrent": obj.get("authTokenPreventConcurrent"),
            "dashboard_layout": obj.get("dashboardLayout"),
            "dashlets_options": obj.get("dashletsOptions"),
            "site_url": obj.get("siteUrl"),
            "application_name": obj.get("applicationName"),
            "readable_date_format_disabled": obj.get("readableDateFormatDisabled"),
            "currency_format": obj.get("currencyFormat"),
            "currency_decimal_places": obj.get("currencyDecimalPlaces"),
            "notification_sounds_disabled": obj.get("notificationSoundsDisabled"),
            "calendar_entity_list": obj.get("calendarEntityList"),
            "activities_entity_list": obj.get("activitiesEntityList"),
            "history_entity_list": obj.get("historyEntityList"),
            "acl_strict_mode": obj.get("aclStrictMode"),
            "last_viewed_count": obj.get("lastViewedCount"),
            "admin_notifications": obj.get("adminNotifications"),
            "admin_notifications_new_version": obj.get("adminNotificationsNewVersion"),
            "admin_notifications_new_extension_version": obj.get("adminNotificationsNewExtensionVersion"),
            "text_filter_use_contains_for_varchar": obj.get("textFilterUseContainsForVarchar"),
            "scope_colors_disabled": obj.get("scopeColorsDisabled"),
            "tab_colors_disabled": obj.get("tabColorsDisabled"),
            "tab_icons_disabled": obj.get("tabIconsDisabled"),
            "email_address_is_opted_out_by_default": obj.get("emailAddressIsOptedOutByDefault"),
            "cleanup_deleted_records": obj.get("cleanupDeletedRecords"),
            "custom_stylesheet_path": obj.get("customStylesheetPath"),
            "custom_stylesheet": obj.get("customStylesheet"),
            "custom_stylesheets_list": obj.get("customStylesheetsList"),
            "navigation_manu_background_color": obj.get("navigationManuBackgroundColor"),
            "navigation_menu_font_color": obj.get("navigationMenuFontColor"),
            "link_font_color": obj.get("linkFontColor"),
            "primary_color": obj.get("primaryColor"),
            "secondary_color": obj.get("secondaryColor"),
            "primary_font_color": obj.get("primaryFontColor"),
            "secondary_font_color": obj.get("secondaryFontColor"),
            "label_color": obj.get("labelColor"),
            "anchor_navigation_background": obj.get("anchorNavigationBackground"),
            "icon_color": obj.get("iconColor"),
            "primary_border_color": obj.get("primaryBorderColor"),
            "secondary_border_color": obj.get("secondaryBorderColor"),
            "panel_title_color": obj.get("panelTitleColor"),
            "header_title_color": obj.get("headerTitleColor"),
            "success": obj.get("success"),
            "notice": obj.get("notice"),
            "information": obj.get("information"),
            "error": obj.get("error"),
            "attachment_duplicates": obj.get("attachmentDuplicates"),
            "file_name_regex_pattern": obj.get("fileNameRegexPattern"),
            "product_can_linked_with_non_leaf_categories": obj.get("productCanLinkedWithNonLeafCategories"),
            "behavior_on_catalog_change": obj.get("behaviorOnCatalogChange"),
            "behavior_on_category_delete": obj.get("behaviorOnCategoryDelete"),
            "behavior_on_category_tree_unlink_from_catalog": obj.get("behaviorOnCategoryTreeUnlinkFromCatalog"),
            "behavior_on_classification_change": obj.get("behaviorOnClassificationChange")
        })
        return _obj


