# coding: utf-8

"""
    Lambda Cloud API

    API for interacting with the Lambda GPU Cloud  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, constr

class AddSSHKeyRequest(BaseModel):
    """
    The name for the SSH key. Optionally, an existing public key can be supplied for the `public_key` property. If the `public_key` property is omitted, a new key pair is generated. The private key is returned in the response.
    """
    name: constr(strict=True, max_length=64) = Field(..., description="Name of the SSH key")
    public_key: Optional[constr(strict=True, max_length=4096)] = Field(None, description="Public key for the SSH key")
    __properties = ["name", "public_key"]

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
    def from_json(cls, json_str: str) -> AddSSHKeyRequest:
        """Create an instance of AddSSHKeyRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddSSHKeyRequest:
        """Create an instance of AddSSHKeyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddSSHKeyRequest.parse_obj(obj)

        _obj = AddSSHKeyRequest.parse_obj({
            "name": obj.get("name"),
            "public_key": obj.get("public_key")
        })
        return _obj
