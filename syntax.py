if 5 > 3:
    print("5 is greater than 3")

"""
if 2 < 1:
print("2 is less than 1") # IndentationError: expected an indented block
"""

# This is functionaly but not syntactically correct
if 5 > 3:
        print("5 is indeed greater than 3")

if 5 > 3:
    if 4 > 3:
        print("4 is greater than 3")
    
    print("5 is greater than 3")