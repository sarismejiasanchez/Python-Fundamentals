# In Python, the boolean values are represented by the keywords True and False.
var = True
print(var) # Output: True
var = False
print(var) # Output: False
print(type(var)) # Output: <class 'bool'>

# Boolean values can be used in conditional statements to control the flow of the program.
var = (5 > 3) # This expression evaluates to True
print(var) # Output: True
var = (5 < 3) # This expression evaluates to False
print(var) # Output: False

print(bool("Hello, World!")) # Output: True (non-empty string is considered True)
print(bool("")) # Output: False (empty string is considered False)
print(bool(None)) # Output: False (None is considered False)

# True
print(bool(1)) # Output: True (non-zero number is considered True)
print(bool([4, 5, 6])) # Output: True (non-empty list is considered True)
print(bool((1, 2, 3))) # Output: True (non-empty tuple is considered True)
print(bool({"key": "value"})) # Output: True (non-empty dictionary is considered True)

# False
print(bool(0)) # Output: False (zero is considered False)
print(bool([])) # Output: False (empty list is considered False)
print(bool(())) # Output: False (empty tuple is considered False)
print(bool({})) # Output: False (empty dictionary is considered False)

x = 123
print(isinstance(x, int)) # Output: True (x is an instance of int)
print(isinstance(x, float)) # Output: False (x is not an instance of float