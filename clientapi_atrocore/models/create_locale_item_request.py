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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class CreateLocaleItemRequest(BaseModel):
    """
    CreateLocaleItemRequest
    """
    name: StrictStr = Field(...)
    description: Optional[StrictStr] = None
    language: StrictStr = Field(...)
    decimal_mark: StrictStr = Field(..., alias="decimalMark")
    time_format: StrictStr = Field(..., alias="timeFormat")
    thousand_separator: Optional[StrictStr] = Field(None, alias="thousandSeparator")
    week_start: StrictStr = Field(..., alias="weekStart")
    date_format: StrictStr = Field(..., alias="dateFormat")
    time_zone: StrictStr = Field(..., alias="timeZone")
    modified_by_id: Optional[StrictStr] = Field(None, alias="modifiedById")
    __properties = ["name", "description", "language", "decimalMark", "timeFormat", "thousandSeparator", "weekStart", "dateFormat", "timeZone", "modifiedById"]

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
    def from_json(cls, json_str: str) -> CreateLocaleItemRequest:
        """Create an instance of CreateLocaleItemRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateLocaleItemRequest:
        """Create an instance of CreateLocaleItemRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateLocaleItemRequest.parse_obj(obj)

        _obj = CreateLocaleItemRequest.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "language": obj.get("language"),
            "decimal_mark": obj.get("decimalMark"),
            "time_format": obj.get("timeFormat"),
            "thousand_separator": obj.get("thousandSeparator"),
            "week_start": obj.get("weekStart"),
            "date_format": obj.get("dateFormat"),
            "time_zone": obj.get("timeZone"),
            "modified_by_id": obj.get("modifiedById")
        })
        return _obj


