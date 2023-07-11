#!/usr/bin/python3
"""
Json representation
"""

import json


def to_json_string(my_obj):
    """
    JSON Representation
    """
  
    data = json.dumps(my_obj)
    return data
