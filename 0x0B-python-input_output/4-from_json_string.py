#!/usr/bin/python3
"""
json module imported
The from_json_string module
"""
import json


def from_json_string(my_str):
    """
    from_json_string funcion
    returns an object (Python data structure)
    represented by a JSON string

    Args:
        @my_str: JSON string to be converted
    """
    return json.loads(my_str)
