"""
    Nombre: Angel Javier García Nieto
    Matrícula: 2530425
    Grupo: IM 1-1

- for loops are ideal when you know the number of iterations in advance (e.g., range(1, n+1)).
- while loops are ideal when the loop depends on a condition that changes at runtime
(e.g., user input, attempts counter, menu selection).
- Accumulators are variables used to "collect" results across iterations:
* total_sum += value
* count += 1
- Sentinel values are special inputs that stop a loop (e.g., -1 to end input).
- Always validate user input (convert safely), and handle edge cases like empty data.
"""

# ============================================================
# 7.1 PROBLEM 1: Sum of range with for
# ============================================================
# Description:
# - Compute the sum of all integers from 1 to n (inclusive).
# - Also compute the sum of only the even numbers in the same range using a for loop.
#
# Inputs:
# - n (int; upper limit)
#
# Outputs:
# - "Sum 1..n:" <total_sum>
# - "Even sum 1..n:" <even_sum>
#
# Validations:
# - n must be convertible to int
# - n >= 1, otherwise print "Error: invalid input"
#
# Key operations:
# - for i in range(1, n + 1): accumulate total_sum and even_sum
#
# Test cases (normal / edge / error):
# 1) Normal: n="10" -> Sum 1..n = 55, Even sum = 30
# 2) Edge:   n="1"  -> Sum 1..n = 1,  Even sum = 0
# 3) Error:  n="0"  -> Error: invalid input
n_text = input("Problem 7.1 - Enter n (int, >= 1): ").strip()

try:
    n = int(n_text)
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
except ValueError:
    print("Error: invalid input")

print()  # separator


# ============================================================
# 7.2 PROBLEM 2: Multiplication table with for
# ============================================================
# Description:
# - Print the multiplication table of a base number from 1 to m.
#
# Inputs:
# - base (int)
# - m (int; table limit)
#
# Outputs:
# - One line per multiplication, e.g.:
#   "5 x 1 = 5"
#   ...
#
# Validations:
# - base and m must be convertible to int
# - m >= 1, otherwise print "Error: invalid input"
#
# Key operations:
# - for i in range(1, m + 1): print f"{base} x {i} = {base*i}"
#
# Test cases (normal / edge / error):
# 1) Normal: base="5", m="4" -> prints 4 lines up to 5 x 4
# 2) Edge:   base="0", m="3" -> prints 0 results (valid), 0 x i = 0
# 3) Error:  base="7", m="0" -> Error: invalid input
base_text = input("Problem 7.2 - Enter base (int): ").strip()
m_text = input("Problem 7.2 - Enter m (int, >= 1): ").strip()

try:
    base = int(base_text)
    m = int(m_text)

    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            product = base * i
            print(f"{base} x {i} = {product}")
except ValueError:
    print("Error: invalid input")

print()  # separator


# ============================================================
# 7.3 PROBLEM 3: Average of numbers with while and sentinel
# ============================================================
# Description:
# - Repeatedly read numbers until the user enters a sentinel value (-1).
# - Compute:
#   * how many valid numbers were entered
#   * the average of those numbers
# - If the user enters only the sentinel, print "Error: no data"
#
# Inputs:
# - number (float; read repeatedly)
# - sentinel_value (fixed in code as -1)
#
# Outputs:
# - "Count:" <count>
# - "Average:" <average_value>
# - or "Error: no data" if no valid numbers were entered
#
# Validations:
# - Each input must be convertible to float, otherwise print "Error: invalid input"
#   and ask again (decision documented below).
# - Sentinel is not included in calculations.
#
# Decision:
# - If the user types a non-number (not convertible to float), show "Error: invalid input"
#   and continue asking for another value (do NOT crash).
#
# Key operations:
# - while True + break at sentinel
# - accumulators: total, count
#
# Test cases (normal / edge / error):
# 1) Normal: enter 10, 20, 30, -1 -> Count=3, Average=20.0
# 2) Edge:   enter -1 -> Error: no data
# 3) Error:  enter "abc", then 5, -1 -> prints invalid input once, then Count=1, Average=5.0
SENTINEL = -1.0

total = 0.0
count = 0

while True:
    number_text = input("Problem 7.3 - Enter a number (-1 to stop): ").strip()

    try:
        number = float(number_text)
    except ValueError:
        print("Error: invalid input")
        continue

    if number == SENTINEL:
        break

    total += number
    count += 1

if count == 0:
    print("Error: no data")
else:
    average_value = total / count
    print("Count:", count)
    print("Average:", average_value)

print()  # separator


# ============================================================
# 7.4 PROBLEM 4: Password attempts with while
# ============================================================
# Description:
# - Simple password attempt system:
#   * The correct password is stored in code (e.g., "admin123").
#   * The user has MAX_ATTEMPTS tries to enter it.
#   * If correct within limit -> "Login success"
#   * If all attempts fail -> "Account locked"
#
# Inputs:
# - user_password (string; read each attempt)
#
# Outputs:
# - "Login success" OR "Account locked"
#
# Validations:
# - MAX_ATTEMPTS > 0 (constant in code)
# - Count attempts correctly
#
# Key operations:
# - while attempts < MAX_ATTEMPTS
# - compare strings, break on success
#
# Test cases (normal / edge / error):
# 1) Normal: wrong, then correct within 3 attempts -> Login success
# 2) Edge:   correct on last attempt (attempt #3) -> Login success
# 3) Error:  all wrong attempts -> Account locked
CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3  # must be > 0

attempts = 0
login_success = False

while attempts < MAX_ATTEMPTS:
    user_password = input("Problem 7.4 - Enter password: ")
    attempts += 1

    if user_password == CORRECT_PASSWORD:
        login_success = True
        break

if login_success:
    print("Login success")
else:
    print("Account locked")

print()  # separator


# ============================================================
# 7.5 PROBLEM 5: Simple menu with while
# ============================================================
# Description:
# - Implement a repeating text menu until the user chooses 0 to exit:
#   1) Show greeting
#   2) Show current counter value
#   3) Increment counter
#   0) Exit
#
# Inputs:
# - option (string or int; user choice)
#
# Outputs:
# - "Hello!" for greeting
# - "Counter:" <counter_value> to show counter
# - "Counter incremented" when incrementing
# - "Bye!" when exiting
# - "Error: invalid option" for invalid choices
#
# Validations:
# - Convert option to int with error handling
# - Accept only 0, 1, 2, 3
#
# Key operations:
# - while True loop, break on 0
# - if/elif for actions
#
# Test cases (normal / edge / error):
# 1) Normal: 1, 3, 2, 0 -> greeting, increment, show counter, exit
# 2) Edge:   0 immediately -> Bye!
# 3) Error:  "x" or 9 -> Error: invalid option, continue
counter_value = 0

while True:
    print("Menu:")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_text = input("Problem 7.5 - Choose an option: ").strip()

    try:
        option = int(option_text)
    except ValueError:
        print("Error: invalid option")
        print()
        continue

    if option == 0:
        print("Bye!")
        break
    elif option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter_value)
    elif option == 3:
        counter_value += 1
        print("Counter incremented")
    else:
        print("Error: invalid option")

    print()  # blank line before showing menu again

print()  # separator


# ============================================================
# 7.6 PROBLEM 6: Pattern printing with nested loops
# ============================================================
# Description:
# - Print a right triangle pattern of '*' using nested loops for n rows.
# - Example for n=4:
#   *
#   **
#   ***
#   ****
# - Decision: also print an inverted pattern (documented here as "implemented").
#
# Inputs:
# - n (int; number of rows)
#
# Outputs:
# - Triangle pattern line by line
# - Inverted pattern line by line (implemented)
#
# Validations:
# - n must be convertible to int
# - n >= 1, otherwise print "Error: invalid input"
#
# Key operations:
# - for i in range(1, n + 1): print "*" * i
# - for i in range(n, 0, -1): print "*" * i
#
# Test cases (normal / edge / error):
# 1) Normal: n="4" -> prints 4-line triangle + 4-line inverted triangle
# 2) Edge:   n="1" -> prints "*" then "*" (inverted)
# 3) Error:  n="0" -> Error: invalid input
pattern_n_text = input("Problem 7.6 - Enter n (int, >= 1): ").strip()

try:
    pattern_n = int(pattern_n_text)
    if pattern_n < 1:
        print("Error: invalid input")
    else:
        # Normal triangle
        for i in range(1, pattern_n + 1):
            print("*" * i)

        # Inverted triangle (implemented)
        for i in range(pattern_n, 0, -1):
            print("*" * i)
except ValueError:
    print("Error: invalid input")


# ============================================================
# REFERENCES (5)
# ============================================================
# 1) for statements (Python language reference):
#    https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
#
# 2) while statements (Python language reference):
#    https://docs.python.org/3/reference/compound_stmts.html#the-while-statement
#
# 3) range() built-in (iteration with integer ranges):
#    https://docs.python.org/3/library/functions.html#func-range
#
# 4) Tutorial on control flow (if/elif/else, loops, break/continue):
#    https://docs.python.org/3/tutorial/controlflow.html
#
# 5) Built-in exceptions (ValueError handling for numeric conversions):
#    https://docs.python.org/3/library/exceptions.html#ValueError
# ============================================================
# Repositorio GitHub: https://github.com/amgel-lab/charly_tareas
# ============================================================