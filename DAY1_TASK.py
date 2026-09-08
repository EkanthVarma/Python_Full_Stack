# Student Marks Manager

marks = []

for mark in range(3):
    mark = int(input("Enter mark: "))
    marks.append(mark)

marks.insert(0, 90)

marks.extend([75, 85])

if 75 in marks:
    marks.remove(75)

removed_mark = marks.pop()
print(f'Removed final mark is {removed_mark}')

print(f'Final marks is {marks}')
print(f'Number of marks is {len(marks)}')


# Number List Analyser

numbers = [20, 10, 30, 20, 40, 20]

numbers.sort()

numbers.reverse()

search = int(input("\nEnter a number to search: "))

if search in numbers:
    print("found")
    print("Count:", numbers.count(search))
    print("First index:", numbers.index(search))
else:
    print("not found.")

print(f'Smallest value is {min(numbers)}')
print(f'Largest value is {max(numbers)}')
print(f'Sum is {sum(numbers)}')


# Even and Odd Number Separator

numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for i in numbers:
    if i % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(f'even numbers is {even}')
print(f'Odd numbers is {odd}')

print(f'first three values are {numbers[:3]}')
print(f'last three values are {numbers[-3:]}')

backup = numbers.copy()

numbers.clear()

print(f'list after clear() is {numbers}')
print(f'backup list is {backup}')


# Unique Name Manager

names = ["Asha", "Rahul", "Asha", "John", "Rahul"]

unique_names = set(names)

print("\nUnique names:", unique_names)

unique_names.add("Meera")

unique_names.update(["Arun", "Priya"])

if "John" in unique_names:
    unique_names.remove("John")
    print("John was removed.")

unique_names.discard("David")

print("\nFinal unique names:")

for name in unique_names:
    print(name)


