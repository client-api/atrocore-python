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

class Notification(BaseModel):
    """
    Notification
    """
    id: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    number: Optional[StrictInt] = None
    data: Optional[Dict[str, Any]] = None
    note_data: Optional[Dict[str, Any]] = Field(None, alias="noteData")
    type: Optional[StrictStr] = None
    read: Optional[StrictBool] = None
    user_id: Optional[StrictStr] = Field(None, alias="userId")
    user_name: Optional[StrictStr] = Field(None, alias="userName")
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    message: Optional[StrictStr] = None
    related_id: Optional[StrictStr] = Field(None, alias="relatedId")
    related_name: Optional[StrictStr] = Field(None, alias="relatedName")
    related_parent_id: Optional[StrictStr] = Field(None, alias="relatedParentId")
    related_parent_name: Optional[StrictStr] = Field(None, alias="relatedParentName")
    __properties = ["id", "deleted", "number", "data", "noteData", "type", "read", "userId", "userName", "createdAt", "message", "relatedId", "relatedName", "relatedParentId", "relatedParentName"]

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
    def from_json(cls, json_str: str) -> Notification:
        """Create an instance of Notification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Notification:
        """Create an instance of Notification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Notification.parse_obj(obj)

        _obj = Notification.parse_obj({
            "id": obj.get("id"),
            "deleted": obj.get("deleted"),
            "number": obj.get("number"),
            "data": obj.get("data"),
            "note_data": obj.get("noteData"),
            "type": obj.get("type"),
            "read": obj.get("read"),
            "user_id": obj.get("userId"),
            "user_name": obj.get("userName"),
            "created_at": obj.get("createdAt"),
            "message": obj.get("message"),
            "related_id": obj.get("relatedId"),
            "related_name": obj.get("relatedName"),
            "related_parent_id": obj.get("relatedParentId"),
            "related_parent_name": obj.get("relatedParentName")
        })
        return _obj


