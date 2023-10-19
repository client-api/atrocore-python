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

class ProductChannel(BaseModel):
    """
    ProductChannel
    """
    id: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    modified_at: Optional[StrictStr] = Field(None, alias="modifiedAt")
    created_by_id: Optional[StrictStr] = Field(None, alias="createdById")
    created_by_name: Optional[StrictStr] = Field(None, alias="createdByName")
    modified_by_id: Optional[StrictStr] = Field(None, alias="modifiedById")
    modified_by_name: Optional[StrictStr] = Field(None, alias="modifiedByName")
    product_id: Optional[StrictStr] = Field(None, alias="productId")
    product_name: Optional[StrictStr] = Field(None, alias="productName")
    channel_id: Optional[StrictStr] = Field(None, alias="channelId")
    channel_name: Optional[StrictStr] = Field(None, alias="channelName")
    is_active: Optional[StrictBool] = Field(None, alias="isActive")
    __properties = ["id", "deleted", "createdAt", "modifiedAt", "createdById", "createdByName", "modifiedById", "modifiedByName", "productId", "productName", "channelId", "channelName", "isActive"]

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
    def from_json(cls, json_str: str) -> ProductChannel:
        """Create an instance of ProductChannel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductChannel:
        """Create an instance of ProductChannel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductChannel.parse_obj(obj)

        _obj = ProductChannel.parse_obj({
            "id": obj.get("id"),
            "deleted": obj.get("deleted"),
            "created_at": obj.get("createdAt"),
            "modified_at": obj.get("modifiedAt"),
            "created_by_id": obj.get("createdById"),
            "created_by_name": obj.get("createdByName"),
            "modified_by_id": obj.get("modifiedById"),
            "modified_by_name": obj.get("modifiedByName"),
            "product_id": obj.get("productId"),
            "product_name": obj.get("productName"),
            "channel_id": obj.get("channelId"),
            "channel_name": obj.get("channelName"),
            "is_active": obj.get("isActive")
        })
        return _obj


