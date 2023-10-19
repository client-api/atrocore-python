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
from pydantic import BaseModel, Field, StrictInt, StrictStr

class CreateAssociatedProductItemRequest(BaseModel):
    """
    CreateAssociatedProductItemRequest
    """
    association_id: Optional[StrictStr] = Field(None, alias="associationId")
    main_product_id: Optional[StrictStr] = Field(None, alias="mainProductId")
    related_product_id: Optional[StrictStr] = Field(None, alias="relatedProductId")
    backward_association_id: Optional[StrictStr] = Field(None, alias="backwardAssociationId")
    modified_by_id: Optional[StrictStr] = Field(None, alias="modifiedById")
    sorting: Optional[StrictInt] = None
    main_product_image_id: Optional[StrictStr] = Field(None, alias="mainProductImageId")
    related_product_image_id: Optional[StrictStr] = Field(None, alias="relatedProductImageId")
    __properties = ["associationId", "mainProductId", "relatedProductId", "backwardAssociationId", "modifiedById", "sorting", "mainProductImageId", "relatedProductImageId"]

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
    def from_json(cls, json_str: str) -> CreateAssociatedProductItemRequest:
        """Create an instance of CreateAssociatedProductItemRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateAssociatedProductItemRequest:
        """Create an instance of CreateAssociatedProductItemRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateAssociatedProductItemRequest.parse_obj(obj)

        _obj = CreateAssociatedProductItemRequest.parse_obj({
            "association_id": obj.get("associationId"),
            "main_product_id": obj.get("mainProductId"),
            "related_product_id": obj.get("relatedProductId"),
            "backward_association_id": obj.get("backwardAssociationId"),
            "modified_by_id": obj.get("modifiedById"),
            "sorting": obj.get("sorting"),
            "main_product_image_id": obj.get("mainProductImageId"),
            "related_product_image_id": obj.get("relatedProductImageId")
        })
        return _obj

