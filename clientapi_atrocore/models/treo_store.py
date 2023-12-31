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

class TreoStore(BaseModel):
    """
    TreoStore
    """
    id: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    name: StrictStr = Field(...)
    description: Optional[StrictStr] = None
    package_id: Optional[StrictStr] = Field(None, alias="packageId")
    url: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    versions: Optional[Dict[str, Any]] = None
    tags: Optional[conlist(StrictStr)] = None
    __properties = ["id", "deleted", "name", "description", "packageId", "url", "status", "versions", "tags"]

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
    def from_json(cls, json_str: str) -> TreoStore:
        """Create an instance of TreoStore from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TreoStore:
        """Create an instance of TreoStore from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TreoStore.parse_obj(obj)

        _obj = TreoStore.parse_obj({
            "id": obj.get("id"),
            "deleted": obj.get("deleted"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "package_id": obj.get("packageId"),
            "url": obj.get("url"),
            "status": obj.get("status"),
            "versions": obj.get("versions"),
            "tags": obj.get("tags")
        })
        return _obj


