# Comparison operators: ==, !=, >, <, >=, <=
x = 5
y = 3
z = 5

print(x == y)  # Output: False (5 is not equal to 3)
print(x != y)  # Output: True (5 is not equal to 3)
print(x > y)   # Output: True (5 is greater than 3)
print(x > z)   # Output: False (5 is not greater than 5)
print(x < y)   # Output: False (5 is not less than 3)
print(x >= y)  # Output: True (5 is greater than or equal to 3)
print(x >= z)  # Output: True (5 is greater than or equal to 5)
print(x <= y)  # Output: False (5 is not less than or equal to 3)
print(x <= z)  # Output: True (5 is less than or equal to 5)

# Logical operators: and, or, not
# and, both conditions must be true for the result to be true
print(x > y and y > z)  # Output: False (5 is greater than 3 but 3 is not greater than 5)

# or, at least one condition must be true for the result to be true
print(x > y or y > z)   # Output: True (5 is greater than 3)

# not, negates the result of a condition
print(not x > y)        # Output: False (5 is greater than 3, so not True is False)
print(not x < y)        # Output: True (5 is not less than 3, so not False is True)
var = True
print(not var)          # Output: False (not True is False)
print(not(not var))     # Output: True (not False is True)
var = False
print(not var)          # Output: True (not False is True)
print(not(not var))     # Output: False (not True is False)
