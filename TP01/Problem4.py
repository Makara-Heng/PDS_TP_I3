# Problem 4. Type-Conversion Detective

# Part A. Predict result and Python's answer
print()
print(int("7") + 3.5)
print(str(10) * 3)
print(bool(""), bool(" "))
print(int(3.99))
print(float(1e3))
print(int(True) + float("2.5"))
print(round(2.5), round(3.5))
print(type(10/2))
print()

# Part B. Write function safe_int(text)
import math
def safe_int(text):
    try:
        return math.floor(float(text))
    except ValueError:
        return None

for text in ["58", "-2", "4.7", "Ben10", ""]:
    print(repr(text), "->", safe_int(text))
print()

# Part C. Ask user to input and convert
def safe_int(text):
    try:
        return int(text.strip())
    except ValueError:
        return None

num1 = input("Enter one number: ")
num2 = input("Enter another number: ")

n1 = safe_int(num1)
n2 = safe_int(num2)

if n1 is not None and n2 is not None:
    print(f"Sum: {n1} + {n2} = {n1 + n2}")
else:
    print("You must enter a whole number.")
print()