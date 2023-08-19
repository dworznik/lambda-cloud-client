# coding: utf-8

"""
    Lambda Cloud API

    API for interacting with the Lambda GPU Cloud  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ErrorCode(str, Enum):
    """
    Unique identifier for the type of error
    """

    """
    allowed enum values
    """
    GLOBAL_SLASH_UNKNOWN = 'global/unknown'
    GLOBAL_SLASH_INVALID_MINUS_API_MINUS_KEY = 'global/invalid-api-key'
    GLOBAL_SLASH_ACCOUNT_MINUS_INACTIVE = 'global/account-inactive'
    GLOBAL_SLASH_INVALID_MINUS_PARAMETERS = 'global/invalid-parameters'
    GLOBAL_SLASH_OBJECT_MINUS_DOES_MINUS_NOT_MINUS_EXIST = 'global/object-does-not-exist'
    INSTANCE_MINUS_OPERATIONS_SLASH_LAUNCH_SLASH_INSUFFICIENT_MINUS_CAPACITY = 'instance-operations/launch/insufficient-capacity'
    INSTANCE_MINUS_OPERATIONS_SLASH_LAUNCH_SLASH_FILE_MINUS_SYSTEM_MINUS_IN_MINUS_WRONG_MINUS_REGION = 'instance-operations/launch/file-system-in-wrong-region'
    INSTANCE_MINUS_OPERATIONS_SLASH_LAUNCH_SLASH_FILE_MINUS_SYSTEMS_MINUS_NOT_MINUS_SUPPORTED = 'instance-operations/launch/file-systems-not-supported'
    SSH_MINUS_KEYS_SLASH_KEY_MINUS_IN_MINUS_USE = 'ssh-keys/key-in-use'

    @classmethod
    def from_json(cls, json_str: str) -> ErrorCode:
        """Create an instance of ErrorCode from a JSON string"""
        return ErrorCode(json.loads(json_str))


