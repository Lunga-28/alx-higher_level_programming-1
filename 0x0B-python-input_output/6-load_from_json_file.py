#!/usr/bin/python3
"""
Load from JSON
"""

import json


def load_from_json_file(filename):
    """
    Load from Json file
    """
  
    with open(filename, "r") as f:
        return json.load(f)
