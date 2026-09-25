# Will Allen
# Testing Python fundamentals

# -------------------------
# INPUT
# -------------------------

our_name = input("What is your name? ")
print("Hello there, ", our_name, "!")

# Combining Strings via f-strings
# f before quotes, variables in curly brackets
age = 21
print(f"Next year you will be {age + 1}!")

# useful functions
# .strip() = remove leading and trailing blanks
# .upper() / .lower() = change case
# .replace('p','f') = swap out characters
nameCount = len(our_name.strip())
print(f"Your name has {nameCount} letters!")

# -------------------------
# VARIABLES
# -------------------------


# dynamically typed, we can change types
status = 0
status = "Online"

# use type() to check type
print(type(status))

# arithmetic examples
a = 5
b = 1.5
c = 5 % 2 # even or odd? - modulo gives us the remainder from division

print(type(a+b))
# int + float = float

score = float(input("What is your favorite number?: "))
print(f"What? Don't like {int(score+1)}?")

# -------------------------
# LISTS
# -------------------------

# A list stores multiple values
favorite_foods = ["pizza", "tacos", "burgers"]

print("\nYour favorite foods are:")
for food in favorite_foods:
    print(food)

# Add another item to the list
new_food = input("Add another favorite food: ")
favorite_foods.append(new_food)

print("Updated food list:", favorite_foods)

# -------------------------
# CONDITIONS
# -------------------------

# Conditions allow the program to make decisions
if age >= 21:
    print("Old enough to enter.")
else:
    print("Not old enough to enter!")


if score >= 5:
    print("Your number is 5 or higher.")
else:
    print("Your number is less than 5.")


# -------------------------
# LOOPS
# -------------------------

# A for loop repeats code for each item in a list
print("\nFavorite foods:")
for food in favorite_foods:
    print(f"- {food}")

# A while loop repeats while a condition is true
number = 1

print("\nCounting:")
while number <= 5:
    print(number)
    number += 1


# -------------------------
# FUNCTIONS
# -------------------------

# A function is a reusable block of code
def greet(name):
    print(f"Welcome, {name}!")


def check_score(score):
    if score % 2 == 0:
        return "That's an even number!"
    else:
        return "That's an odd number!"


# Calling the functions
greet(our_name)

message = check_score(score)
print(message)

