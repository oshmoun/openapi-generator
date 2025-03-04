# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, conlist
from petstore_api.models.read_only_first import ReadOnlyFirst

class ArrayTest(BaseModel):
    """
    ArrayTest
    """
    array_of_string: Optional[conlist(StrictStr, max_items=3, min_items=0)] = None
    array_array_of_integer: Optional[conlist(conlist(StrictInt))] = None
    array_array_of_model: Optional[conlist(conlist(ReadOnlyFirst))] = None
    __properties = ["array_of_string", "array_array_of_integer", "array_array_of_model"]

    """Pydantic configuration"""
    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
    }

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ArrayTest:
        """Create an instance of ArrayTest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in array_array_of_model (list of list)
        _items = []
        if self.array_array_of_model:
            for _item in self.array_array_of_model:
                if _item:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item if _inner_item is not None]
                    )
            _dict['array_array_of_model'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ArrayTest:
        """Create an instance of ArrayTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ArrayTest.parse_obj(obj)

        _obj = ArrayTest.parse_obj({
            "array_of_string": obj.get("array_of_string"),
            "array_array_of_integer": obj.get("array_array_of_integer"),
            "array_array_of_model": [
                    [ReadOnlyFirst.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj.get("array_array_of_model")
                ] if obj.get("array_array_of_model") is not None else None
        })
        return _obj


