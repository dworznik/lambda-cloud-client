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
from pydantic import BaseModel, Field, StrictStr
from lambda_cloud_client.models.error_code import ErrorCode

class Error(BaseModel):
    """
    Error
    """
    code: ErrorCode = Field(...)
    message: StrictStr = Field(..., description="Detailed description of the error")
    suggestion: Optional[StrictStr] = Field(None, description="Suggestion of possible ways to fix the error.")
    __properties = ["code", "message", "suggestion"]

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
    def from_json(cls, json_str: str) -> Error:
        """Create an instance of Error from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if suggestion (nullable) is None
        # and __fields_set__ contains the field
        if self.suggestion is None and "suggestion" in self.__fields_set__:
            _dict['suggestion'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Error:
        """Create an instance of Error from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Error.parse_obj(obj)

        _obj = Error.parse_obj({
            "code": obj.get("code"),
            "message": obj.get("message"),
            "suggestion": obj.get("suggestion")
        })
        return _obj
