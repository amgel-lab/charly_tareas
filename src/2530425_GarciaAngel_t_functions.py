"""
    Nombre: Angel Javier García Nieto
    Matrícula: 2530425
    Grupo: IM 1-1

- Functions help you organize code into reusable, testable blocks.
- A function can take parameters (inputs) and return a value with `return`.
- Validation is often done in the "main" code before calling a function, so the function
can assume inputs are valid (simpler and safer).
- "Pure functions" do not modify their inputs and have no side effects. They return new values
(useful for lists, such as returning a discounted copy).
- Default parameters (e.g., title="") make a function more flexible without requiring extra
"""

# ============================================================
# 7.1 PROBLEM 1: Rectangle area and perimeter (basic functions)
# ============================================================
# Description:
# - Define two functions:
#   * calculate_area(width, height): returns rectangle area
#   * calculate_perimeter(width, height): returns rectangle perimeter
# - Main code reads (or defines) width/height, validates, calls functions, prints results.
#
# Inputs:
# - width (float)
# - height (float)
#
# Outputs:
# - "Area:" <area_value>
# - "Perimeter:" <perimeter_value>
#
# Validations:
# - width > 0
# - height > 0
# - If invalid, print "Error: invalid input" and DO NOT call the functions
#
# Key operations:
# - area = width * height
# - perimeter = 2 * (width + height)
#
# Test cases (normal / edge / error):
# 1) Normal:  width="5", height="2" -> Area=10, Perimeter=14
# 2) Edge:    width="0.0001", height="0.0001" -> valid small positives
# 3) Error:   width="-3", height="2" -> Error: invalid input
def calculate_area(width: float, height: float) -> float:
    return width * height


def calculate_perimeter(width: float, height: float) -> float:
    return 2 * (width + height)


width_text = input("Problem 7.1 - Enter width: ").strip()
height_text = input("Problem 7.1 - Enter height: ").strip()

try:
    width = float(width_text)
    height = float(height_text)

    if width <= 0 or height <= 0:
        print("Error: invalid input")
    else:
        area_value = calculate_area(width, height)
        perimeter_value = calculate_perimeter(width, height)

        print("Area:", area_value)
        print("Perimeter:", perimeter_value)
except ValueError:
    print("Error: invalid input")

print()  # separator


# ============================================================
# 7.2 PROBLEM 2: Grade classifier (function with return string)
# ============================================================
# Description:
# - Define classify_grade(score) returning a letter category:
#   * A: score >= 90
#   * B: 80 <= score < 90
#   * C: 70 <= score < 80
#   * D: 60 <= score < 70
#   * F: score < 60
# - Main code validates score as 0..100, then calls the function and prints the result.
#
# Inputs:
# - score (float or int)
#
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
#
# Validations:
# - 0 <= score <= 100
# - If invalid, print "Error: invalid input" and DO NOT classify
#
# Key operations:
# - if/elif ranges
#
# Test cases (normal / edge / error):
# 1) Normal: score="85" -> Category=B
# 2) Edge:   score="90" -> Category=A (boundary)
# 3) Error:  score="120" -> Error: invalid input
def classify_grade(score: float) -> str:
    # Multiple returns keeps the logic simple and readable.
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


score_text = input("Problem 7.2 - Enter score (0..100): ").strip()

try:
    score = float(score_text)
    if score < 0 or score > 100:
        print("Error: invalid input")
    else:
        grade_letter = classify_grade(score)
        print("Score:", score)
        print("Category:", grade_letter)
except ValueError:
    print("Error: invalid input")

print()  # separator


# ============================================================
# 7.3 PROBLEM 3: List statistics function (min, max, average)
# ============================================================
# Description:
# - Define summarize_numbers(numbers_list) returning a dictionary with:
#   * "min": minimum
#   * "max": maximum
#   * "average": mean average (float)
# - Main code reads comma-separated text, builds list of numbers, calls function, prints values.
#
# Inputs:
# - numbers_text (string; e.g., "10,20,30")
# - Internally: numbers_list (list of float)
#
# Outputs:
# - "Min:" <min_value>
# - "Max:" <max_value>
# - "Average:" <average_value>
#
# Validations:
# - numbers_text not empty after strip()
# - List not empty after conversion
# - Every element must be convertible to float; if any fails -> "Error: invalid input"
#
# Key operations:
# - split(), loop conversion, sum(), len(), min(), max()
#
# Test cases (normal / edge / error):
# 1) Normal: numbers_text="10,20,30" -> min=10, max=30, avg=20
# 2) Edge:   numbers_text="5" -> min=max=avg=5
# 3) Error:  numbers_text="10,abc,30" -> Error: invalid input
def summarize_numbers(numbers_list: list[float]) -> dict:
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list),
    }


numbers_text = input("Problem 7.3 - Enter numbers (comma-separated): ").strip()

if not numbers_text:
    print("Error: invalid input")
else:
    parts = [p.strip() for p in numbers_text.split(",")]
    numbers_list = []

    conversion_failed = False
    for p in parts:
        if p == "":
            conversion_failed = True
            break
        try:
            numbers_list.append(float(p))
        except ValueError:
            conversion_failed = True
            break

    if conversion_failed or len(numbers_list) == 0:
        print("Error: invalid input")
    else:
        stats = summarize_numbers(numbers_list)
        print("Min:", stats["min"])
        print("Max:", stats["max"])
        print("Average:", stats["average"])

print()  # separator


# ============================================================
# 7.4 PROBLEM 4: Apply discount list (pure function)
# ============================================================
# Description:
# - Define apply_discount(prices_list, discount_rate) that returns a NEW list with discounted prices.
# - Must NOT modify the original list (pure function).
# - Main code reads prices list and discount_rate, validates, calls function, prints both lists.
#
# Inputs:
# - prices_text (string; e.g., "100,200,300")
# - discount_rate (float; between 0 and 1)
#
# Outputs:
# - "Original prices:" <original_list>
# - "Discounted prices:" <discounted_list>
#
# Validations:
# - prices_text not empty and list not empty after parsing
# - All prices > 0
# - 0 <= discount_rate <= 1
# - If invalid -> "Error: invalid input"
#
# Key operations:
# - Build list of float from text
# - Create a new list in the function using a loop
#
# Test cases (normal / edge / error):
# 1) Normal: prices_text="100,200", discount_rate="0.10" -> [90, 180]
# 2) Edge:   prices_text="50", discount_rate="1" -> [0.0] (100% discount)
# 3) Error:  prices_text="100,-5", discount_rate="0.2" -> Error: invalid input
def apply_discount(prices_list: list[float], discount_rate: float) -> list[float]:
    # Pure function: create and return a new list (do not modify the input list).
    discounted = []
    for price in prices_list:
        discounted.append(price * (1 - discount_rate))
    return discounted


prices_text = input("Problem 7.4 - Enter prices (comma-separated): ").strip()
discount_text = input("Problem 7.4 - Enter discount rate (0..1): ").strip()

if not prices_text:
    print("Error: invalid input")
else:
    try:
        discount_rate = float(discount_text)
    except ValueError:
        discount_rate = -1  # force invalid

    if discount_rate < 0 or discount_rate > 1:
        print("Error: invalid input")
    else:
        price_parts = [p.strip() for p in prices_text.split(",")]
        prices_list = []

        parse_failed = False
        for p in price_parts:
            if p == "":
                parse_failed = True
                break
            try:
                value = float(p)
                if value <= 0:
                    parse_failed = True
                    break
                prices_list.append(value)
            except ValueError:
                parse_failed = True
                break

        if parse_failed or len(prices_list) == 0:
            print("Error: invalid input")
        else:
            discounted_list = apply_discount(prices_list, discount_rate)
            print("Original prices:", prices_list)
            print("Discounted prices:", discounted_list)

print()  # separator


# ============================================================
# 7.5 PROBLEM 5: Greeting function with default parameters
# ============================================================
# Description:
# - Define greet(name, title="") that optionally prepends title to the name.
# - Returns: "Hello, <full_name>!"
# - Main code calls the function using positional and named arguments.
#
# Inputs:
# - name (string)
# - title (string; optional)
#
# Outputs:
# - "Greeting:" <greeting_message>
#
# Validations:
# - name must not be empty after strip()
# - title can be empty; if not empty, also normalize with strip()
#
# Key operations:
# - default parameter: def greet(name, title="")
# - named arguments: greet(name="Alice", title="Dr.")
#
# Test cases (normal / edge / error):
# 1) Normal: name="Alice", title="Dr." -> "Hello, Dr. Alice!"
# 2) Edge:   name="Bob", title="" -> "Hello, Bob!"
# 3) Error:  name="   " -> Error: invalid input
def greet(name: str, title: str = "") -> str:
    name_clean = name.strip()
    title_clean = title.strip()

    if title_clean:
        full_name = f"{title_clean} {name_clean}"
    else:
        full_name = name_clean

    return f"Hello, {full_name}!"


name_input = input("Problem 7.5 - Enter name: ").strip()
title_input = input("Problem 7.5 - Enter title (optional): ").strip()

if not name_input:
    print("Error: invalid input")
else:
    # Show both calling styles (positional + named)
    greeting_positional = greet(name_input, title_input)
    greeting_named = greet(name=name_input, title=title_input)

    # Print just one output message (same result in both calls)
    print("Greeting:", greeting_named)

print()  # separator


# ============================================================
# 7.6 PROBLEM 6: Factorial function (iterative)
# ============================================================
# Description:
# - Define factorial(n) returning n! (factorial).
# - Decision: implemented ITERATIVELY (for loop) for clarity and to avoid recursion limits.
# - Main code reads n, validates, calls factorial(), prints the result.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
#
# Validations:
# - n must be integer
# - n >= 0
# - Optional limit: n <= 20 to keep results reasonable (implemented here)
# - If invalid -> "Error: invalid input"
#
# Key operations:
# - result = 1
# - for i in range(1, n + 1): result *= i
#
# Test cases (normal / edge / error):
# 1) Normal: n="5" -> 120
# 2) Edge:   n="0" -> 1
# 3) Error:  n="-1" or n="25" -> Error: invalid input
MAX_N = 20  # optional safety limit

def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n_text = input("Problem 7.6 - Enter n (int, 0..20): ").strip()

try:
    n = int(n_text)
    if n < 0 or n > MAX_N:
        print("Error: invalid input")
    else:
        fact_value = factorial(n)
        print("n:", n)
        print("Factorial:", fact_value)
except ValueError:
    print("Error: invalid input")


# ============================================================
# REFERENCES (5)
# ============================================================
# 1) Defining functions (Python tutorial):
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
#
# 2) Built-in Functions (sum, min, max, len, etc.):
#    https://docs.python.org/3/library/functions.html
#
# 3) Data structures (lists and common patterns):
#    https://docs.python.org/3/tutorial/datastructures.html
#
# 4) Errors and exceptions (try/except, ValueError):
#    https://docs.python.org/3/tutorial/errors.html
#
# 5) math.factorial documentation (reference implementation for factorial behavior):
#    https://docs.python.org/3/library/math.html#math.factorial
# ============================================================
# Repositorio GitHub: https://github.com/amgel-lab/charly_tareas
# ============================================================