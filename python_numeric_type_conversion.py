# Number types in Python include int, float, and complex.
x = 1
y = 2.5
z = 1j

# Print the types of the variables
print(type(x)) # Output: <class 'int'>
print(type(y)) # Output: <class 'float'>
print(type(z)) # Output: <class 'complex'>

# Positive and negative numbers
positive = 5
negative = -5
float_positive = 5.0
float_negative = -5.0

imaginary_positive = 5 + 1j
imaginary_negative = -5 - 1j

# Type conversion or casting
# You can convert between different numeric types using the built-in functions int(), float(), and complex().
print(x) # Output: 1
xf = float(x) # Convert int to float
print(xf) # Output: 1.0
print(type(xf)) # Output: <class 'float'>

print(y) # Output: 2.5
yi = int(y) # Convert float to int (truncates the decimal part)
print(yi) # Output: 2
print(type(yi)) # Output: <class 'int'>


int_number = 5
float_number = 5.5

int_complex = complex(int_number) # Convert int to complex
print(int_complex) # Output: (5+0j) 
print(type(int_complex)) # Output: <class 'complex'>
float_complex = complex(float_number) # Convert float to complex
print(float_complex) # Output: (5.5+0j)
print(type(float_complex)) # Output: <class 'complex'>


import random as rnd

# Generate a random integer between 1 and 10
rand_range = rnd.randrange(1, 10) # Output: A random integer between 1 and 10 (inclusive of 1, exclusive of 10)
print(rand_range)

# Generate a random float between 2.5 and 8.5
rand_float = rnd.uniform(2.5, 8.5) # Output: A random float between 2.5 and 8.5
print(rand_float)
print(round(rand_float, 4)) # Round to 4 decimal places

# Generate a random complex number with real part between 1 and 5 and imaginary part between 1 and 5
rand_complex = complex(rnd.uniform(1, 5), rnd.uniform(1, 5)) # Output: A random complex number with real part between 1 and 5 and imaginary part between 1 and 5
print(rand_complex)