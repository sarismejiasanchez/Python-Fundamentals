x = 5

x += 3 # Addition assignment operator
print(x)  # Output: 8

x -= 3 # Subtraction assignment operator
print(x)  # Output: 5

x *= 3 # Multiplication assignment operator
print(x)  # Output: 15

x /= 3 # Division assignment operator
print(x)  # Output: 5.0

x %= 3 # Modulus assignment operator
print(x)  # Output: 2.0

x //= 2 # Floor division assignment operator
print(x)  # Output: 1.0

y = 21
y //= 2 # Floor division operator
print(y)  # Output: 10 (y is updated to the result of the floor division)

# Using modulos and floor division together
z = 21
z //= 2 # Floor division assignment operator
print(z)  # Output: 10 (z is updated to the result of the floor division)
z = 21 % 2 # Modulus assignment operator
print(z)  # Output: 0 (z is updated to the result of the modulus operation) 

y = 20
y **= 3 # Exponentiation assignment operator
print(y)  # Output: 8000 (y is updated to the result of raising 20 to the power of 3)

# Walrus operator example (Morsa) :=
print(z := 3) # Output: 3 (z is assigned the value 3 and then printed)
print(z) # Output: 3 (z retains the value assigned by the walrus operator

