#!/usr/bin/python3
"""This module adds all arguments to a Python list and saves them to a file."""

# Import the sys module to access command-line arguments.
import sys

# Check if this script is being run directly (not imported).
if __name__ == "__main__":
    
    # Dynamically import the save_to_json_file function from another module.
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    
    # Similarly, dynamically import the load_from_json_file function from another module.
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    # Try to load items from the file "add_item.json".
    try:
        # If the file does not exist, FileNotFoundError will be caught, and items will be initialized as an empty list.
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    
    # Extend the items list with the command-line arguments passed to the script.
    # sys.argv[1:] contains all arguments except the script name itself.
    items.extend(sys.argv[1:])
    
    # Save the updated list of items back to the file "add_item.json".
    save_to_json_file(items, "add_item.json")
