"""
Program: Grocery_Store_Checklist
Author: Ankith Srivathsan
Purpose: Defines the GroceryList class, which manages all the items on the list.
Starter code: None, written using concepts from chapters 1-11
Date: November 4th, 2026
"""

from grocery_item import GroceryItem, CATEGORIES

class GroceryList:
    """A collection of grocery items, stored by item name"""

    def __init__(self):
        """Create an empty grocery list."""
        self.items = {}

    def add_item(self, name, category):
        """Add an item to the list. Raises ValueError if the category is invalid."""
        if category not in CATEGORIES:
            raise ValueError("Invalid category")
        self.items[name] = GroceryItem(name, category)

    def remove_item(self, name):
        """Remove an item from the list. Raises ValueError if it is not there."""
        if name not in self.items:
            raise ValueError("Item not on list")
        del self.items[name]

    def check_off_item(self, name):
        """Check off an item. Raises ValueError if it is missing or already checked."""
        if name not in self.items:
            raise ValueError(f"{name} is not on your list.")
        if self.items[name].checked:
            raise ValueError(f"{name} is already checked off.")
        self.items[name].check_off()

    def checked_count(self):
        """Return how many items are checked off."""
        return sum(1 for item in self.items.values() if item.checked)

    def total_count(self):
        """Return how many items are on the list."""
        return len(self.items)

    def to_dict_list(self):
        """Return every item as a dictionary so the list can be saved to JSON."""
        return [item.to_dict() for item in self.items.values()]