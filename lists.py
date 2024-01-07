# Referecing list items by position
scores = [88, 92, 78, 90, 84]
print(scores[4])

# Looping through a list
scores = [88, 92, 78, 90, 84]
for score in scores:
    print(score)
print("Done!")

# Seeing whether a list contains an item
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
has_Anita = "Anita" in students
has_Bob = "Bob" in students
print(has_Anita)
print(has_Bob)

#or 
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
if "Anita" in students:
    print("Anita")
else:
    print("Anita is not in students list")
if "Bob" in students:
    print("Bob")
else:
    print("Bob is not in students list")
print("Search finished!")

# Getting the lenght of a list
students = ["Mark", "Amber", "Jack", "Sparrow"]
print(len(students))

# Adding an item to the end of a list
students = ["Mark", "Amber", "Todd", "Anita", "Sandy"]
students.append("Jack")
new_students = "Andrew", "Dan" # nu imi dau seama momentan de ce pe acestia doi ii scoate in paranteze...
students.append(new_students)
print(students)

# Test to see if an item is already in a list
cars = ["Golf", "Mazda", "Mercedes", "Opel"]
new_car = "Mazda"
if new_car in cars:
    cars.append("Toyota") 
    print(cars)
    print("Toyota was added to the offer")
print("We updraded the cars offer")

# or
cars = ["Golf", "Mazda", "Mercedes", "Opel"]
new_car = "Mazda"
if new_car in cars:
    new_car = "Pontiac"
    cars.append(new_car)
    print("We added " + new_car + " to the offer")
print("We updraded the cars offer")

# Inserting an item into a list
students = ["Mark", "Oswaldo", "Kimosabe", "Jeanpatitu"]
new_student = "Lupe"
students.insert(2,new_student)
print(students)
#or
students = ["Mark", "Oswaldo", "Kimosabe", "Jeanpatitu"]
students.insert(0,"Adriana")
print(students)

# Changing an item in a list
fruits = ["banana", "apple", "orange"]
fruits[0] = "grapes"
print(fruits)

# Combining lists
list1 = ["Zara", "Lupe", "Hong"]
list2 = ["Huey", "Louie", "Bubba"]
list1.extend(list2)
print(list1)

# Removing list items
""" removing an item var.1"""
letters = ["A", "B", "C", "D", "E"]
letters.remove("C")
print(letters)


""" removing an item var.2"""
letters = ["A", "B", "C", "D", "C", "X", "Y", "C"]
while "C" in letters:
    letters.remove("C")
print(letters)

""" removing an item var.3 - removes position 2, last and first"""
letters = ["A", "B", "C", "Z", "Q", "X", "Y", "P"]
letters.pop(2)
letters.pop()
letters.pop(0)
print(letters)

# copying removed elements
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
third_position_removed = letters.pop(3)
first_removed = letters.pop(0)
last_removed = letters.pop()
print(letters)
print(third_position_removed, first_removed, last_removed)
print(third_position_removed + ", " + first_removed + " and " + last_removed + " were removed from the list")

# Deleting items from a list
letters = ["a", "b", "c"]
del letters[2]
""" to delete the entire list use: del urmata de spatiu si numele listei"""

# Clearing out a list
letters = ["A", "B", "C", "Z", "Q", "X", "Y", "P"]
letters.clear()
print(letters)

# Counting how many times an item appears in a list
grades = ["C", "B", "A", "D", "C", "B", "C"]
b_grades = grades.count("B")
look_for = "C"
c_grades = grades.count(look_for)
print("There are " + str(b_grades) + " B grades in the list.")
print("There are " + str(c_grades) + " " +  look_for + " in the list.")
print("There are " + str(grades.count("F")) + " F grades in the list.")

# Finding an list item's index
""" first example is with an error, for fun"""

"""grades = ["C", "B", "A", "D", "C", "B", "C"]
b_index = grades.index("B")
look_for = "F"
f_index = grades.index(look_for)
print("The first B is at index " + str(grades.index(b_index)))
print("The first " + look_for + " is at " + str(f_index))"""

# for test F grade this should be the way
grades = ["C", "B", "A", "D", "C", "B", "C"]
b_index = grades.index("B")
look_for = "F"
if look_for in grades:
    print(str(look_for)) + " is at index " + str(grades.index(look_for))
else:
    print(str(look_for) + " isn't in the list.")
print("The first B is at index " + str((b_index)))

# Alphabetizing and sorting lists

names = ["Zara", "Lupe", "Hong", "Alberto", "Jake", "Tyler"]
numbers = [14, 0, 56, -4, 99, 56, 11.23]
names.sort()
numbers.sort()
print(names)
print(numbers)

# Dates

import datetime as dt
datelist = []
datelist.append(dt.date(2020,12,31))
datelist.append(dt.date(2019,1,31))
datelist.append(dt.date(2018,2,28))
datelist.append(dt.date(2020,1,1))
datelist.sort()
for date in datelist:
    print(f"{date:%d/%m/%Y}")

# Reverse & sort

import datetime as dt
names = ["Zara", "Lupe", "Hong", "Alberto", "Jake", "Tyler"]
numbers = [14, 0, 56, -4, 99, 56, 11.23]
datelist = []
datelist.append(dt.date(2020,12,31))
datelist.append(dt.date(2019,1,31))
datelist.append(dt.date(2018,2,28))
datelist.append(dt.date(2020,1,1))
names.sort(reverse = True)
print(names)
print() 
numbers.sort(reverse = True)
print(numbers)
print()
datelist.sort(reverse = True)
for date in datelist:
    print(f"{date:%d/%m/%Y}")

# Just reverse
    
names = ["Zara", "Lupe", "Hong", "Alberto", "Jake"]
names.reverse()
print(names)
print()

# Copying a list. Copying a list and reverse the copy

names = ["Zara", "Lupe", "Hong", "Alberto", "Jake"]
backward_names = names.copy()
backward_names.reverse()
print(backward_names)
print()
print(names)

# Tuples. It is a immutable list

""" Getting the length of a tuple"""

prices = (29.95, 9.98, 4.95, 79.98, 2.95)
print(len(prices))
print()

# Count items in tuple

prices = (29.95, 9.98, 4.95, 79.98, 2.95)
print(prices.count(4.95))
print()

# See if an element is in the tuple

prices = (29.95, 9.98, 4.95, 79.98, 2.95)
print(4.95 in prices)
print()

# Get the index of an item from a tuple, with cheking if its exists first

prices = (29.95, 9.98, 4.95, 79.98, 2.95)
look_for = 12345
if look_for in prices:
    position = prices.index(look_for)
else:
    position = -1
print(position)
print()

# or

prices = (29.59, 10.98, 18.95, 70.98, 3)
look_for = 10.98
if look_for in prices:
    position = prices.index(look_for)
else:
    position = -1
print(position)
print()

# curios..

prices = (29.59, 10.98, 18.95, 70.98, 3)

if 3 in prices:
    position = prices.index(3)
else:
    position = -1
print(position)
print()

# Loop the tuple to display the items

prices = (29.59, 10.98, 18.95, 70.98, 3)
for price in prices:
    print(f"${price:.2f}")
print()

# .append(), .clear(), .copy(), .extend(), .insert(), .pop(), .remove(), .reverse(), and .sort() will not work with tuples

