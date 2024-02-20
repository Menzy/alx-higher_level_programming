#!/usr/bin/python3
"""The append_write module"""


def append_write(filename="", text=""):
    """append_write funcion definition"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
