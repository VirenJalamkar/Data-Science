# ==========================================================
# PYTHON DATA TYPES
# ==========================================================

"""
Python provides different built-in data types to store data.

Main Data Types:
1. String
2. Number (int, float, complex)
3. Tuple
4. List
5. Dictionary
6. Set
7. Frozenset
"""

# ==========================================================
# Mutable and Immutable Data Types
# ==========================================================

"""
Mutable Data Types
------------------
These data types can be modified after creation.

1. List
2. Dictionary
3. Set

Example:
my_list = [1, 2, 3]
my_list.append(4)    # Allowed
"""

"""
Immutable Data Types
--------------------
These data types cannot be modified after creation.

1. String
2. Number (int, float, complex)
3. Tuple
4. Frozenset

Example:
text = "Python"
# text[0] = "J"      # Not Allowed
"""

# ==========================================================
# DATA TYPE DECLARATION
# ==========================================================

# -------------------------
# 1. String
# -------------------------
string_var = "Hello Python"

print(string_var)
print(type(string_var))


# -------------------------
# 2. Number
# -------------------------

# Integer
int_var = 22

# Float
float_var = 12.5

# Complex
complex_var = 2 + 3j

print(int_var)
print(type(int_var))

print(float_var)
print(type(float_var))

print(complex_var)
print(type(complex_var))


# -------------------------
# 3. Tuple
# -------------------------
tuple_var = ("Name", "Age")

print(tuple_var)
print(type(tuple_var))


# -------------------------
# 4. List
# -------------------------
list_var = ["Name", "Age"]

print(list_var)
print(type(list_var))


# -------------------------
# 5. Dictionary
# -------------------------
dict_var = {
    "Name": "Viren",
    "Age": 22
}

print(dict_var)
print(type(dict_var))


# -------------------------
# 6. Set
# -------------------------
set_var = {1, 2, 3}

print(set_var)
print(type(set_var))


# -------------------------
# 7. Frozenset
# -------------------------
frozenset_var = frozenset([1, 2, 3])

print(frozenset_var)
print(type(frozenset_var))