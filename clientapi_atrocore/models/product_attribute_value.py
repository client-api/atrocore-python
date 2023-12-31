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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

class ProductAttributeValue(BaseModel):
    """
    ProductAttributeValue
    """
    id: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    product_id: Optional[StrictStr] = Field(None, alias="productId")
    product_name: Optional[StrictStr] = Field(None, alias="productName")
    attribute_id: Optional[StrictStr] = Field(None, alias="attributeId")
    attribute_name: Optional[StrictStr] = Field(None, alias="attributeName")
    language: Optional[StrictStr] = None
    scope: StrictStr = Field(...)
    channel_id: Optional[StrictStr] = Field(None, alias="channelId")
    channel_name: Optional[StrictStr] = Field(None, alias="channelName")
    is_variant_specific_attribute: Optional[StrictBool] = Field(None, alias="isVariantSpecificAttribute")
    count_bytes_instead_of_characters: Optional[StrictBool] = Field(None, alias="countBytesInsteadOfCharacters")
    amount_of_digits_after_comma: Optional[StrictInt] = Field(None, alias="amountOfDigitsAfterComma")
    value: Optional[StrictStr] = None
    attribute_type: Optional[StrictStr] = Field(None, alias="attributeType")
    attribute_asset_type: Optional[StrictStr] = Field(None, alias="attributeAssetType")
    attribute_tooltip: Optional[StrictStr] = Field(None, alias="attributeTooltip")
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    modified_at: Optional[StrictStr] = Field(None, alias="modifiedAt")
    created_by_id: Optional[StrictStr] = Field(None, alias="createdById")
    created_by_name: Optional[StrictStr] = Field(None, alias="createdByName")
    modified_by_id: Optional[StrictStr] = Field(None, alias="modifiedById")
    modified_by_name: Optional[StrictStr] = Field(None, alias="modifiedByName")
    is_inherit_assigned_user: Optional[StrictBool] = Field(None, alias="isInheritAssignedUser")
    is_inherit_owner_user: Optional[StrictBool] = Field(None, alias="isInheritOwnerUser")
    is_inherit_teams: Optional[StrictBool] = Field(None, alias="isInheritTeams")
    owner_user_id: Optional[StrictStr] = Field(None, alias="ownerUserId")
    owner_user_name: Optional[StrictStr] = Field(None, alias="ownerUserName")
    assigned_user_id: Optional[StrictStr] = Field(None, alias="assignedUserId")
    assigned_user_name: Optional[StrictStr] = Field(None, alias="assignedUserName")
    teams_ids: Optional[conlist(StrictStr)] = Field(None, alias="teamsIds")
    teams_names: Optional[Dict[str, Any]] = Field(None, alias="teamsNames")
    __properties = ["id", "deleted", "productId", "productName", "attributeId", "attributeName", "language", "scope", "channelId", "channelName", "isVariantSpecificAttribute", "countBytesInsteadOfCharacters", "amountOfDigitsAfterComma", "value", "attributeType", "attributeAssetType", "attributeTooltip", "createdAt", "modifiedAt", "createdById", "createdByName", "modifiedById", "modifiedByName", "isInheritAssignedUser", "isInheritOwnerUser", "isInheritTeams", "ownerUserId", "ownerUserName", "assignedUserId", "assignedUserName", "teamsIds", "teamsNames"]

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
    def from_json(cls, json_str: str) -> ProductAttributeValue:
        """Create an instance of ProductAttributeValue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProductAttributeValue:
        """Create an instance of ProductAttributeValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProductAttributeValue.parse_obj(obj)

        _obj = ProductAttributeValue.parse_obj({
            "id": obj.get("id"),
            "deleted": obj.get("deleted"),
            "product_id": obj.get("productId"),
            "product_name": obj.get("productName"),
            "attribute_id": obj.get("attributeId"),
            "attribute_name": obj.get("attributeName"),
            "language": obj.get("language"),
            "scope": obj.get("scope"),
            "channel_id": obj.get("channelId"),
            "channel_name": obj.get("channelName"),
            "is_variant_specific_attribute": obj.get("isVariantSpecificAttribute"),
            "count_bytes_instead_of_characters": obj.get("countBytesInsteadOfCharacters"),
            "amount_of_digits_after_comma": obj.get("amountOfDigitsAfterComma"),
            "value": obj.get("value"),
            "attribute_type": obj.get("attributeType"),
            "attribute_asset_type": obj.get("attributeAssetType"),
            "attribute_tooltip": obj.get("attributeTooltip"),
            "created_at": obj.get("createdAt"),
            "modified_at": obj.get("modifiedAt"),
            "created_by_id": obj.get("createdById"),
            "created_by_name": obj.get("createdByName"),
            "modified_by_id": obj.get("modifiedById"),
            "modified_by_name": obj.get("modifiedByName"),
            "is_inherit_assigned_user": obj.get("isInheritAssignedUser"),
            "is_inherit_owner_user": obj.get("isInheritOwnerUser"),
            "is_inherit_teams": obj.get("isInheritTeams"),
            "owner_user_id": obj.get("ownerUserId"),
            "owner_user_name": obj.get("ownerUserName"),
            "assigned_user_id": obj.get("assignedUserId"),
            "assigned_user_name": obj.get("assignedUserName"),
            "teams_ids": obj.get("teamsIds"),
            "teams_names": obj.get("teamsNames")
        })
        return _obj


