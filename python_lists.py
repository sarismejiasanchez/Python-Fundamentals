# The lists are ordered, changeable, and allow duplicate values.

from calendar import c


fruits = ["Apple", "Orange", "Tangerine", "Grapes"]
print(fruits) # output: ['Apple', 'Orange', 'Tangerine', 'Grapes']
print(type(fruits)) # output: <class 'list'>


# The firts element of the list is at index 0, the second element is at index 1, and so on.
print("\nAccessing elements of the list by index:")
print(fruits[0]) # output: Apple
print(fruits[1]) # output: Orange
print(fruits[2]) # output: Tangerine
print(fruits[3]) # output: Grapes

print("\nChanging the value of an element in the list:")
fruits[1] = "Banana"
print(fruits[1]) # output: Banana
print(fruits) # output: ['Apple', 'Banana', 'Tangerine', 'Grapes']

print("\nAdding a duplicate value to the list:")
fruits.append("Apple")
print(fruits) # output: ['Apple', 'Banana', 'Tangerine', 'Grapes', 'Apple']

print("\nCreating a list with different data types:")
mixed_list = ["Apple", 5, True, 3.14]
print(mixed_list) # output: ['Apple', 5, True, 3.14]
print(type(mixed_list)) # output: <class 'list'>

print("\nFinding the length of the list:")
print(len(fruits)) # output: 5
print(len(mixed_list)) # output: 4

print("\nSlicing the list:")
print(fruits) # output: ['Apple', 'Banana', 'Tangerine', 'Grapes', 'Apple']
print(fruits[0:3]) # output: ['Apple', 'Banana', 'Tangerine']
print(fruits[:3]) # output: ['Apple', 'Banana', 'Tangerine']
print(fruits[2:4]) # output: ['Tangerine', 'Grapes']
print(fruits[-1:]) # output: ['Apple']
print(fruits[-2:]) # output: ['Grapes', 'Apple']

print("\nChecking if an element is in the list:")
print(f"Banana is in the fruits list: {'Banana' in fruits}") # output: True
print(f"Mango is in the fruits list: {'Mango' in fruits}") # output: False

if "Mango" in fruits:
    print("Mango is in the fruits list.")
elif "Banana" in fruits:
    print("Banana is in the fruits list.")


print("\nMethods to manipulate the list:")

vehicles = ["Car", "Bike", "Bus", "Truck"]
print(vehicles) # output: ['Car', 'Bike', 'Bus', 'Truck']

print("\nAppend method:")
# Adding an element to the end of the list
vehicles.append("Motorcycle")
print(vehicles) # output: ['Car', 'Bike', 'Bus', 'Truck', 'Motorcycle']

print("\nInsert method:")
# Adding an element at a specific index
vehicles.insert(1, "Scooter")
print(vehicles) # output: ['Car', 'Scooter', 'Bike', 'Bus', 'Truck', 'Motorcycle']

print("\nRemove method:")
# Removing an element by value
vehicles.remove("Bus")
print(vehicles) # output: ['Car', 'Scooter', 'Bike', 'Truck', 'Motorcycle']

print("\nPop method:")
vehicles.pop() # Removing the last element
print(vehicles) # output: ['Car', 'Scooter', 'Bike', 'Truck']

vehicles.pop(1) # Removing the element at index 1
print(vehicles) # output: ['Car', 'Bike', 'Truck']

print("\nSort method:")
vehicles.sort() # Sorting the list in ascending order
print(vehicles) # output: ['Bike', 'Car', 'Truck']

vehicles.sort(reverse=True) # Sorting the list in descending order
print(vehicles) # output: ['Truck', 'Car', 'Bike']

vehicles.reverse() # Reversing the order of the list
print(vehicles) # output: ['Bike', 'Car', 'Truck']

print("\nClear method:")
vehicles.clear() # Removing all elements from the list
print(vehicles) # output: []

print("\nUnion of two lists:")
collection1 = [1, 2, 3]
collection2 = [4, 5, 6]
final_collection = collection1 + collection2
print(final_collection) # output: [1, 2, 3, 4, 5, 6]

print("\nUsing extend method to combine two lists:")
collection1.extend(collection2) # Adding elements of collection2 to collection1
print(collection1) # output: [1, 2, 3, 4, 5, 6]