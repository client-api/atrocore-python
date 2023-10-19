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

class Product(BaseModel):
    """
    Product
    """
    id: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    name: StrictStr = Field(...)
    name_de_de: StrictStr = Field(..., alias="nameDeDe")
    classifications_ids: Optional[conlist(StrictStr)] = Field(None, alias="classificationsIds")
    classifications_names: Optional[Dict[str, Any]] = Field(None, alias="classificationsNames")
    brand_id: Optional[StrictStr] = Field(None, alias="brandId")
    brand_name: Optional[StrictStr] = Field(None, alias="brandName")
    sku: Optional[StrictStr] = None
    is_active: Optional[StrictBool] = Field(None, alias="isActive")
    amount: Optional[StrictStr] = None
    price: Optional[StrictStr] = None
    price_currency: Optional[StrictStr] = Field(None, alias="priceCurrency")
    product_status: StrictStr = Field(..., alias="productStatus")
    tax_id: Optional[StrictStr] = Field(None, alias="taxId")
    tax_name: Optional[StrictStr] = Field(None, alias="taxName")
    ean: Optional[StrictStr] = None
    mpn: Optional[StrictStr] = None
    packaging_id: Optional[StrictStr] = Field(None, alias="packagingId")
    packaging_name: Optional[StrictStr] = Field(None, alias="packagingName")
    uvp: Optional[StrictStr] = None
    tag: Optional[conlist(StrictStr)] = None
    long_description: Optional[StrictStr] = Field(None, alias="longDescription")
    long_description_de_de: Optional[StrictStr] = Field(None, alias="longDescriptionDeDe")
    product_serie_id: Optional[StrictStr] = Field(None, alias="productSerieId")
    product_serie_name: Optional[StrictStr] = Field(None, alias="productSerieName")
    parents_ids: Optional[conlist(StrictStr)] = Field(None, alias="parentsIds")
    parents_names: Optional[Dict[str, Any]] = Field(None, alias="parentsNames")
    sort_order: Optional[StrictInt] = Field(None, alias="sortOrder")
    data: Optional[Dict[str, Any]] = None
    catalog_id: Optional[StrictStr] = Field(None, alias="catalogId")
    catalog_name: Optional[StrictStr] = Field(None, alias="catalogName")
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
    sorting: Optional[StrictInt] = None
    contents_ids: Optional[conlist(StrictStr)] = Field(None, alias="contentsIds")
    contents_names: Optional[Dict[str, Any]] = Field(None, alias="contentsNames")
    is_inherit_assigned_user: Optional[StrictBool] = Field(None, alias="isInheritAssignedUser")
    is_inherit_owner_user: Optional[StrictBool] = Field(None, alias="isInheritOwnerUser")
    is_inherit_teams: Optional[StrictBool] = Field(None, alias="isInheritTeams")
    task_status: Optional[conlist(StrictStr)] = Field(None, alias="taskStatus")
    attachments: Optional[StrictStr] = None
    __properties = ["id", "deleted", "name", "nameDeDe", "classificationsIds", "classificationsNames", "brandId", "brandName", "sku", "isActive", "amount", "price", "priceCurrency", "productStatus", "taxId", "taxName", "ean", "mpn", "packagingId", "packagingName", "uvp", "tag", "longDescription", "longDescriptionDeDe", "productSerieId", "productSerieName", "parentsIds", "parentsNames", "sortOrder", "data", "catalogId", "catalogName", "createdAt", "modifiedAt", "createdById", "createdByName", "modifiedById", "modifiedByName", "ownerUserId", "ownerUserName", "assignedUserId", "assignedUserName", "teamsIds", "teamsNames", "sorting", "contentsIds", "contentsNames", "isInheritAssignedUser", "isInheritOwnerUser", "isInheritTeams", "taskStatus", "attachments"]

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
    def from_json(cls, json_str: str) -> Product:
        """Create an instance of Product from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Product:
        """Create an instance of Product from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Product.parse_obj(obj)

        _obj = Product.parse_obj({
            "id": obj.get("id"),
            "deleted": obj.get("deleted"),
            "name": obj.get("name"),
            "name_de_de": obj.get("nameDeDe"),
            "classifications_ids": obj.get("classificationsIds"),
            "classifications_names": obj.get("classificationsNames"),
            "brand_id": obj.get("brandId"),
            "brand_name": obj.get("brandName"),
            "sku": obj.get("sku"),
            "is_active": obj.get("isActive"),
            "amount": obj.get("amount"),
            "price": obj.get("price"),
            "price_currency": obj.get("priceCurrency"),
            "product_status": obj.get("productStatus"),
            "tax_id": obj.get("taxId"),
            "tax_name": obj.get("taxName"),
            "ean": obj.get("ean"),
            "mpn": obj.get("mpn"),
            "packaging_id": obj.get("packagingId"),
            "packaging_name": obj.get("packagingName"),
            "uvp": obj.get("uvp"),
            "tag": obj.get("tag"),
            "long_description": obj.get("longDescription"),
            "long_description_de_de": obj.get("longDescriptionDeDe"),
            "product_serie_id": obj.get("productSerieId"),
            "product_serie_name": obj.get("productSerieName"),
            "parents_ids": obj.get("parentsIds"),
            "parents_names": obj.get("parentsNames"),
            "sort_order": obj.get("sortOrder"),
            "data": obj.get("data"),
            "catalog_id": obj.get("catalogId"),
            "catalog_name": obj.get("catalogName"),
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
            "sorting": obj.get("sorting"),
            "contents_ids": obj.get("contentsIds"),
            "contents_names": obj.get("contentsNames"),
            "is_inherit_assigned_user": obj.get("isInheritAssignedUser"),
            "is_inherit_owner_user": obj.get("isInheritOwnerUser"),
            "is_inherit_teams": obj.get("isInheritTeams"),
            "task_status": obj.get("taskStatus"),
            "attachments": obj.get("attachments")
        })
        return _obj

