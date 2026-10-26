# Problem 1. Student Profile Card

# a. Print the profile card
name = "Ben10"
age = 18
major = "Applied Mathematics and Statistics"
gpa = 3.50
is_scholar = True
print()
print("================================")
print(f"Name      : {name}")
print(f"Age       : {age}")
print(f"Major     : {major}")
print(f"GPA       : {gpa:.2f}")
print(f"Scholar   : {is_scholar}")
print("================================")
print()

# b. Print value type
print(f"'{name}' -> {type(name).__name__}")
print(f"{age} -> {type(age).__name__}")
print(f"'{major}' -> {type(major).__name__}")
print(f"{gpa} -> {type(gpa).__name__}")
print(f"{is_scholar} -> {type(is_scholar).__name__}")
print()

# Other way to display b
for value in (name, age, major, gpa, is_scholar):
    print(repr(value), "->", type(value).__name__)
print()

# c. Reassign age
age = 20
print(f"'{age}' -> {type(age).__name__}")
print()