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



from pydantic import BaseModel, Field, StrictInt, StrictStr
from lambda_cloud_client.models.instance_type_specs import InstanceTypeSpecs

class InstanceType(BaseModel):
    """
    Hardware configuration and pricing of an instance type
    """
    name: StrictStr = Field(..., description="Name of an instance type")
    description: StrictStr = Field(..., description="Long name of the instance type")
    price_cents_per_hour: StrictInt = Field(..., description="Price of the instance type, in US cents per hour")
    specs: InstanceTypeSpecs = Field(...)
    __properties = ["name", "description", "price_cents_per_hour", "specs"]

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
    def from_json(cls, json_str: str) -> InstanceType:
        """Create an instance of InstanceType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of specs
        if self.specs:
            _dict['specs'] = self.specs.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InstanceType:
        """Create an instance of InstanceType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstanceType.parse_obj(obj)

        _obj = InstanceType.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "price_cents_per_hour": obj.get("price_cents_per_hour"),
            "specs": InstanceTypeSpecs.from_dict(obj.get("specs")) if obj.get("specs") is not None else None
        })
        return _obj
