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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class ExportConfiguratorItem(BaseModel):
    """
    ExportConfiguratorItem
    """
    id: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    attribute_value: Optional[StrictStr] = Field(None, alias="attributeValue")
    zip: Optional[StrictBool] = None
    file_name_template: Optional[StrictStr] = Field(None, alias="fileNameTemplate")
    name: Optional[StrictStr] = None
    column: Optional[StrictStr] = None
    sort_order: Optional[StrictInt] = Field(None, alias="sortOrder")
    column_type: StrictStr = Field(..., alias="columnType")
    export_into_separate_columns: Optional[StrictBool] = Field(None, alias="exportIntoSeparateColumns")
    export_by: Optional[conlist(StrictStr)] = Field(None, alias="exportBy")
    filter_field: Optional[StrictStr] = Field(None, alias="filterField")
    filter_field_value: Optional[conlist(StrictStr)] = Field(None, alias="filterFieldValue")
    type: Optional[StrictStr] = None
    value_modifier: Optional[conlist(StrictStr)] = Field(None, alias="valueModifier")
    attribute_name_value: Optional[StrictStr] = Field(None, alias="attributeNameValue")
    is_attribute_multi_lang: Optional[StrictBool] = Field(None, alias="isAttributeMultiLang")
    language: Optional[StrictStr] = None
    entity: Optional[StrictStr] = None
    remove: Optional[StrictStr] = None
    scope: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    export_feed_id: Optional[StrictStr] = Field(None, alias="exportFeedId")
    export_feed_name: Optional[StrictStr] = Field(None, alias="exportFeedName")
    mask: Optional[StrictStr] = None
    editable: Optional[StrictBool] = None
    offset_relation: Optional[StrictInt] = Field(None, alias="offsetRelation")
    limit_relation: Optional[StrictInt] = Field(None, alias="limitRelation")
    sort_field_relation: Optional[StrictStr] = Field(None, alias="sortFieldRelation")
    sort_order_relation: Optional[StrictStr] = Field(None, alias="sortOrderRelation")
    fixed_value: Optional[StrictStr] = Field(None, alias="fixedValue")
    attribute_id: Optional[StrictStr] = Field(None, alias="attributeId")
    attribute_name: Optional[StrictStr] = Field(None, alias="attributeName")
    channel_id: Optional[StrictStr] = Field(None, alias="channelId")
    channel_name: Optional[StrictStr] = Field(None, alias="channelName")
    __properties = ["id", "deleted", "attributeValue", "zip", "fileNameTemplate", "name", "column", "sortOrder", "columnType", "exportIntoSeparateColumns", "exportBy", "filterField", "filterFieldValue", "type", "valueModifier", "attributeNameValue", "isAttributeMultiLang", "language", "entity", "remove", "scope", "createdAt", "exportFeedId", "exportFeedName", "mask", "editable", "offsetRelation", "limitRelation", "sortFieldRelation", "sortOrderRelation", "fixedValue", "attributeId", "attributeName", "channelId", "channelName"]

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
    def from_json(cls, json_str: str) -> ExportConfiguratorItem:
        """Create an instance of ExportConfiguratorItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExportConfiguratorItem:
        """Create an instance of ExportConfiguratorItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExportConfiguratorItem.parse_obj(obj)

        _obj = ExportConfiguratorItem.parse_obj({
            "id": obj.get("id"),
            "deleted": obj.get("deleted"),
            "attribute_value": obj.get("attributeValue"),
            "zip": obj.get("zip"),
            "file_name_template": obj.get("fileNameTemplate"),
            "name": obj.get("name"),
            "column": obj.get("column"),
            "sort_order": obj.get("sortOrder"),
            "column_type": obj.get("columnType"),
            "export_into_separate_columns": obj.get("exportIntoSeparateColumns"),
            "export_by": obj.get("exportBy"),
            "filter_field": obj.get("filterField"),
            "filter_field_value": obj.get("filterFieldValue"),
            "type": obj.get("type"),
            "value_modifier": obj.get("valueModifier"),
            "attribute_name_value": obj.get("attributeNameValue"),
            "is_attribute_multi_lang": obj.get("isAttributeMultiLang"),
            "language": obj.get("language"),
            "entity": obj.get("entity"),
            "remove": obj.get("remove"),
            "scope": obj.get("scope"),
            "created_at": obj.get("createdAt"),
            "export_feed_id": obj.get("exportFeedId"),
            "export_feed_name": obj.get("exportFeedName"),
            "mask": obj.get("mask"),
            "editable": obj.get("editable"),
            "offset_relation": obj.get("offsetRelation"),
            "limit_relation": obj.get("limitRelation"),
            "sort_field_relation": obj.get("sortFieldRelation"),
            "sort_order_relation": obj.get("sortOrderRelation"),
            "fixed_value": obj.get("fixedValue"),
            "attribute_id": obj.get("attributeId"),
            "attribute_name": obj.get("attributeName"),
            "channel_id": obj.get("channelId"),
            "channel_name": obj.get("channelName")
        })
        return _obj


