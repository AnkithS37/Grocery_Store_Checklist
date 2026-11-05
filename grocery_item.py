"""
Program: Grocery_Store_Checklist
Author: Ankith Srivathsan
Purpose: Defines the GroceryItem class, which stores one item on the grocery list.
Starter code: None, written using concepts from chapters 1-11
Date: November 4th, 2026
"""

CATEGORIES = ("Produce", "Dairy", "Meat", "Pantry", "Frozen", "Other")


class GroceryItem:
    """One item on the grocery list."""

    def __init__(self, name, category, checked=False):
        """Create an item with a name, a category, and a checked-off status."""
        self.name = name
        self.category = category
        self.checked = checked


    def check_off(self):
        """Mark this item as checked off."""
        self.checked = True

    def to_dict(self):
        """Return a dictionary representation of this item."""
        return {
            "name": self.name,
            "category": self.category,
            "checked": self.checked
        }