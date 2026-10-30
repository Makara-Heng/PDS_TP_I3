# Problem 3. Temperature Converter
def celsius_to_fahrenheit(celsius, round_to = 1):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit, round_to = 1):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# a. Use a for loop to print table
print()
print(f"{"°C":>10} | {"°F"}")
print(f"{"-"*11}+{"-"*11}")
      
for celsius in range(0, 101, 20):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:>7} °C | {fahrenheit:.1f} °F")
print()

# b. Convert Fahrenheit to Celsius
fahrenheit = 98.6
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} °F = {celsius:.1f} °C")
print()

# c. Convert Celsius to Fahrenheit
celsius = 37
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} °C = {fahrenheit:.1f} °F")
print()

# d. Call one function with round_to = 3 (default argument).
def fahrenheit_to_celsius(fahrenheit, round_to = 3):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, round_to)

fahrenheit = 98.7
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} °F = {celsius} °C")
print("Default argument is useful here because we don't need to specify any round_to everytime, automatically use 1 decimal.")
print()