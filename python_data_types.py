# Strings
simplequote_string = 'This is a string with single quotes.'
doublequote_string = "This is a string with double quotes."
triplequote_string = '''This is a string with triple single quotes.'''
tripledoublequote_string = """This is a string with triple double quotes."""

print(simplequote_string)
print(doublequote_string)
print(triplequote_string)
print(tripledoublequote_string)

# Numbers
integer = 10
floating_point = 3.14
complex_number = 5 + 2j # This is an imaginary number

print(integer)
print(floating_point)
print(complex_number)

# Lists
# Is a collection which is ordered and mutable. Allows duplicate members.
numbers = [1, 2, 3, 4, 5, 5]
print(numbers)

# Tuples
# Is a collection which is ordered and immutable. Also allows duplicate members.
tuple = ('a', 'b', 'c', 'a')
print(tuple)

# Dictionaries
# Is a collection which is unordered, mutable and indexed. No duplicate members.
dictionary = {'name': 'Juan', 'age': 30, 'city': 'New York'}
print(dictionary)

print(dictionary['name'])  # Accessing value by key
print(dictionary.get('city'))  # Another way to access value by key

# Sets
# Is a collection which is unordered, unindexed and mutable. No duplicate members.
set = {1, 1, 2, 2, 5, 3, 4}
print(set) # Duplicates will be removed
# print(set[1])  # This will raise an error since sets are unindexed TypeError: 'set' object is not subscriptable

# Booleans
is_true = True
is_false = False
print(is_true)
print(is_false)
