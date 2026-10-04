"""
Program: Grocery_Store_Checklist
Author: Ankith Srivathsan
Purpose: A command-line grocery list manager that lets the user add, view, remove, and check off items while shopping.
Starter code: None, written using concepts from chapters 1-7
Date: October 4th, 2026
"""


CATEGORIES = ("Produce", "Dairy", "Meat", "Pantry", "Frozen", "Other")

grocery_items = {}
checked_off = []
running = True

while running:
    print("\n=== Grocery Store Checklist ===")
    print("1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Check Off Item")
    print("5. quit")
    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        name = input("Item name: ").strip().lower()
        print("Categories:")
        for category in CATEGORIES:
            print(category)
        category = input("Category: ").strip().title()
        if category in CATEGORIES:
            grocery_items[name] = category
            print(f"Added {name} ({category})")
        else:
            print("Not a valid category.")

    elif choice == "2":
        if len(grocery_items) == 0:
            print("Your list is empty.")
        else:
            for name, category in grocery_items.items():
                print(f"{name} ({category})")

    elif choice == "5":
        running = False

    else:
        print("Feature coming soon!")


print("Happy Shopping!")

    
