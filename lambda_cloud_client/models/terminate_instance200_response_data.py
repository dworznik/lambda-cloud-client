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


from typing import List
from pydantic import BaseModel, Field, conlist
from lambda_cloud_client.models.instance import Instance

class TerminateInstance200ResponseData(BaseModel):
    """
    TerminateInstance200ResponseData
    """
    terminated_instances: conlist(Instance) = Field(..., description="List of instances that were terminated. Note: this list might not contain all instances requested to be terminated.")
    __properties = ["terminated_instances"]

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
    def from_json(cls, json_str: str) -> TerminateInstance200ResponseData:
        """Create an instance of TerminateInstance200ResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in terminated_instances (list)
        _items = []
        if self.terminated_instances:
            for _item in self.terminated_instances:
                if _item:
                    _items.append(_item.to_dict())
            _dict['terminated_instances'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TerminateInstance200ResponseData:
        """Create an instance of TerminateInstance200ResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TerminateInstance200ResponseData.parse_obj(obj)

        _obj = TerminateInstance200ResponseData.parse_obj({
            "terminated_instances": [Instance.from_dict(_item) for _item in obj.get("terminated_instances")] if obj.get("terminated_instances") is not None else None
        })
        return _obj

