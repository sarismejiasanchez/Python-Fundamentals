# This code demonstrates the use of if-elif-else statements in Python to evaluate conditions 
# and execute different blocks of code based on those conditions.

x = 8
y = 12
z = 6

if x > y or x > z:
    print(f"{x} is greater than {y} or {x} is greater than {z}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print("None of the above conditions are true")

a = "Python"
b = "JavaScript"
c = "Python"

if a == b:
    print(f"{a} is equal to {b}")
elif a == c:
    if a == b:
        print(f"{a} is equal to {c} but not equal to {b}")
    else:
        print("I'm exiting through the else of the inner if")
else:
    print(f"{a} is not equal to {b}")


e = 10
f = 10

if e == f:
    pass  # This is a placeholder for future code, it does nothing

number = input("Enter a number to find out if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")