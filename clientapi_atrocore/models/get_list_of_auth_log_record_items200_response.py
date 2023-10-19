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
from pydantic import BaseModel, StrictInt, conlist
from clientapi_atrocore.models.auth_log_record import AuthLogRecord

class GetListOfAuthLogRecordItems200Response(BaseModel):
    """
    GetListOfAuthLogRecordItems200Response
    """
    total: Optional[StrictInt] = None
    list: Optional[conlist(AuthLogRecord)] = None
    __properties = ["total", "list"]

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
    def from_json(cls, json_str: str) -> GetListOfAuthLogRecordItems200Response:
        """Create an instance of GetListOfAuthLogRecordItems200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in list (list)
        _items = []
        if self.list:
            for _item in self.list:
                if _item:
                    _items.append(_item.to_dict())
            _dict['list'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetListOfAuthLogRecordItems200Response:
        """Create an instance of GetListOfAuthLogRecordItems200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetListOfAuthLogRecordItems200Response.parse_obj(obj)

        _obj = GetListOfAuthLogRecordItems200Response.parse_obj({
            "total": obj.get("total"),
            "list": [AuthLogRecord.from_dict(_item) for _item in obj.get("list")] if obj.get("list") is not None else None
        })
        return _obj


