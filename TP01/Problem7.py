# Problem 7. Digit Tools
def digit_sum(n):
    """Add up digits with whole number"""
    n = abs(n)
    total = 0
    while n > 0:
        digit = n % 10  # last digit
        total += digit  # total = total + digit
        n //= 10        # n = n // 10 (remove last digit)
    return total

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

def is_palindrome(n):
    return n == reverse_number(n)

# a. Test the three function
print()
numbers = [2026, 12321, 9875]

for n in numbers:
    print(f"{n}: Digit Sum = {digit_sum(n)}, "
          f"Reversed = {reverse_number(n)}, "
          f"Palindrome = {is_palindrome(n)}")
print()

# b. Count palindrome from 10 to 999
count = 0
for n in range(10, 1000):
    if is_palindrome(n):
        count += 1

print(f"Palindrome from 10 to 999: {count}")
print()