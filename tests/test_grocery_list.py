"""
Program: Grocery_Store_Checklist
Author: Ankith Srivathsan
Purpose: Tests for the GroceryList class.
Starter code: None, written using concepts from chapters 1-11
Date: November 4th, 2026
"""

import pytest

from grocery_list import GroceryList


def test_add_item_puts_item_on_list():
    """Adding an item should increase the total count."""
    grocery_list = GroceryList()
    grocery_list.add_item("milk", "Dairy")
    assert grocery_list.total_count() == 1


def test_add_item_rejects_bad_category():
    """An invalid category should raise a ValueError."""
    grocery_list = GroceryList()
    with pytest.raises(ValueError):
        grocery_list.add_item("milk", "Toys")


def test_remove_item_takes_item_off_list():
    """Removing an item should leave the list empty."""
    grocery_list = GroceryList()
    grocery_list.add_item("milk", "Dairy")
    grocery_list.remove_item("milk")
    assert grocery_list.total_count() == 0


def test_remove_missing_item_raises_error():
    """Removing an item that is not there should raise a ValueError."""
    grocery_list = GroceryList()
    with pytest.raises(ValueError):
        grocery_list.remove_item("milk")


def test_check_off_item_updates_checked_count():
    """Checking off an item should raise the checked count to 1."""
    grocery_list = GroceryList()
    grocery_list.add_item("milk", "Dairy")
    grocery_list.check_off_item("milk")
    assert grocery_list.checked_count() == 1


def test_check_off_twice_raises_error():
    """Checking off the same item twice should raise a ValueError."""
    grocery_list = GroceryList()
    grocery_list.add_item("milk", "Dairy")
    grocery_list.check_off_item("milk")
    with pytest.raises(ValueError):
        grocery_list.check_off_item("milk")