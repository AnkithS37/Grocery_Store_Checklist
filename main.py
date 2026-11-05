"""
Program: Grocery_Store_Checklist
Author: Ankith Srivathsan
Purpose: Command-line menu for managing a grocery list that is saved between runs.
Starter code: Menu text and loop based on my Project 1 version of this program
Date: November 4th, 2026
"""

from storage import load_list, save_list

from grocery_item import CATEGORIES


def show_menu():
    """Print the menu options."""
    print("\n=== Grocery Store Checklist ===")
    print("1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Check Off Item")
    print("5. Quit")

def add_item_menu(grocery_list):
    """Ask the user for an item name and category, then add it to the list."""
    name = input("Item name: ").strip().lower()
    print("Categories:")
    for category in CATEGORIES:
        print(category)
    category = input("Category: ").strip().title()
    try:
        grocery_list.add_item(name, category)
        print(f"Added {name} ({category})")
    except ValueError as error:
        print(error)


def remove_item_menu(grocery_list):
    """Ask the user which item to remove and take it off the list."""
    name = input("Item to remove: ").strip().lower()
    try:
        grocery_list.remove_item(name)
        print(f"Removed {name}.")
    except ValueError as error:
        print(error)


def view_list_menu(grocery_list):
    """Print every item with a checkbox and show the progress count."""
    if grocery_list.total_count() == 0:
        print("Your list is empty.")
        return
    for item in grocery_list.items.values():
        box = "[X]" if item.checked else "[ ]"
        print(f"{box} {item.name} ({item.category})")
    print(f"Progress: {grocery_list.checked_count()} of {grocery_list.total_count()} checked off.")


def check_off_item_menu(grocery_list):
    """Ask the user which item to check off and mark it done."""
    name = input("Item to check off: ").strip().lower()
    try:
        grocery_list.check_off_item(name)
        print(f"Checked off {name}.")
    except ValueError as error:
        print(error)


def main():
    """Load the saved list, run the menu loop, and save when the user quits."""
    grocery_list = load_list()
    running = True
    while running:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_item_menu(grocery_list)
        elif choice == "2":
            view_list_menu(grocery_list)
        elif choice == "3":
            remove_item_menu(grocery_list)
        elif choice == "4":
            check_off_item_menu(grocery_list)
        elif choice == "5":
            running = False
        else:
            print("Feature coming soon!")
    save_list(grocery_list)
    print("Happy Shopping!")


if __name__ == "__main__":
    main()

    
