"""
Program: Grocery_Store_Checklist
Author: Ankith Srivathsan
Purpose: Saves and loads the grocery list as a JSON file.
Starter code: None, written using concepts from chapters 1-11
Date: November 4th, 2026
"""

import json

from grocery_item import GroceryItem
from grocery_list import GroceryList

SAVE_FILE = "grocery_list.json"


def save_list(grocery_list, filename=SAVE_FILE):
    """Write the grocery list to a JSON file."""
    with open(filename, "w") as file:
        json.dump(grocery_list.to_dict_list(), file, indent=4)

def load_list(filename=SAVE_FILE):
    """Read a grocery list from a JSON file and return it as a GroceryList.

    If the file is missing or damaged, return an empty GroceryList instead.
    """
    grocery_list = GroceryList()
    try:
        with open(filename) as file:
            saved_items = json.load(file)
    except FileNotFoundError:
        return grocery_list
    except json.JSONDecodeError:
        print("Save file was damaged, starting with an empty list.")
        return grocery_list
    for saved in saved_items:
        item = GroceryItem(saved["name"], saved["category"], saved["checked"])
        grocery_list.items[item.name] = item
    return grocery_list