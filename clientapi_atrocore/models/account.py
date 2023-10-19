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

class Account(BaseModel):
    """
    Account
    """
    id: Optional[StrictStr] = None
    deleted: Optional[StrictBool] = None
    name: StrictStr = Field(...)
    description: Optional[StrictStr] = None
    email_address: Optional[StrictStr] = Field(None, alias="emailAddress")
    phone_number: Optional[StrictStr] = Field(None, alias="phoneNumber")
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    modified_at: Optional[StrictStr] = Field(None, alias="modifiedAt")
    created_by_id: Optional[StrictStr] = Field(None, alias="createdById")
    created_by_name: Optional[StrictStr] = Field(None, alias="createdByName")
    modified_by_id: Optional[StrictStr] = Field(None, alias="modifiedById")
    modified_by_name: Optional[StrictStr] = Field(None, alias="modifiedByName")
    assigned_user_id: Optional[StrictStr] = Field(None, alias="assignedUserId")
    assigned_user_name: Optional[StrictStr] = Field(None, alias="assignedUserName")
    teams_ids: Optional[conlist(StrictStr)] = Field(None, alias="teamsIds")
    teams_names: Optional[Dict[str, Any]] = Field(None, alias="teamsNames")
    channel_id: Optional[StrictStr] = Field(None, alias="channelId")
    channel_name: Optional[StrictStr] = Field(None, alias="channelName")
    assigned_import_feeds_ids: Optional[conlist(StrictStr)] = Field(None, alias="assignedImportFeedsIds")
    assigned_import_feeds_names: Optional[Dict[str, Any]] = Field(None, alias="assignedImportFeedsNames")
    assigned_export_feeds_ids: Optional[conlist(StrictStr)] = Field(None, alias="assignedExportFeedsIds")
    assigned_export_feeds_names: Optional[Dict[str, Any]] = Field(None, alias="assignedExportFeedsNames")
    __properties = ["id", "deleted", "name", "description", "emailAddress", "phoneNumber", "createdAt", "modifiedAt", "createdById", "createdByName", "modifiedById", "modifiedByName", "assignedUserId", "assignedUserName", "teamsIds", "teamsNames", "channelId", "channelName", "assignedImportFeedsIds", "assignedImportFeedsNames", "assignedExportFeedsIds", "assignedExportFeedsNames"]

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
    def from_json(cls, json_str: str) -> Account:
        """Create an instance of Account from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Account:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Account.parse_obj(obj)

        _obj = Account.parse_obj({
            "id": obj.get("id"),
            "deleted": obj.get("deleted"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "email_address": obj.get("emailAddress"),
            "phone_number": obj.get("phoneNumber"),
            "created_at": obj.get("createdAt"),
            "modified_at": obj.get("modifiedAt"),
            "created_by_id": obj.get("createdById"),
            "created_by_name": obj.get("createdByName"),
            "modified_by_id": obj.get("modifiedById"),
            "modified_by_name": obj.get("modifiedByName"),
            "assigned_user_id": obj.get("assignedUserId"),
            "assigned_user_name": obj.get("assignedUserName"),
            "teams_ids": obj.get("teamsIds"),
            "teams_names": obj.get("teamsNames"),
            "channel_id": obj.get("channelId"),
            "channel_name": obj.get("channelName"),
            "assigned_import_feeds_ids": obj.get("assignedImportFeedsIds"),
            "assigned_import_feeds_names": obj.get("assignedImportFeedsNames"),
            "assigned_export_feeds_ids": obj.get("assignedExportFeedsIds"),
            "assigned_export_feeds_names": obj.get("assignedExportFeedsNames")
        })
        return _obj


