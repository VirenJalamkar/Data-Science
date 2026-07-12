# ==========================================================
# PYTHON ARITHMETIC OPERATORS
# ==========================================================

"""
1. Addition (+)
   Use: Adds two numbers.
   Example:
"""
print(10 + 5)          # Output: 15


"""
2. Subtraction (-)
   Use: Subtracts the second number from the first number.
   Example:
"""
print(10 - 5)          # Output: 5


"""
3. Multiplication (*)
   Use: Multiplies two numbers.
   Example:
"""
print(10 * 5)          # Output: 50


"""
4. Division (/)
   Use: Divides two numbers and returns a float value.
   Example:
"""
print(10 / 5)          # Output: 2.0


"""
5. Floor Division (//)
   Use: Divides two numbers and removes the decimal part.
   Example:
"""
print(10 // 3)         # Output: 3


"""
6. Modulus (%)
   Use: Returns the remainder after division.
   Example:
"""
print(10 % 3)          # Output: 1


"""
7. Exponent (**)
   Use: Raises the first number to the power of the second number.
   Example:
"""
print(2 ** 3)          # Output: 8


# ==========================================================
# PYTHON COMPARISON OPERATORS
# ==========================================================

"""
1. Equal To (==)
   Use: Checks whether two values are equal.
   Example:
"""
print(10 == 10)        # Output: True


"""
2. Not Equal To (!=)
   Use: Checks whether two values are different.
   Example:
"""
print(10 != 5)         # Output: True


"""
3. Greater Than (>)
   Use: Checks if the left value is greater than the right value.
   Example:
"""
print(10 > 5)          # Output: True


"""
4. Less Than (<)
   Use: Checks if the left value is less than the right value.
   Example:
"""
print(5 < 10)          # Output: True


"""
5. Greater Than or Equal To (>=)
   Use: Checks if the left value is greater than or equal to the right value.
   Example:
"""
print(10 >= 10)        # Output: True


"""
6. Less Than or Equal To (<=)
   Use: Checks if the left value is less than or equal to the right value.
   Example:
"""
print(5 <= 10)         # Output: True


# ==========================================================
# PYTHON LOGICAL OPERATORS
# ==========================================================

"""
1. AND (and)
   Use: Returns True if both conditions are True.
   Example:
"""
print(10 > 5 and 20 > 10)      # Output: True


"""
2. OR (or)
   Use: Returns True if at least one condition is True.
   Example:
"""
print(10 > 20 or 20 > 10)      # Output: True


"""
3. NOT (not)
   Use: Reverses the result.
   Example:
"""
print(not(10 > 5))             # Output: False


# ==========================================================
# PYTHON ASSIGNMENT OPERATORS
# ==========================================================

"""
1. Assignment (=)
   Use: Assigns a value to a variable.
"""
x = 10
print(x)                       # Output: 10


"""
2. Add and Assign (+=)
   Use: Adds a value and stores the result.
"""
x = 10
x += 5
print(x)                       # Output: 15


"""
3. Subtract and Assign (-=)
   Use: Subtracts a value and stores the result.
"""
x = 10
x -= 3
print(x)                       # Output: 7


"""
4. Multiply and Assign (*=)
   Use: Multiplies and stores the result.
"""
x = 10
x *= 2
print(x)                       # Output: 20


"""
5. Divide and Assign (/=)
   Use: Divides and stores the result.
"""
x = 10
x /= 2
print(x)                       # Output: 5.0


# ==========================================================
# PYTHON MEMBERSHIP OPERATORS
# ==========================================================

"""
1. IN (in)
   Use: Checks whether a value exists in a sequence.
   Example:
"""
print("Apple" in ["Apple", "Banana"])      # Output: True


"""
2. NOT IN (not in)
   Use: Checks whether a value does not exist.
   Example:
"""
print("Orange" not in ["Apple", "Banana"]) # Output: True


# ==========================================================
# PYTHON IDENTITY OPERATORS
# ==========================================================

"""
1. IS (is)
   Use: Checks whether two variables refer to the same object.
"""
a = [1, 2]
b = a
print(a is b)                  # Output: True


"""
2. IS NOT (is not)
   Use: Checks whether two variables refer to different objects.
"""
a = [1, 2]
b = [1, 2]
print(a is not b)              # Output: True