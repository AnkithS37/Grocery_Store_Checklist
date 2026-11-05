**Video Presentation:** (https://youtu.be/kx4LgC9EQ1w)

# Grocery Store Checklist

**Author:** Ankith Srivathsan

**Date:** November 4th, 2026

**Purpose:** A command-line program for building and tracking a grocery shopping list. The list is saved to a file, so it is still there the next time the program runs.

## Features

- Add items with a category
- View the list with checked-off items marked and a progress count
- Remove items from the list
- Check items off while shopping
- Automatically saves and loads the list (JSON)

## Project Structure

| File | Job |
|------|-----|
| `main.py` | The menu and the program loop |
| `grocery_item.py` | `GroceryItem` class: one item's name, category, and checked status |
| `grocery_list.py` | `GroceryList` class: add, remove, check off, and count items |
| `storage.py` | Saves the list to JSON and loads it back, handling missing or damaged files |
| `tests/` | pytest tests for the item, list, and storage code |

## Design Choices

- **Separate modules:** each file has one job, so a bug in saving cannot break the list logic.
- **No inheritance:** a grocery item has no real subtypes, so a `GroceryList` simply holds `GroceryItem` objects (composition).
- **Errors raised, not printed:** `GroceryList` raises a `ValueError` when something is wrong, and the menu code decides how to show it.

## How to Run

    python main.py

## How to Run the Tests

    pip install -r requirements.txt
    pytest