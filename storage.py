"""
Program: Grocery_Store_Checklist
Author: Ankith Srivathsan
Purpose: Saves and loads the grocery list as a JSON file.
Starter code: None, written using concepts from chapters 1-11
Date: November 4th, 2026
"""

import json

SAVE_FILE = "grocery_list.json"


def save_list(grocery_list, filename=SAVE_FILE):
    """Write the grocery list to a JSON file."""
    with open(filename, "w") as file:
        json.dump(grocery_list.to_dict_list(), file, indent=4)