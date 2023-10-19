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

class CreateCatalogItemRequest(BaseModel):
    """
    CreateCatalogItemRequest
    """
    name: StrictStr = Field(...)
    name_de_de: StrictStr = Field(..., alias="nameDeDe")
    code: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    description_de_de: Optional[StrictStr] = Field(None, alias="descriptionDeDe")
    modified_by_id: Optional[StrictStr] = Field(None, alias="modifiedById")
    assigned_user_id: Optional[StrictStr] = Field(None, alias="assignedUserId")
    teams_ids: Optional[conlist(StrictStr)] = Field(None, alias="teamsIds")
    is_active: Optional[StrictBool] = Field(None, alias="isActive")
    products_count: Optional[StrictInt] = Field(None, alias="productsCount")
    __properties = ["name", "nameDeDe", "code", "description", "descriptionDeDe", "modifiedById", "assignedUserId", "teamsIds", "isActive", "productsCount"]

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
    def from_json(cls, json_str: str) -> CreateCatalogItemRequest:
        """Create an instance of CreateCatalogItemRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateCatalogItemRequest:
        """Create an instance of CreateCatalogItemRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateCatalogItemRequest.parse_obj(obj)

        _obj = CreateCatalogItemRequest.parse_obj({
            "name": obj.get("name"),
            "name_de_de": obj.get("nameDeDe"),
            "code": obj.get("code"),
            "description": obj.get("description"),
            "description_de_de": obj.get("descriptionDeDe"),
            "modified_by_id": obj.get("modifiedById"),
            "assigned_user_id": obj.get("assignedUserId"),
            "teams_ids": obj.get("teamsIds"),
            "is_active": obj.get("isActive"),
            "products_count": obj.get("productsCount")
        })
        return _obj


