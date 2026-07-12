# ==========================================================
# PYTHON CONDITIONAL STATEMENTS
# ==========================================================

"""
Conditional Statements are used to make decisions in a program.

Python checks whether a condition is True or False.
If the condition is True, a block of code is executed.
Otherwise, another block of code can be executed.

Types of Conditional Statements:
1. if
2. if...else
3. if...elif...else
4. Nested if
5. Short-hand if
6. Short-hand if...else (Ternary Operator)
"""

# ==========================================================
# 1. IF STATEMENT
# ==========================================================

"""
Syntax:

if condition:
    statement

Use:
Executes the code only when the condition is True.
"""

age = 20

if age >= 18:
    print("You are eligible to vote.")

# Output:
# You are eligible to vote.


# ==========================================================
# 2. IF...ELSE STATEMENT
# ==========================================================

"""
Syntax:

if condition:
    statement
else:
    statement

Use:
Executes one block if the condition is True,
otherwise executes the else block.
"""

age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

# Output:
# You cannot vote.


# ==========================================================
# 3. IF...ELIF...ELSE STATEMENT
# ==========================================================

"""
Syntax:

if condition1:
    statement
elif condition2:
    statement
else:
    statement

Use:
Checks multiple conditions.
The first True condition is executed.
"""

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# Output:
# Grade B


# ==========================================================
# 4. NESTED IF STATEMENT
# ==========================================================

"""
Syntax:

if condition1:
    if condition2:
        statement

Use:
An if statement inside another if statement.
"""

age = 22
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a driving license.")
else:
    print("You are underage.")

# Output:
# You can drive.


# ==========================================================
# 5. SHORT-HAND IF
# ==========================================================

"""
Syntax:

if condition: statement

Use:
Used when only one statement needs to be executed.
"""

age = 20

if age >= 18: print("Adult")

# Output:
# Adult


# ==========================================================
# 6. SHORT-HAND IF...ELSE (TERNARY OPERATOR)
# ==========================================================

"""
Syntax:

value_if_true if condition else value_if_false

Use:
Executes one statement if the condition is True,
otherwise executes another statement.
"""

age = 16

print("Adult") if age >= 18 else print("Minor")

# Output:
# Minor


# ==========================================================
# PRACTICE EXAMPLES
# ==========================================================

# Example 1: Check Positive Number

number = 10

if number > 0:
    print("Positive Number")

# Output:
# Positive Number


# Example 2: Check Even or Odd

number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Output:
# Odd Number


# Example 3: Find Largest Number

a = 10
b = 20

if a > b:
    print("a is Greater")
else:
    print("b is Greater")

# Output:
# b is Greater


# Example 4: Student Result

marks = 45

if marks >= 35:
    print("Pass")
else:
    print("Fail")

# Output:
# Pass