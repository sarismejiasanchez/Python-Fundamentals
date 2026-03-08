from operator import mul


x = 5
y = 10

# Addition +
addition = x + y
print("Addition:", addition)

# Subtraction -
subtraction = x - y
print("Subtraction:", subtraction)

# Multiplication *
multiplication = x * y
print("Multiplication:", multiplication)

# Division /
division = x / y
print("Division:", division)

# Floor Division //
floor_division = x // y 
print("Floor Division:", floor_division)

# Modulus %
modulus = x % y
print("Modulus:", modulus)

# Exponentiation **
exponentiation = y ** 5
print("Exponentiation:", exponentiation)

# Example of modulus operator to check if a number is even or odd
num = 8
result = num % 2
print(f"{num} is {'even' if result == 0 else 'odd'}")

num = 9
result = num % 2
print(f"{num} is {'even' if result == 0 else 'odd'}")

# Precedence of operators
# 1. Parentheses
# 2. Exponentiation
# 3. Multiplication, Division, Floor Division, Modulus
# 4. Addition, Subtraction
# 5. Comparison identity, membership operators
# 6. Logical operators