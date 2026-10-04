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
    choice = input ("Choose an option (1-5): ").strip()

    if choice == "5":
        running = False
    else:
        print("Feature coming soon!")

print("Happy Shopping!")

    
