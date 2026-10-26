print("C.")
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