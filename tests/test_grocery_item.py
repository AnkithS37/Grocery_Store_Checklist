"""
Program: Grocery_Store_Checklist
Author: Ankith Srivathsan
Purpose: Tests for the GroceryItem class.
Starter code: None, written using concepts from chapters 1-11
Date: November 4th, 2026
"""

from grocery_item import GroceryItem


def test_new_item_starts_unchecked():
    """A brand new item should not be checked off."""
    item = GroceryItem("milk", "Dairy")
    assert item.checked is False


def test_check_off_marks_item_checked():
    """Calling check_off should set checked to True."""
    item = GroceryItem("milk", "Dairy")
    item.check_off()
    assert item.checked is True


def test_to_dict_returns_all_fields():
    """to_dict should return the name, category, and checked status."""
    item = GroceryItem("eggs", "Dairy")
    assert item.to_dict() == {"name": "eggs", "category": "Dairy", "checked": False}