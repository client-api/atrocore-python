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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class GetModulesLogs200ResponseListInner(BaseModel):
    """
    GetModulesLogs200ResponseListInner
    """
    id: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    post: Optional[StrictStr] = None
    data: Optional[Dict[str, Any]] = None
    type: Optional[StrictStr] = None
    target_type: Optional[StrictStr] = Field(None, alias="targetType")
    parent_id: Optional[StrictStr] = Field(None, alias="parentId")
    parent_name: Optional[StrictStr] = Field(None, alias="parentName")
    related_id: Optional[StrictStr] = Field(None, alias="relatedId")
    related_name: Optional[StrictStr] = Field(None, alias="relatedName")
    attachments: Optional[StrictStr] = None
    number: Optional[StrictInt] = None
    is_global: Optional[StrictBool] = Field(None, alias="isGlobal")
    created_by_gender: Optional[StrictStr] = Field(None, alias="createdByGender")
    notified_user_id_list: Optional[Dict[str, Any]] = Field(None, alias="notifiedUserIdList")
    is_internal: Optional[StrictBool] = Field(None, alias="isInternal")
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    modified_at: Optional[StrictStr] = Field(None, alias="modifiedAt")
    created_by_id: Optional[StrictStr] = Field(None, alias="createdById")
    created_by_name: Optional[StrictStr] = Field(None, alias="createdByName")
    modified_by_id: Optional[StrictStr] = Field(None, alias="modifiedById")
    modified_by_name: Optional[StrictStr] = Field(None, alias="modifiedByName")
    attribute_id: Optional[StrictStr] = Field(None, alias="attributeId")
    pav_id: Optional[StrictStr] = Field(None, alias="pavId")
    __properties = ["id", "deleted", "post", "data", "type", "targetType", "parentId", "parentName", "relatedId", "relatedName", "attachments", "number", "isGlobal", "createdByGender", "notifiedUserIdList", "isInternal", "createdAt", "modifiedAt", "createdById", "createdByName", "modifiedById", "modifiedByName", "attributeId", "pavId"]

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
    def from_json(cls, json_str: str) -> GetModulesLogs200ResponseListInner:
        """Create an instance of GetModulesLogs200ResponseListInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetModulesLogs200ResponseListInner:
        """Create an instance of GetModulesLogs200ResponseListInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetModulesLogs200ResponseListInner.parse_obj(obj)

        _obj = GetModulesLogs200ResponseListInner.parse_obj({
            "id": obj.get("id"),
            "deleted": obj.get("deleted"),
            "post": obj.get("post"),
            "data": obj.get("data"),
            "type": obj.get("type"),
            "target_type": obj.get("targetType"),
            "parent_id": obj.get("parentId"),
            "parent_name": obj.get("parentName"),
            "related_id": obj.get("relatedId"),
            "related_name": obj.get("relatedName"),
            "attachments": obj.get("attachments"),
            "number": obj.get("number"),
            "is_global": obj.get("isGlobal"),
            "created_by_gender": obj.get("createdByGender"),
            "notified_user_id_list": obj.get("notifiedUserIdList"),
            "is_internal": obj.get("isInternal"),
            "created_at": obj.get("createdAt"),
            "modified_at": obj.get("modifiedAt"),
            "created_by_id": obj.get("createdById"),
            "created_by_name": obj.get("createdByName"),
            "modified_by_id": obj.get("modifiedById"),
            "modified_by_name": obj.get("modifiedByName"),
            "attribute_id": obj.get("attributeId"),
            "pav_id": obj.get("pavId")
        })
        return _obj


