"""
    Nombre: Angel Javier García Nieto
    Matrícula: 2530425
    Grupo: IM 1-1

- The Fibonacci sequence starts with 0 and 1, and each next term is the sum of the previous two.
Example: 0, 1, 1, 2, 3, 5, 8, ...
- This is a classic use-case for loops and accumulators:
* keep two variables (a, b) representing consecutive Fibonacci terms
* update them each iteration: a, b = b, a + b
- Input validation is essential:
* n must be an integer
* n must be >= 1
* optional upper limit (e.g., n <= 50) to keep outputs reasonable
"""

# ============================================================
# 6.1 PROBLEM: Fibonacci series up to n terms
# ============================================================
# Description:
# - Read an integer n and print the Fibonacci series up to n terms.
# - The series starts with 0 and 1:
#   * n = 1 -> 0
#   * n = 2 -> 0, 1
#   * n = 7 -> 0, 1, 1, 2, 3, 5, 8
#
# Inputs:
# - n (int; number of terms to generate)
#
# Outputs:
# - (Optional) "Number of terms:" <n>
# - "Fibonacci series:" <term_1> <term_2> ... <term_n>
#
# Validations:
# - n must be convertible to int
# - n >= 1
# - Optional: n <= 50 to avoid very large series (implemented here)
# - If validation fails, print "Error: invalid input" and do NOT compute the series
#
# Key operations:
# - Use a loop (for) and keep two variables:
#   a = 0, b = 1
#   for _ in range(n):
#       output a
#       a, b = b, a + b
#
# Test cases (normal / edge / error):
# 1) Normal: n = "7"
#    - Fibonacci series: 0 1 1 2 3 5 8
# 2) Edge: n = "1"
#    - Fibonacci series: 0
# 3) Error: n = "0" (or "abc" or "60")
#    - Error: invalid input
MAX_N = 50  # optional safety limit

n_text = input("Problem 6.1 - Enter number of Fibonacci terms (1..50): ").strip()

try:
    n = int(n_text)
    if n < 1 or n > MAX_N:
        print("Error: invalid input")
    else:
        a = 0
        b = 1
        series = []

        for _ in range(n):
            series.append(a)
            a, b = b, a + b

        print("Number of terms:", n)
        print("Fibonacci series:", " ".join(str(x) for x in series))
except ValueError:
    print("Error: invalid input")


# ============================================================
# REFERENCES (5)
# ============================================================
# 1) for statement (Python language reference):
#    https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
#
# 2) range() built-in (iteration over integer sequences):
#    https://docs.python.org/3/library/functions.html#func-range
#
# 3) Built-in types: integers and arithmetic behavior:
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
#
# 4) Errors and exceptions (ValueError on int conversion):
#    https://docs.python.org/3/tutorial/errors.html
#
# 5) Fibonacci sequence overview (MathWorld - Wolfram):
#    https://mathworld.wolfram.com/FibonacciNumber.html
# ============================================================
# Repositorio GitHub: https://github.com/amgel-lab/charly_tareas
# ============================================================