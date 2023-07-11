#!/usr/bin/python3
"""
decoding
"""
import json


def from_json_string(my_str):
    """
    JSON String deserialization/decoding
    """

  
    data = json.loads(my_str)
    return data
