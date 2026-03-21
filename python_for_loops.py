# Using a for loop to iterate through each letter in the word "Python" and print it out.
print("Using a for loop to iterate through each letter in a word:")

word = "Python"

for letter in word:
    print(letter)

print("\nUsing a for loop to iterate through a list of fruits:")

fruits = ["Apple", "Orange", "Kiwi"]

for fruit in fruits:
    print(fruit)

print("\nBreaking out of a for loop when a certain condition is met:")
for fruit in fruits:
    if fruit == "Orange":
        break
    print(fruit) # This will print "Apple" and then break out of the loop when it encounters "Orange".

print("\nUsing continue statement in a for loop:")
for fruit in fruits:
    if fruit == "Orange":
        continue
    print(fruit) # This will print "Apple" and "Kiwi", but it will skip printing "Orange" because of the continue statement.

print("\nUsing else statement with a for loop:")
for fruit in fruits:
    print(fruit)
else:
    print("The for loop has finished iterating through all the fruits.") # This will execute after the for loop has finished iterating through all the fruits.

print("\nUsing range() function in a for loop:")
# The range() function is used to generate a sequence of numbers.
# Starting from 0 by default, and increments by 1 (by default), and ends at a specified number without including it.

for i in range(10):
    print(i)

print("\nUsing range() function with a start and end value:")
for i in range(3, 5):
    print(i) # This will print numbers from 3 to 4, because the range starts at 3 and ends at 5 (exclusive).

print("\nUsing range() function with a step value:")
for i in range(0, 10, 2):
    print(i) # This will print even numbers from 0 to 8, because the range starts at 0, ends at 10 (exclusive), and increments by 2 (the step value).

print("\nUsing nested for loops:")

fruits = ["Apple", "Orange", "Kiwi"]
adjectives = ["Tasty", "Healthy"]

for adjective in adjectives:
    for fruit in fruits:
        print(f"{fruit} is {adjective}") # This will print a combination of each fruit with each adjective, resulting in 6 lines of output.

print("\nUsing nested for loops with the order of iteration changed:")
for fruit in fruits:
    for adjective in adjectives:
        print(f"{fruit} is {adjective}") # The outer loop iterates through fruits first, and the inner loop iterates through adjectives for each fruit.

print("\nUsing pass statement in a for loop:")

for i in range(10):
    pass