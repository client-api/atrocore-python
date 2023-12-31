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

class ValidationRule(BaseModel):
    """
    ValidationRule
    """
    id: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    modified_at: Optional[StrictStr] = Field(None, alias="modifiedAt")
    created_by_id: Optional[StrictStr] = Field(None, alias="createdById")
    created_by_name: Optional[StrictStr] = Field(None, alias="createdByName")
    modified_by_id: Optional[StrictStr] = Field(None, alias="modifiedById")
    modified_by_name: Optional[StrictStr] = Field(None, alias="modifiedByName")
    is_active: Optional[StrictBool] = Field(None, alias="isActive")
    asset_type_id: Optional[StrictStr] = Field(None, alias="assetTypeId")
    asset_type_name: Optional[StrictStr] = Field(None, alias="assetTypeName")
    type: StrictStr = Field(...)
    ratio: Optional[StrictStr] = None
    validate_by: StrictStr = Field(..., alias="validateBy")
    pattern: Optional[StrictStr] = None
    min: Optional[StrictInt] = None
    max: Optional[StrictInt] = None
    color_depth: Optional[conlist(StrictStr)] = Field(None, alias="colorDepth")
    color_space: Optional[conlist(StrictStr)] = Field(None, alias="colorSpace")
    min_width: Optional[StrictInt] = Field(None, alias="minWidth")
    min_height: Optional[StrictInt] = Field(None, alias="minHeight")
    extension: Optional[conlist(StrictStr)] = None
    mime_list: Optional[conlist(StrictStr)] = Field(None, alias="mimeList")
    __properties = ["id", "deleted", "name", "createdAt", "modifiedAt", "createdById", "createdByName", "modifiedById", "modifiedByName", "isActive", "assetTypeId", "assetTypeName", "type", "ratio", "validateBy", "pattern", "min", "max", "colorDepth", "colorSpace", "minWidth", "minHeight", "extension", "mimeList"]

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
    def from_json(cls, json_str: str) -> ValidationRule:
        """Create an instance of ValidationRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValidationRule:
        """Create an instance of ValidationRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidationRule.parse_obj(obj)

        _obj = ValidationRule.parse_obj({
            "id": obj.get("id"),
            "deleted": obj.get("deleted"),
            "name": obj.get("name"),
            "created_at": obj.get("createdAt"),
            "modified_at": obj.get("modifiedAt"),
            "created_by_id": obj.get("createdById"),
            "created_by_name": obj.get("createdByName"),
            "modified_by_id": obj.get("modifiedById"),
            "modified_by_name": obj.get("modifiedByName"),
            "is_active": obj.get("isActive"),
            "asset_type_id": obj.get("assetTypeId"),
            "asset_type_name": obj.get("assetTypeName"),
            "type": obj.get("type"),
            "ratio": obj.get("ratio"),
            "validate_by": obj.get("validateBy"),
            "pattern": obj.get("pattern"),
            "min": obj.get("min"),
            "max": obj.get("max"),
            "color_depth": obj.get("colorDepth"),
            "color_space": obj.get("colorSpace"),
            "min_width": obj.get("minWidth"),
            "min_height": obj.get("minHeight"),
            "extension": obj.get("extension"),
            "mime_list": obj.get("mimeList")
        })
        return _obj


