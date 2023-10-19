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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class CreateAuthLogRecordItemRequest(BaseModel):
    """
    CreateAuthLogRecordItemRequest
    """
    username: Optional[StrictStr] = None
    portal_id: Optional[StrictStr] = Field(None, alias="portalId")
    user_id: Optional[StrictStr] = Field(None, alias="userId")
    auth_token_id: Optional[StrictStr] = Field(None, alias="authTokenId")
    ip_address: Optional[StrictStr] = Field(None, alias="ipAddress")
    is_denied: Optional[StrictBool] = Field(None, alias="isDenied")
    denial_reason: Optional[StrictStr] = Field(None, alias="denialReason")
    request_time: Optional[StrictStr] = Field(None, alias="requestTime")
    request_url: Optional[StrictStr] = Field(None, alias="requestUrl")
    request_method: Optional[StrictStr] = Field(None, alias="requestMethod")
    auth_token_is_active: Optional[StrictStr] = Field(None, alias="authTokenIsActive")
    __properties = ["username", "portalId", "userId", "authTokenId", "ipAddress", "isDenied", "denialReason", "requestTime", "requestUrl", "requestMethod", "authTokenIsActive"]

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
    def from_json(cls, json_str: str) -> CreateAuthLogRecordItemRequest:
        """Create an instance of CreateAuthLogRecordItemRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateAuthLogRecordItemRequest:
        """Create an instance of CreateAuthLogRecordItemRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateAuthLogRecordItemRequest.parse_obj(obj)

        _obj = CreateAuthLogRecordItemRequest.parse_obj({
            "username": obj.get("username"),
            "portal_id": obj.get("portalId"),
            "user_id": obj.get("userId"),
            "auth_token_id": obj.get("authTokenId"),
            "ip_address": obj.get("ipAddress"),
            "is_denied": obj.get("isDenied"),
            "denial_reason": obj.get("denialReason"),
            "request_time": obj.get("requestTime"),
            "request_url": obj.get("requestUrl"),
            "request_method": obj.get("requestMethod"),
            "auth_token_is_active": obj.get("authTokenIsActive")
        })
        return _obj


