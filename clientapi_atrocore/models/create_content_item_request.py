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
from pydantic import BaseModel, Field, StrictStr, conlist

class CreateContentItemRequest(BaseModel):
    """
    CreateContentItemRequest
    """
    tags: Optional[conlist(StrictStr)] = None
    name: StrictStr = Field(...)
    status: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    text: Optional[StrictStr] = None
    meta_title: Optional[StrictStr] = Field(None, alias="metaTitle")
    meta_description: Optional[StrictStr] = Field(None, alias="metaDescription")
    products_ids: Optional[conlist(StrictStr)] = Field(None, alias="productsIds")
    content_group_id: Optional[StrictStr] = Field(None, alias="contentGroupId")
    modified_by_id: Optional[StrictStr] = Field(None, alias="modifiedById")
    owner_user_id: Optional[StrictStr] = Field(None, alias="ownerUserId")
    assigned_user_id: Optional[StrictStr] = Field(None, alias="assignedUserId")
    teams_ids: Optional[conlist(StrictStr)] = Field(None, alias="teamsIds")
    __properties = ["tags", "name", "status", "type", "description", "text", "metaTitle", "metaDescription", "productsIds", "contentGroupId", "modifiedById", "ownerUserId", "assignedUserId", "teamsIds"]

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
    def from_json(cls, json_str: str) -> CreateContentItemRequest:
        """Create an instance of CreateContentItemRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateContentItemRequest:
        """Create an instance of CreateContentItemRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateContentItemRequest.parse_obj(obj)

        _obj = CreateContentItemRequest.parse_obj({
            "tags": obj.get("tags"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "type": obj.get("type"),
            "description": obj.get("description"),
            "text": obj.get("text"),
            "meta_title": obj.get("metaTitle"),
            "meta_description": obj.get("metaDescription"),
            "products_ids": obj.get("productsIds"),
            "content_group_id": obj.get("contentGroupId"),
            "modified_by_id": obj.get("modifiedById"),
            "owner_user_id": obj.get("ownerUserId"),
            "assigned_user_id": obj.get("assignedUserId"),
            "teams_ids": obj.get("teamsIds")
        })
        return _obj


