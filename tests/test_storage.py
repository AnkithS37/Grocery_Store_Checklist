"""
Program: Grocery_Store_Checklist
Author: Ankith Srivathsan
Purpose: Tests for saving and loading the grocery list.
Starter code: None, written using concepts from chapters 1-11
Date: November 4th, 2026
"""

from grocery_list import GroceryList
from storage import save_list, load_list


def test_save_then_load_keeps_items(tmp_path):
    """A saved list should load back with the same items."""
    filename = tmp_path / "list.json"
    grocery_list = GroceryList()
    grocery_list.add_item("milk", "Dairy")
    grocery_list.check_off_item("milk")
    save_list(grocery_list, filename)

    loaded_list = load_list(filename)
    assert loaded_list.total_count() == 1
    assert loaded_list.checked_count() == 1

def test_load_missing_file_gives_empty_list(tmp_path):
    """Loading a file that does not exist should give an empty list."""
    filename = tmp_path / "missing.json"
    assert load_list(filename).total_count() == 0

def test_load_damaged_file_gives_empty_list(tmp_path):
    """Loading a file with broken JSON should give an empty list."""
    filename = tmp_path / "bad.json"
    filename.write_text("oops")
    assert load_list(filename).total_count() == 0