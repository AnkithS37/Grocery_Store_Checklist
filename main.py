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


def main():
    """Load the saved list, run the menu loop, and save when the user quits."""
    grocery_list = load_list()
    running = True
    while running:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_item_menu(grocery_list)
        elif choice == "5":
            running = False
        else:
            print("Feature coming soon!")
    save_list(grocery_list)
    print("Happy Shopping!")


if __name__ == "__main__":
    main()

    
