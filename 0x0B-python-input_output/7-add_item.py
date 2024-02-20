#!/usr/bin/python3
"""
json module imported
The add_item module
"""
import sys
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').\
    load_from_json_file


def add_item(args, filename):
    """
    add_item - adds all items and saves to a JSON file
    Args:
        @args: arguments that to be added.
        @filename: file to be updated
    """
    try:
        items = load_from_json(filename)

    except FileNotFoundError:
        items = []

    for item in args:
        items.append(item)
    save_to_json(items, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
