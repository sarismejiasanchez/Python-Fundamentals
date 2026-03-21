# The while loop in Python is used to execute a block of code repeatedly as long as a certain condition is true. The syntax for a while loop is:
i = 1

while i <= 10:
    print(i)
    i += 1

print("Using while loop with a increment variable before the print statement:")
# This will print numbers from 2 to 11, because the increment happens before the print statement. 
# When i becomes 10, it will be incremented to 11 before being printed, and then the loop will terminate since the condition i <= 10 is no longer true.
i = 1
while i <= 10:
    i += 1
    print(i) 

# Break statement is used to exit the loop prematurely when a certain condition is met. The syntax for the break statement is:
print("Using break statement:")
i = 1
while i <= 10:
    # When i is equal to 5, the break statement will be executed, and the loop will terminate immediately.
    if i == 5:
        break
    print(i) # This will print numbers from 1 to 4, and when i becomes 5, the loop will exit due to the break statement.
    i += 1

print("Using break statement with a condition after the print statement:")
i = 1
while i <= 10:
    print(i) # This will print numbers from 1 to 5, and when i becomes 5, the loop will exit after printing 5 due to the break statement.
    if i == 5:
        break
    i += 1

print("Using continue statement:")
# The continue statement is used to skip the current iteration of the loop and move on to the next iteration. 
# The syntax for the continue statement is:

# This will print numbers from 1 to 10, but it will skip printing 5 because when i is equal to 5, 
# the continue statement will be executed, and the loop will move on to the next iteration 
# without executing the print statement for that iteration.

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
else:
    print(f"{i} is no longer less than 10")