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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class Tax(BaseModel):
    """
    Tax
    """
    id: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    name: StrictStr = Field(...)
    name_de_de: StrictStr = Field(..., alias="nameDeDe")
    value: StrictStr = Field(...)
    is_active: Optional[StrictBool] = Field(None, alias="isActive")
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    modified_at: Optional[StrictStr] = Field(None, alias="modifiedAt")
    created_by_id: Optional[StrictStr] = Field(None, alias="createdById")
    created_by_name: Optional[StrictStr] = Field(None, alias="createdByName")
    modified_by_id: Optional[StrictStr] = Field(None, alias="modifiedById")
    modified_by_name: Optional[StrictStr] = Field(None, alias="modifiedByName")
    owner_user_id: Optional[StrictStr] = Field(None, alias="ownerUserId")
    owner_user_name: Optional[StrictStr] = Field(None, alias="ownerUserName")
    assigned_user_id: Optional[StrictStr] = Field(None, alias="assignedUserId")
    assigned_user_name: Optional[StrictStr] = Field(None, alias="assignedUserName")
    teams_ids: Optional[conlist(StrictStr)] = Field(None, alias="teamsIds")
    teams_names: Optional[Dict[str, Any]] = Field(None, alias="teamsNames")
    products_ids: Optional[conlist(StrictStr)] = Field(None, alias="productsIds")
    products_names: Optional[Dict[str, Any]] = Field(None, alias="productsNames")
    __properties = ["id", "deleted", "name", "nameDeDe", "value", "isActive", "createdAt", "modifiedAt", "createdById", "createdByName", "modifiedById", "modifiedByName", "ownerUserId", "ownerUserName", "assignedUserId", "assignedUserName", "teamsIds", "teamsNames", "productsIds", "productsNames"]

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
    def from_json(cls, json_str: str) -> Tax:
        """Create an instance of Tax from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Tax:
        """Create an instance of Tax from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Tax.parse_obj(obj)

        _obj = Tax.parse_obj({
            "id": obj.get("id"),
            "deleted": obj.get("deleted"),
            "name": obj.get("name"),
            "name_de_de": obj.get("nameDeDe"),
            "value": obj.get("value"),
            "is_active": obj.get("isActive"),
            "created_at": obj.get("createdAt"),
            "modified_at": obj.get("modifiedAt"),
            "created_by_id": obj.get("createdById"),
            "created_by_name": obj.get("createdByName"),
            "modified_by_id": obj.get("modifiedById"),
            "modified_by_name": obj.get("modifiedByName"),
            "owner_user_id": obj.get("ownerUserId"),
            "owner_user_name": obj.get("ownerUserName"),
            "assigned_user_id": obj.get("assignedUserId"),
            "assigned_user_name": obj.get("assignedUserName"),
            "teams_ids": obj.get("teamsIds"),
            "teams_names": obj.get("teamsNames"),
            "products_ids": obj.get("productsIds"),
            "products_names": obj.get("productsNames")
        })
        return _obj


