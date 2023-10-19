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

class Team(BaseModel):
    """
    Team
    """
    id: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    roles_ids: Optional[conlist(StrictStr)] = Field(None, alias="rolesIds")
    roles_names: Optional[Dict[str, Any]] = Field(None, alias="rolesNames")
    position_list: Optional[conlist(StrictStr)] = Field(None, alias="positionList")
    user_role: Optional[StrictStr] = Field(None, alias="userRole")
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    __properties = ["id", "deleted", "name", "rolesIds", "rolesNames", "positionList", "userRole", "createdAt"]

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
    def from_json(cls, json_str: str) -> Team:
        """Create an instance of Team from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Team:
        """Create an instance of Team from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Team.parse_obj(obj)

        _obj = Team.parse_obj({
            "id": obj.get("id"),
            "deleted": obj.get("deleted"),
            "name": obj.get("name"),
            "roles_ids": obj.get("rolesIds"),
            "roles_names": obj.get("rolesNames"),
            "position_list": obj.get("positionList"),
            "user_role": obj.get("userRole"),
            "created_at": obj.get("createdAt")
        })
        return _obj

