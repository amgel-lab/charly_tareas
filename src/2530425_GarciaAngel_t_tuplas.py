"""
    Nombre: Angel Javier García Nieto
    Matrícula: 2530425
    Grupo: IM 1-1

- Lists (list) are ordered, mutable collections: you can append(), remove(), and modify items.
- Tuples (tuple) are ordered, immutable collections: great for fixed data like coordinates (x, y).
- Dictionaries (dict) map keys to values: fast lookup with `in`, access with dict[key], safe access with get().
- Common patterns:
* Clean input text with strip(), normalize with lower()/upper()
* Convert text to collections: split() for lists, (a, b) for tuples, {k: v} for dicts
* Use boolean checks: item in list, key in dict, len(...) > 0

"""

# ============================================================
# 7.1 PROBLEM 1: Shopping list basics (list operations)
# ============================================================
# Description:
# - Work with a list of product names (strings).
# - The program must:
#   1) Create an initial list from a comma-separated string.
#   2) Append a new product to the end.
#   3) Print the total number of items.
#   4) Check if a searched product exists in the list (boolean is_in_list).
#
# Inputs:
# - initial_items_text (string; e.g., "apple,banana,orange")
# - new_item (string; item to append)
# - search_item (string; item to search)
#
# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <len_list>
# - "Found item:" true|false
#
# Validations:
# - initial_items_text must not be empty after strip()
# - Split by commas and strip extra spaces from each item
# - new_item and search_item must not be empty after strip()
# - Decision: if initial parsing produces an empty list, treat as invalid input (documented here)
#
# Key operations:
# - split(), strip(), append(), len(), in
#
# Test cases (normal / edge / error):
# 1) Normal:
#    - initial_items_text="apple, banana, orange", new_item="milk", search_item="banana"
#    - Found item: true, Total items: 4
# 2) Edge:
#    - initial_items_text="  apple  ", new_item="apple", search_item="apple"
#    - List becomes ["apple", "apple"], Found item: true
# 3) Error:
#    - initial_items_text="   ", new_item="milk", search_item="milk"
#    - invalid input
initial_items_text = input("Problem 7.1 - Enter initial items (comma-separated): ").strip()
new_item = input("Problem 7.1 - Enter a new item to add: ").strip()
search_item = input("Problem 7.1 - Enter an item to search: ").strip()

if not initial_items_text or not new_item or not search_item:
    print("Error: invalid input")
else:
    raw_parts = initial_items_text.split(",")
    items_list = [part.strip() for part in raw_parts if part.strip()]

    # Decision: empty initial list after cleaning is invalid
    if len(items_list) == 0:
        print("Error: invalid input")
    else:
        items_list.append(new_item)
        is_in_list = (search_item in items_list)

        print("Items list:", items_list)
        print("Total items:", len(items_list))
        print("Found item:", str(is_in_list).lower())

print()  # separator


# ============================================================
# 7.2 PROBLEM 2: Points and distances with tuples
# ============================================================
# Description:
# - Use tuples to represent 2D points: (x1, y1) and (x2, y2).
# - The program must:
#   1) Create point_a and point_b tuples from numeric input.
#   2) Compute Euclidean distance.
#   3) Create midpoint tuple.
#
# Inputs:
# - x1, y1, x2, y2 (float)
#
# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)
#
# Validations:
# - All 4 inputs must be convertible to float
#
# Key operations:
# - point_a = (x1, y1), point_b = (x2, y2)
# - distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# - midpoint = ((x1 + x2)/2, (y1 + y2)/2)
#
# Test cases (normal / edge / error):
# 1) Normal: (0,0) and (3,4) -> distance 5.0, midpoint (1.5, 2.0)
# 2) Edge: same points (2,2) and (2,2) -> distance 0.0
# 3) Error: x1="a" -> invalid input
x1_text = input("Problem 7.2 - Enter x1: ").strip()
y1_text = input("Problem 7.2 - Enter y1: ").strip()
x2_text = input("Problem 7.2 - Enter x2: ").strip()
y2_text = input("Problem 7.2 - Enter y2: ").strip()

try:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)
except ValueError:
    print("Error: invalid input")

print()  # separator


# ============================================================
# 7.3 PROBLEM 3: Product catalog with dictionary
# ============================================================
# Description:
# - Manage a small product catalog using a dictionary:
#   * key: product name (string)
#   * value: unit price (float)
# - The program must:
#   1) Create an initial dictionary with at least 3 products.
#   2) Read product_name and quantity.
#   3) If product exists, compute total price.
#   4) If not, print an error message.
#
# Inputs:
# - product_name (string)
# - quantity (int)
#
# Outputs:
# - If product exists:
#   * "Unit price:" <unit_price>
#   * "Quantity:" <quantity>
#   * "Total:" <total_price>
# - If product does not exist:
#   * "Error: product not found"
#
# Validations:
# - product_name must not be empty after strip()
# - quantity must be convertible to int and quantity > 0
# - product_name must be a key in the dictionary (case policy documented below)
#
# Decision:
# - Catalog keys are stored in lowercase, and user input is normalized to lowercase.
#
# Key operations:
# - dict literal, `in` for key check, access with product_prices[product_name]
#
# Test cases (normal / edge / error):
# 1) Normal: product_name="apple", quantity="3" -> total = 3 * 10.0
# 2) Edge: product_name="APPLE", quantity="1" -> works due to lowercasing
# 3) Error: quantity="0" or product_name not in dict -> invalid / not found
product_prices = {
    "apple": 10.0,
    "banana": 6.5,
    "orange": 8.0
}

product_name_input = input("Problem 7.3 - Enter product name: ").strip()
quantity_text = input("Problem 7.3 - Enter quantity (int): ").strip()

if not product_name_input:
    print("Error: invalid input")
else:
    try:
        quantity = int(quantity_text)
    except ValueError:
        quantity = 0  # force invalid

    if quantity <= 0:
        print("Error: invalid input")
    else:
        product_key = product_name_input.lower()

        if product_key in product_prices:
            unit_price = product_prices[product_key]
            total_price = unit_price * quantity
            print("Unit price:", unit_price)
            print("Quantity:", quantity)
            print("Total:", total_price)
        else:
            print("Error: product not found")

print()  # separator


# ============================================================
# 7.4 PROBLEM 4: Student grades with dict and list
# ============================================================
# Description:
# - Manage student grades using a dictionary:
#   * key: student name (string)
#   * value: list of grades (list of float)
# - The program must:
#   1) Create a dictionary with at least 3 students.
#   2) Read student_name.
#   3) Compute the average of the student's grades.
#   4) Compute boolean is_passed: average >= 70.0
#
# Inputs:
# - student_name (string)
#
# Outputs:
# - If student exists:
#   * "Grades:" <grades_list>
#   * "Average:" <average>
#   * "Passed:" true|false
# - If student does not exist:
#   * "Error: student not found"
#
# Validations:
# - student_name must not be empty after strip()
# - student_name must exist as a key
# - grades list must not be empty before computing average
#
# Decision:
# - Student keys are stored as Title Case (e.g., "Alice"), and input is normalized with title().
#
# Key operations:
# - dict of lists, sum(), len(), `in` for key check
#
# Test cases (normal / edge / error):
# 1) Normal: student_name="Alice" -> average computed, passed based on >=70
# 2) Edge: student_name="bob" -> works due to title() normalization
# 3) Error: student_name="Zoe" -> not found
student_grades = {
    "Alice": [90.0, 85.0, 78.0],
    "Bob": [60.0, 72.0, 70.0],
    "Carla": [100.0, 95.0]
}

student_name_input = input("Problem 7.4 - Enter student name: ").strip()

if not student_name_input:
    print("Error: invalid input")
else:
    student_key = student_name_input.title()

    if student_key not in student_grades:
        print("Error: student not found")
    else:
        grades_list = student_grades[student_key]

        if len(grades_list) == 0:
            print("Error: invalid input")
        else:
            average = sum(grades_list) / len(grades_list)
            is_passed = (average >= 70.0)

            print("Grades:", grades_list)
            print("Average:", average)
            print("Passed:", str(is_passed).lower())

print()  # separator


# ============================================================
# 7.5 PROBLEM 5: Word frequency counter (list + dict)
# ============================================================
# Description:
# - Count the frequency of each word in a sentence using:
#   * a list of words
#   * a dictionary mapping word -> count
# - The program must:
#   1) Read a sentence.
#   2) Normalize to lowercase and split into a list of words.
#   3) Build a frequency dictionary.
#   4) Print the dictionary and the most common word (ties allowed).
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Words list:" <words_list>
# - "Frequencies:" <freq_dict>
# - "Most common word:" <word>
#
# Validations:
# - sentence must not be empty after strip()
# - words list must not be empty after processing
#
# Decision (simple punctuation handling):
# - Remove a few common punctuation marks by replacing them with "" before split().
#
# Key operations:
# - lower(), replace(), split()
# - dict counting with if-in / else
#
# Test cases (normal / edge / error):
# 1) Normal: "Apple apple orange." -> most common "apple" (count 2)
# 2) Edge: "Hello!!!" -> words ["hello"], freq {"hello": 1}
# 3) Error: "   " -> invalid input
sentence = input("Problem 7.5 - Enter a sentence: ").strip()

if not sentence:
    print("Error: invalid input")
else:
    cleaned = sentence.lower()
    for mark in [",", ".", "!", "?", ":", ";"]:
        cleaned = cleaned.replace(mark, "")

    words_list = cleaned.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        # Find most common word (any tie is acceptable)
        most_common_word = None
        most_common_count = -1
        for word, count in freq_dict.items():
            if count > most_common_count:
                most_common_word = word
                most_common_count = count

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)

print()  # separator


# ============================================================
# 7.6 PROBLEM 6: Simple contact book (dictionary CRUD)
# ============================================================
# Description:
# - Implement a mini contact book using a dictionary:
#   * key: contact name (string)
#   * value: phone number (string)
# - The program must:
#   1) Create an initial dictionary with some contacts.
#   2) Read action_text ("ADD", "SEARCH", or "DELETE").
#   3) Execute the action:
#      - ADD: read name and phone; add or update contact.
#      - SEARCH: read name; print phone if exists.
#      - DELETE: read name; remove contact if exists.
#   4) Print a message indicating the result.
#
# Inputs:
# - action_text (string; "ADD", "SEARCH", "DELETE")
# - name (string; depends on action)
# - phone (string; only for "ADD")
#
# Outputs:
# - ADD: "Contact saved:" name, phone
# - SEARCH: "Phone:" <phone> or "Error: contact not found"
# - DELETE: "Contact deleted:" name or "Error: contact not found"
#
# Validations:
# - Normalize action_text to uppercase
# - action_text must be one of the valid options
# - name must not be empty after strip()
# - For ADD: phone must not be empty after strip()
#
# Key operations:
# - dict, get(), in, pop(), if/elif
#
# Test cases (normal / edge / error):
# 1) Normal: action="SEARCH", name="Alice" -> prints her phone if exists
# 2) Edge: action="ADD", name="  Alice  ", phone="999" -> updates existing contact
# 3) Error: action="REMOVE" -> invalid action
contacts = {
    "Alice": "1234567890",
    "Bob": "5551234567",
    "Carla": "8880001111"
}

action_text = input("Problem 7.6 - Action (ADD/SEARCH/DELETE): ").strip().upper()

if action_text not in ("ADD", "SEARCH", "DELETE"):
    print("Error: invalid input")
else:
    name = input("Problem 7.6 - Enter contact name: ").strip()

    if not name:
        print("Error: invalid input")
    else:
        name_key = name.title()  # decision: store names normalized to Title Case

        if action_text == "ADD":
            phone = input("Problem 7.6 - Enter phone number: ").strip()
            if not phone:
                print("Error: invalid input")
            else:
                contacts[name_key] = phone
                print("Contact saved:", name_key, phone)

        elif action_text == "SEARCH":
            if name_key in contacts:
                print("Phone:", contacts[name_key])
            else:
                print("Error: contact not found")

        else:  # DELETE
            if name_key in contacts:
                contacts.pop(name_key)
                print("Contact deleted:", name_key)
            else:
                print("Error: contact not found")


# ============================================================
# REFERENCES (5)
# ============================================================
# 1) Python Lists (tutorial section):
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 2) Built-in Types (list, tuple, dict behavior and methods):
#    https://docs.python.org/3/library/stdtypes.html
#
# 3) Dictionary operations and methods (mapping types):
#    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
#
# 4) Built-in Functions (len, sum, etc.):
#    https://docs.python.org/3/library/functions.html
#
# 5) Text processing basics (strings, split, replace, etc.):
#    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# ============================================================
# Repositorio GitHub: https://github.com/amgel-lab/charly_tareas
# ============================================================
