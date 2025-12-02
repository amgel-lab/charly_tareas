"""
    Nombre: Angel Javier García Nieto
    Matrícula: 2530425
    Grupo: IM 1-1

    En Python, los strings (str) representan texto
    Unicode y son inmutables: 'cualquier cambio' realmente
    crea una nueva cadena. Esto hace muy comunes operaciones
    como indexación y slicing (s[0], s[-1], s[a:b], s[::-1])
    y el uso de métodos strip(), lower(), upper(), title(),
    split(), join(), replace(), find(), count(), isalpha(), etc.
    para transformar texto sin modificar el original.
    Para validar o analizar texto se suelen usar: busquedas (in, find()),
    conteos (count()) y recorridos carácter por carácter. Para construir
    salidas legibles, lo más claro hoy es usar f-strings
    (interpolación y formato), incluyendo especificaciones como :.2f para números.
"""
# ============================================================
# Problem 1: Full name formatter (name + initials)
# ============================================================
# Description:
# - Normalize a full name string (trim and collapse extra spaces, handle mixed casing),
#   then print the name in Title Case and its initials (e.g., J.C.T.).
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - "Formatted name: <Title Case Name>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - Must not be empty after strip()
# - Must contain at least two words after split()
# - Must not be only whitespace
#
# Key operations:
# - strip(), split(), title(), concatenation/join, len()
#
# Test cases (normal / edge / error):
# 1) Normal:
#    - full_name = "juan carlos tovar"
#    - Output: "Formatted name: Juan Carlos Tovar", "Initials: J.C.T."
# 2) Edge:
#    - full_name = "   mArIA   deL   cArMen  "
#    - Output: "Formatted name: Maria Del Carmen", "Initials: M.D.C."
# 3) Error:
#    - full_name = "Plato"
#    - Output: invalid (only 1 word)
# ============================================================
full_name = input("Insert your full name: ")
full_name = full_name.strip()
if not full_name:
    print("Error: Please insert a name.")
    exit()
words = full_name.split()
if len(words) < 2:
    print("Error: Please insert at least a first name and a last name.")
    exit()
clean_full_name = " ".join(words)
formatted_name = clean_full_name.title()
initials = ""
for word in words:
    initials += word[0].upper() + "."
print("Formatted Name: ", formatted_name)
print("Initials: ", initials)
# ============================================================
# Problem 2
# ============================================================
# Description:
# - Validate a basic email format:
#   * exactly one '@'
#   * no spaces
#   * at least one '.' after '@'
# - If valid, also print the domain part (text after '@').
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - If valid: "Domain: <domain_part>"
#
# Validations:
# - Not empty after strip()
# - Exactly one '@' (count("@") == 1)
# - No spaces (" " not in email_text)
# - Domain part contains at least one '.' ("." in domain_part)
#
# Key operations:
# - strip(), count(), find(), slicing, in / not in
#
# Test cases (normal / edge / error):
# 1) Normal:
#    - email_text = "user.name@school.edu"
#    - Output: true, Domain: school.edu
# 2) Edge:
#    - email_text = "a@b.c"
#    - Output: true, Domain: b.c
# 3) Error:
#    - email_text = "user@@mail.com"
#    - Output: false
# ============================================================
email_text = input("Enter email: ").strip()
if not email_text:
    print("Valid email: false")
else:
    at_count = email_text.count("@")
    has_spaces = " " in email_text
    if at_count == 1 and not has_spaces:
        at_index = email_text.find("@")
        domain_part = email_text[at_index + 1:]
        if "." in domain_part:
            print("Valid email: true")
            print("Domain:", domain_part)
        else:
            print("Valid email: false")
    else:
        print("Valid email: false")
# ============================================================
# Problem 3
# ============================================================
# Description:
# - Determine whether a phrase is a palindrome ignoring spaces and case.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - "Is palindrome: true" or "Is palindrome: false"
# - (Optional) print the normalized phrase
#
# Validations:
# - Not empty after strip()
# - After normalization (remove spaces), length should be >= 3
#
# Key operations:
# - lower(), replace(" ", ""), reverse slicing text[::-1], comparison ==
#
# Test cases (normal / edge / error):
# 1) Normal:
#    - phrase = "Anita lava la tina"
#    - Output: true
# 2) Edge:
#    - phrase = "A a"
#    - Normalized: "aa" (len 2) -> Output: false (fails min length rule)
# 3) Error:
#    - phrase = "   "
#    - Output: false
# ============================================================
phrase = input("Enter a phrase: ").strip()
if not phrase:
    print("Is palindrome: false")
else:
    normalized = phrase.lower().replace(" ", "")
    if len(normalized) < 3:
        print("Is palindrome: false")
    else:
        reversed_text = normalized[::-1]
        if normalized == reversed_text:
            print("Is palindrome: true")
            print("Normalized phrase:", normalized)
        else:
            print("Is palindrome: false")
            print("Normalized phrase:", normalized)
# ============================================================
# Problem 4
# ============================================================
# Description:
# - Normalize a sentence, split it into words, then print:
#   * total word count
#   * first word
#   * last word
#   * shortest word (by length)
#   * longest word (by length)
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"
#
# Validations:
# - Not empty after strip()
# - Must contain at least one word after split()
#
# Key operations:
# - strip(), split(), len(), loop or min/max(words, key=len)
#
# Test cases (normal / edge / error):
# 1) Normal:
#    - sentence = "Python is really fun"
#    - Output: count 4, first Python, last fun, shortest is, longest really
# 2) Edge:
#    - sentence = "Hello"
#    - Output: count 1, first/last Hello, shortest/longest Hello
# 3) Error:
#    - sentence = "    "
#    - Output: invalid / no words (handle gracefully)
# ============================================================
sentence = input("Enter a sentence: ").strip()
if not sentence:
    print("Word count: 0")
else:
    words = sentence.split()
    if len(words) == 0:
        print("Word count: 0")
    else:
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]
        shortest_word = min(words, key=len)
        longest_word = max(words, key=len)
        print("Word count:", word_count)
        print("First word:", first_word)
        print("Last word:", last_word)
        print("Shortest word:", shortest_word)
        print("Longest word:", longest_word)
# ============================================================
# Problem 5
# ============================================================
# Description:
# - Classify a password as "weak", "medium", or "strong" based on rules:
#   * weak: empty OR length < 8 OR very simple (only digits or only letters in one case)
#   * strong: length >= 8 AND has uppercase + lowercase + digit + symbol (non-alphanumeric)
#   * medium: length >= 8 but not strong (and not considered "simple weak")
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
#
# Validations:
# - Must not be empty
# - Check length with len()
#
# Key operations:
# - Loop through characters
# - isupper(), islower(), isdigit(), isalnum()
# - Boolean flags (has_upper, has_lower, has_digit, has_symbol)
#
# Test cases (normal / edge / error):
# 1) Normal (strong):
#    - password_input = "Abcdef1!"
#    - Output: strong
# 2) Edge (medium):
#    - password_input = "Password1"
#    - Output: medium (no symbol)
# 3) Error:
#    - password_input = ""
#    - Output: weak
# ============================================================
password_input = input("Enter password: ")
if not password_input:
    print("Password strength: weak")
else:
    length_ok = len(password_input) >= 8
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    for ch in password_input:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_symbol = True
    if not length_ok:
        strength = "weak"
    else:
        is_strong = has_upper and has_lower and has_digit and has_symbol
        only_digits = password_input.isdigit()
        only_lower_letters = password_input.isalpha() and password_input.islower()
        only_upper_letters = password_input.isalpha() and password_input.isupper()
        if is_strong:
            strength = "strong"
        elif only_digits or only_lower_letters or only_upper_letters:
            strength = "weak"
        else:
            strength = "medium"
    print("Password strength:", strength)
# ============================================================
# Problem 6
# ============================================================
# Description:
# - Build a label in one line:
#     "Product: <NAME> | Price: $<PRICE>"
# - The final string must be exactly 30 characters:
#   * if shorter -> pad with spaces to the right
#   * if longer  -> truncate to 30 chars (label[:30])
#
# Inputs:
# - product_name (string)
# - price_value (string or number)
#
# Outputs:
# - 'Label: "<exactly 30 characters>"'  (quotes help show trailing spaces)
#
# Validations:
# - product_name not empty after strip()
# - price_value convertible to a positive number (> 0)
#
# Key operations:
# - f-strings / concatenation, len(), slicing, right-padding with spaces
#
# Test cases (normal / edge / error):
# 1) Normal (pads):
#    - product_name = "Pen", price_value = "5"
#    - Output: label padded to 30 characters
# 2) Edge (truncates):
#    - product_name = "Ultra Long Product Name 2025 Edition", price_value = "99.99"
#    - Output: label truncated to 30 characters
# 3) Error:
#    - product_name = "Milk", price_value = "-3"
#    - Output: invalid (should not generate a valid label)
# ============================================================
product_name = input("Enter product name: ").strip()
price_text = input("Enter price: ").strip()
if not product_name:
    print("Label: \"\"")
else:
    try:
        price_number = float(price_text)
    except ValueError:
        price_number = -1
    if price_number <= 0:
        print("Label: \"\"")
    else:
        price_str = f"{price_number:.2f}"
        label = f"Product: {product_name} | Price: ${price_str}"
        if len(label) < 30:
            label = label + " " * (30 - len(label))
        else:
            label = label[:30]
        print(f"Label: \"{label}\"")
# ============================================================
print("End of the program.")
# ============================================================
# REFERENCES (5)
# ============================================================
# 1) Built-in Types (str methods, sequences, etc.):
#    https://docs.python.org/3/library/stdtypes.html
#
# 2) PEP 498 (f-strings / literal string interpolation):
#    https://peps.python.org/pep-0498/
#
# 3) Format Specification Mini-Language (format specifiers like :.2f, width, alignment):
#    https://docs.python.org/3/library/string.html#format-specification-mini-language
#
# 4) Python Tutorial: Input and Output (f-strings and formatting examples):
#    https://docs.python.org/3/tutorial/inputoutput.html
#
# 5) Built-in Types (Spanish mirror, explains str immutability and Unicode):
#    https://docs.python.org/es/3/library/stdtypes.html
# ============================================================
# Repositorio GitHub: https://github.com/amgel-lab/charly_tareas
# ============================================================