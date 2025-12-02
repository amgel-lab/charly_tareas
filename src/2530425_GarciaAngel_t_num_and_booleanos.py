"""
    Nombre: Angel Javier García Nieto
    Matrícula: 2530425
    Grupo: IM 1-1

 - Python supports integers (int) with arbitrary precision and floating-point numbers (float)
   using IEEE 754 double precision (so small rounding artifacts can happen with decimals).
 - Conversions: int("10"), float("3.14") raise ValueError if the text is not numeric.
 - Boolean values are True / False, produced by comparisons (>=, <=, ==, !=, <, >) and
   combined with logical operators: and, or, not (short-circuit evaluation).
 - Useful numeric helpers:
   * min(), max() for bounds and selecting extremes
   * round(x, 2) for display rounding
 - A common pattern is: validate inputs -> compute intermediate values -> compute booleans
   -> print results. Always guard against invalid or impossible states (e.g., division by zero).
"""
# ============================================================
# PROBLEM 1: Temperature converter and range flag
# ============================================================
# Description:
# - Convert a temperature from Celsius (float) to Fahrenheit and Kelvin.
# - Also compute a boolean flag is_high_temperature:
#   * true if temp_c >= 30.0, otherwise false
#
# Inputs:
# - temp_c (float; temperature in °C)
#
# Outputs:
# - "Fahrenheit:" <temp_f>
# - "Kelvin:" <temp_k>
# - "High temperature:" true|false
#
# Validations:
# - temp_c must be convertible to float
# - Kelvin must not be physically impossible: temp_k >= 0.0
#
# Key operations:
# - temp_f = temp_c * 9 / 5 + 32
# - temp_k = temp_c + 273.15
# - is_high_temperature = (temp_c >= 30.0)
#
# Test cases (normal / edge / error):
# 1) Normal: temp_c = "25"
#    - Fahrenheit: 77.0, Kelvin: 298.15, High temperature: false
# 2) Edge: temp_c = "30.0"
#    - High temperature: true (boundary)
# 3) Error: temp_c = "-300"
#    - Kelvin < 0.0 => invalid
# ============================================================
temp_c_text = input("Problem 7.1 - Enter temperature in Celsius: ").strip()

try:
    temp_c = float(temp_c_text)
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15

    if temp_k < 0.0:
        print("Error: invalid input")
    else:
        is_high_temperature = (temp_c >= 30.0)
        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", str(is_high_temperature).lower())
except ValueError:
    print("Error: invalid input")

print()  # separator

# ============================================================
# PROBLEM 2: Work hours and overtime payment
# ============================================================
# Description:
# - Compute weekly pay:
#   * Up to 40 hours at hourly_rate
#   * Overtime hours (> 40) paid at 150% (hourly_rate * 1.5)
# - Also compute has_overtime boolean: true if hours_worked > 40
#
# Inputs:
# - hours_worked (float; hours worked in the week)
# - hourly_rate (float; pay per hour)
#
# Outputs:
# - "Regular pay:" <regular_pay>
# - "Overtime pay:" <overtime_pay>
# - "Total pay:" <total_pay>
# - "Has overtime:" true|false
#
# Validations:
# - hours_worked >= 0
# - hourly_rate > 0
# - If invalid, print: "Error: invalid input"
#
# Key operations:
# - regular_hours = min(hours_worked, 40)
# - overtime_hours = max(hours_worked - 40, 0)
# - overtime_pay = overtime_hours * hourly_rate * 1.5
# - has_overtime = (hours_worked > 40)
#
# Test cases (normal / edge / error):
# 1) Normal: hours_worked="45", hourly_rate="100"
#    - Regular pay: 4000, Overtime pay: 750, Total: 4750, Has overtime: true
# 2) Edge: hours_worked="40", hourly_rate="200"
#    - Overtime pay: 0, Has overtime: false (boundary)
# 3) Error: hours_worked="-2", hourly_rate="100"
#    - invalid input
hours_text = input("Problem 7.2 - Enter hours worked: ").strip()
rate_text = input("Problem 7.2 - Enter hourly rate: ").strip()

try:
    hours_worked = float(hours_text)
    hourly_rate = float(rate_text)

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40.0)
        overtime_hours = max(hours_worked - 40.0, 0.0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        has_overtime = (hours_worked > 40.0)

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", str(has_overtime).lower())
except ValueError:
    print("Error: invalid input")


print()  # separator


# ============================================================
# PROBLEM 3: Discount eligibility with booleans
# ============================================================
# Description:
# - Determine if a customer is eligible for a 10% discount.
# - Eligible if:
#   * is_student is true OR
#   * is_senior is true OR
#   * purchase_total >= 1000.0
# - If eligible, final_total = purchase_total * 0.9 else purchase_total
#
# Inputs:
# - purchase_total (float)
# - is_student_text (string; "YES" or "NO")
# - is_senior_text (string; "YES" or "NO")
#
# Outputs:
# - "Discount eligible:" true|false
# - "Final total:" <final_total>
#
# Validations:
# - purchase_total >= 0.0
# - Normalize is_student_text and is_senior_text to uppercase
# - If either text is not "YES" or "NO", print: "Error: invalid input"
#
# Key operations:
# - is_student = (is_student_text == "YES")
# - is_senior  = (is_senior_text  == "YES")
# - discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
#
# Test cases (normal / edge / error):
# 1) Normal: total="1200", student="NO", senior="NO" -> eligible true, final 1080
# 2) Edge: total="1000", student="NO", senior="NO" -> eligible true, final 900
# 3) Error: total="500", student="MAYBE", senior="NO" -> invalid input
total_text = input("Problem 7.3 - Enter purchase total: ").strip()
student_text = input('Problem 7.3 - Is student? (YES/NO): ').strip()
senior_text = input('Problem 7.3 - Is senior? (YES/NO): ').strip()

try:
    purchase_total = float(total_text)
    if purchase_total < 0.0:
        print("Error: invalid input")
    else:
        student_norm = student_text.upper()
        senior_norm = senior_text.upper()

        if student_norm not in ("YES", "NO") or senior_norm not in ("YES", "NO"):
            print("Error: invalid input")
        else:
            is_student = (student_norm == "YES")
            is_senior = (senior_norm == "YES")

            discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
            final_total = purchase_total * 0.9 if discount_eligible else purchase_total

            print("Discount eligible:", str(discount_eligible).lower())
            print("Final total:", final_total)
except ValueError:
    print("Error: invalid input")


print()  # separator


# ============================================================
# PROBLEM 4: Basic statistics of three integers
# ============================================================
# Description:
# - Read three integers and compute:
#   * sum (int)
#   * average (float)
#   * max value
#   * min value
#   * all_even boolean (true if all three are even)
#
# Inputs:
# - n1 (int), n2 (int), n3 (int)
#
# Outputs:
# - "Sum:" <sum_value>
# - "Average:" <average_value>
# - "Max:" <max_value>
# - "Min:" <min_value>
# - "All even:" true|false
#
# Validations:
# - All three values must be convertible to int
# - Negative values are allowed
#
# Key operations:
# - sum_value = n1 + n2 + n3
# - average_value = sum_value / 3
# - max(), min()
# - all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
#
# Test cases (normal / edge / error):
# 1) Normal: "2", "7", "10" -> sum 19, all_even false
# 2) Edge: "-4", "-2", "0" -> all_even true
# 3) Error: "10", "x", "3" -> invalid input
n1_text = input("Problem 7.4 - Enter n1 (int): ").strip()
n2_text = input("Problem 7.4 - Enter n2 (int): ").strip()
n3_text = input("Problem 7.4 - Enter n3 (int): ").strip()

try:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())
except ValueError:
    print("Error: invalid input")


print()  # separator


# ============================================================
# PROBLEM 5: Loan eligibility (income and debt ratio)
# ============================================================
# Description:
# - Determine loan eligibility using:
#   * monthly_income (float)
#   * monthly_debt (float)
#   * credit_score (int)
# - debt_ratio = monthly_debt / monthly_income
# - eligible is true if:
#   * monthly_income >= 8000.0 AND
#   * debt_ratio <= 0.4 AND
#   * credit_score >= 650
#
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
#
# Outputs:
# - "Debt ratio:" <debt_ratio>
# - "Eligible:" true|false
#
# Validations:
# - monthly_income > 0.0 (avoid division by zero)
# - monthly_debt >= 0.0
# - credit_score >= 0
# - If invalid, print: "Error: invalid input"
#
# Key operations:
# - debt_ratio = monthly_debt / monthly_income
# - eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)
#
# Test cases (normal / edge / error):
# 1) Normal: income="10000", debt="3500", score="700" -> eligible true
# 2) Edge: income="8000", debt="3200", score="650" -> ratio 0.4, eligible true
# 3) Error: income="0", debt="100", score="700" -> invalid input
income_text = input("Problem 7.5 - Enter monthly income: ").strip()
debt_text = input("Problem 7.5 - Enter monthly debt: ").strip()
score_text = input("Problem 7.5 - Enter credit score (int): ").strip()

try:
    monthly_income = float(income_text)
    monthly_debt = float(debt_text)
    credit_score = int(score_text)

    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

        print("Debt ratio:", debt_ratio)
        print("Eligible:", str(eligible).lower())
except ValueError:
    print("Error: invalid input")


print()  # separator


# ============================================================
# PROBLEM 6: Body Mass Index (BMI) and category flags
# ============================================================
# Description:
# - Compute BMI:
#   bmi = weight_kg / (height_m * height_m)
# - Also compute boolean category flags:
#   * is_underweight: bmi < 18.5
#   * is_normal:      18.5 <= bmi < 25.0
#   * is_overweight:  bmi >= 25.0
#
# Inputs:
# - weight_kg (float)
# - height_m (float)
#
# Outputs:
# - "BMI:" <bmi_rounded_to_2_decimals>
# - "Underweight:" true|false
# - "Normal:" true|false
# - "Overweight:" true|false
#
# Validations:
# - weight_kg > 0.0
# - height_m > 0.0
# - If invalid, print: "Error: invalid input"
#
# Key operations:
# - round(bmi, 2)
# - chained comparisons for ranges (e.g., 18.5 <= bmi < 25.0)
#
# Test cases (normal / edge / error):
# 1) Normal: weight="70", height="1.75" -> BMI 22.86, normal true
# 2) Edge: weight="74", height="2.0" -> BMI 18.5, normal true (boundary)
# 3) Error: weight="70", height="0" -> invalid input
weight_text = input("Problem 7.6 - Enter weight (kg): ").strip()
height_text = input("Problem 7.6 - Enter height (m): ").strip()

try:
    weight_kg = float(weight_text)
    height_m = float(height_text)

    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, 2)

        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print("BMI:", bmi_rounded)
        print("Underweight:", str(is_underweight).lower())
        print("Normal:", str(is_normal).lower())
        print("Overweight:", str(is_overweight).lower())
except ValueError:
    print("Error: invalid input")
# ============================================================
# REFERENCES (5)
# ============================================================
# 1) Python Built-in Types (numbers, strings, booleans, methods):
#    https://docs.python.org/3/library/stdtypes.html
#
# 2) Python Built-in Functions (min, max, round, etc.):
#    https://docs.python.org/3/library/functions.html
#
# 3) Python Tutorial: More Control Flow Tools (if/else, boolean logic patterns):
#    https://docs.python.org/3/tutorial/controlflow.html
#
# 4) Python Floating Point Arithmetic: Issues and Limitations (IEEE 754 behavior):
#    https://docs.python.org/3/tutorial/floatingpoint.html
#
# 5) WHO BMI classification (BMI thresholds commonly used in practice):
#    https://www.who.int/data/gho/data/themes/topics/topic-details/GHO/body-mass-index
# ============================================================
# Repositorio GitHub: https://github.com/amgel-lab/charly_tareas
# ============================================================
