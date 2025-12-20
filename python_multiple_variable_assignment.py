# Assigning multiple variables in a single line
x, y, z = "Apple", "Orange", "Banana"
print(x, y, z)  # Output: Apple Orange Banana

# Assigning the same value to multiple variables
a = b = c = "Tangerine"
print(a, b, c)  # Output: Tangerine Tangerine Tangerine

# Concatenating variable values in a print statement
print("My favorite fruit is " + x) # Output: My favorite fruit is Apple
print(a + " " + z) # Output: Tangerine Banana
print(a + z)    # Output: TangerineBanana

# Performing arithmetic operations with multiple variables
d = 5
e = 6
print(d + e)  # Output: 11

# Challenging example: swapping variable values
m = 10
n = 20
print("Before swapping: m =", m, ", n =", n)  # Output: Before swapping: m = 10 , n = 20
m, n = n, m
print("After swapping: m =", m, ", n =", n)   # Output: After swapping: m = 20 , n = 10