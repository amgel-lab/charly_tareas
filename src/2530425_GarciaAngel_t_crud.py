"""
    Nombre: Angel Javier García Nieto
    Matrícula: 2530425
    Grupo: IM 1-1

- CRUD stands for Create, Read, Update, Delete.
- A clean way to build CRUD programs in Python is:
   1) Choose a main data structure to store items in memory.
   2) Implement one function per CRUD operation (plus listing).
   3) Use a menu loop (while) to read user options and delegate work to functions.
- Input validation is critical so the program remains stable and data stays consistent.
- Policy decisions (like what to do with duplicate IDs) must be documented clearly.
"""

# ============================================================
# DATA STRUCTURE CHOICE
# ============================================================
# Option chosen: A dictionary mapping item_id -> item_data_dict
#
# Why this option?
# - Fast lookup by id (average O(1) with `item_id in items`, items.get(item_id))
# - Unique IDs are naturally enforced by dictionary keys
# - CRUD operations are simpler than scanning a list each time
#
# Structure:
# items = {
#   "A1": {"id": "A1", "name": "Pen", "price": 5.0, "quantity": 10},
#   "B2": {"id": "B2", "name": "Notebook", "price": 25.0, "quantity": 7},
# }
# ============================================================

# ============================================================
# CRUD FUNCTIONS
# ============================================================
# Notes:
# - Functions receive the data structure as a parameter (no global dependency required).
# - Returns are boolean or dict/None to indicate success or failure.
# - Policy for CREATE duplicates: DO NOT allow duplicate IDs.
# ============================================================
def create_item(items: dict, item_id: str, name: str, price: float, quantity: int) -> bool:
    """Create a new item. Returns True if created, False if id already exists."""
    if item_id in items:
        return False

    items[item_id] = {"id": item_id, "name": name, "price": price, "quantity": quantity}
    return True


def read_item(items: dict, item_id: str) -> dict | None:
    """Return the item dict if found; otherwise None."""
    return items.get(item_id)


def update_item(items: dict, item_id: str, new_name: str, new_price: float, new_quantity: int) -> bool:
    """Update an existing item. Returns True if updated, False if not found."""
    if item_id not in items:
        return False

    items[item_id]["name"] = new_name
    items[item_id]["price"] = new_price
    items[item_id]["quantity"] = new_quantity
    return True


def delete_item(items: dict, item_id: str) -> bool:
    """Delete an item by id. Returns True if deleted, False if not found."""
    if item_id not in items:
        return False

    items.pop(item_id)
    return True


def list_items(items: dict) -> None:
    """Print all items in a readable format."""
    if not items:
        print("Items list: (empty)")
        return

    print("Items list:")
    for item_id, data in items.items():
        print(f"- id={item_id} | name={data['name']} | price={data['price']} | quantity={data['quantity']}")


# ============================================================
# INPUT HELPERS (small validation utilities)
# ============================================================
def read_non_empty_text(prompt: str) -> str | None:
    """Read a non-empty string after strip(). Returns the string or None if invalid."""
    value = input(prompt).strip()
    return value if value else None


def read_float(prompt: str) -> float | None:
    """Read a float. Returns float value or None if conversion fails."""
    text = input(prompt).strip()
    try:
        return float(text)
    except ValueError:
        return None


def read_int(prompt: str) -> int | None:
    """Read an int. Returns int value or None if conversion fails."""
    text = input(prompt).strip()
    try:
        return int(text)
    except ValueError:
        return None


# ============================================================
# 6. PROBLEM 6.1: CRUD Manager with functions (menu-driven)
# ============================================================
# Description:
# - Manage in-memory items with fields:
#   * id (string; unique)
#   * name (string)
#   * price (float; >= 0.0)
#   * quantity (int; >= 0)
# - Provide menu options:
#   1) Create item
#   2) Read item by id
#   3) Update item by id
#   4) Delete item by id
#   5) List all items
#   0) Exit
# - All CRUD logic must be in functions; menu delegates to those functions.
#
# Inputs:
# - option (int)
# - item_id (string)
# - name (string)
# - price (float)
# - quantity (int)
#
# Outputs:
# - "Item created" / "Item updated" / "Item deleted"
# - "Item not found"
# - "Error: invalid input"
# - "Items list:" + printed items
#
# Validations:
# - option must be one of 0..5
# - item_id non-empty after strip()
# - price must be a valid number and price >= 0.0
# - quantity must be a valid integer and quantity >= 0
# - CREATE policy: if id exists -> do not create (prints "Error: duplicate id")
# - READ/UPDATE/DELETE: if id not found -> print "Item not found"
#
# Test cases (normal / edge / error):
# 1) Normal:
#    - Create: id="A1", name="Pen", price=5, quantity=10 -> Item created
#    - Read: id="A1" -> prints the stored item
#    - Update: id="A1", name="Pen Blue", price=6, quantity=8 -> Item updated
#    - Delete: id="A1" -> Item deleted
# 2) Edge:
#    - Create: price=0.0 and quantity=0 (allowed) -> Item created
#    - Update: set quantity=0 (allowed) -> Item updated
# 3) Error:
#    - Invalid option (e.g., 9) -> Error: invalid input
#    - Create with existing id -> Error: duplicate id
#    - Read/Update/Delete non-existing id -> Item not found
#    - Negative price or quantity -> Error: invalid input
items = {
    # Initial sample data (optional)
    "A1": {"id": "A1", "name": "Pen", "price": 5.0, "quantity": 10},
    "B2": {"id": "B2", "name": "Notebook", "price": 25.0, "quantity": 7},
    "C3": {"id": "C3", "name": "Eraser", "price": 3.5, "quantity": 20},
}

while True:
    print("Menu:")
    print("1) Create item")
    print("2) Read item by id")
    print("3) Update item by id")
    print("4) Delete item by id")
    print("5) List all items")
    print("0) Exit")

    option_text = input("Choose an option (0-5): ").strip()

    try:
        option = int(option_text)
    except ValueError:
        print("Error: invalid input")
        print()
        continue

    if option not in (0, 1, 2, 3, 4, 5):
        print("Error: invalid input")
        print()
        continue

    if option == 0:
        print("Bye!")
        break

    # 5) List all items
    if option == 5:
        list_items(items)
        print()
        continue

    # For options 1-4, we always need an item_id
    item_id = read_non_empty_text("Enter item id: ")
    if item_id is None:
        print("Error: invalid input")
        print()
        continue

    # 2) Read item by id
    if option == 2:
        found = read_item(items, item_id)
        if found is None:
            print("Item not found")
        else:
            print(f"Item: id={found['id']} | name={found['name']} | price={found['price']} | quantity={found['quantity']}")
        print()
        continue

    # 4) Delete item by id
    if option == 4:
        deleted = delete_item(items, item_id)
        if deleted:
            print("Item deleted")
        else:
            print("Item not found")
        print()
        continue

    # For CREATE (1) and UPDATE (3), we need name, price, quantity
    name = read_non_empty_text("Enter name: ")
    price = read_float("Enter price (>= 0): ")
    quantity = read_int("Enter quantity (>= 0): ")

    if name is None or price is None or quantity is None:
        print("Error: invalid input")
        print()
        continue

    if price < 0.0 or quantity < 0:
        print("Error: invalid input")
        print()
        continue

    # 1) Create item
    if option == 1:
        created = create_item(items, item_id, name, price, quantity)
        if created:
            print("Item created")
        else:
            print("Error: duplicate id")
        print()
        continue

    # 3) Update item by id
    if option == 3:
        updated = update_item(items, item_id, name, price, quantity)
        if updated:
            print("Item updated")
        else:
            print("Item not found")
        print()
        continue

# ============================================================
# REFERENCES (5)
# ============================================================
# 1) Python tutorial: defining functions (parameters, return values):
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#
# 2) Python tutorial: data structures (lists, dictionaries):
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 3) Built-in types: mapping type dict (methods like get, pop, membership):
#    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
#
# 4) Errors and exceptions (try/except, ValueError):
#    https://docs.python.org/3/tutorial/errors.html
#
# 5) PEP 8 (naming conventions, clean and readable code):
#    https://peps.python.org/pep-0008/
# ============================================================
# Repositorio GitHub: https://github.com/amgel-lab/charly_tareas
# ============================================================