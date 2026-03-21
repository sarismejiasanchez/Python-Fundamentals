import random
day = random.randint(1, 8) # Generate a random integer between 1 and 8 to test the match statement, 8 is included to test the default case

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
        

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
test_days = days + ["Funday"] # Add an invalid option to test the default case
day = random.choice(test_days) # Generate a random day (or invalid value) to test the match statement
#day = "Funday"
print(f"Randomly selected day: {day}")
match day:
    case _ if day in days:
        day_number = days.index(day) + 1
        print(f"{day} is the day number {day_number} of the week")
    case _:
        print("Invalid day")