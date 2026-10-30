# Problem 6. Leap Years and Days in a Month

# a. Write the function is_leap(year)
def is_leap(year):
    """leap year must divided by 4 and not 100, but if divided by 400 then it's leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# b. Write the function days_in_month
def days_in_month(month, year):
    """Return the number of day in the month (1-12), or None if Invalid."""
    if month < 1 or month > 12:
        return None
    elif month == 2:
        return 29 if is_leap(year) else 28
        """ if is_leap(year):
                return 29
            else:
                return 28"""
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31

# c. Check whether the given years are leap years
print()
for year in (1900, 2000, 2024, 2026):
    if is_leap(year):
        print(year, "leap")
    else:
        print(year, "not leap")
print()

# Additional from the output
print("Feb 2024:", days_in_month(2, 2024),
      "| Feb 2026:", days_in_month(2, 2026),
      "| Apr 2026:", days_in_month(4, 2026),
      "| Month 13:", days_in_month(13, 2026))
print()

# d. Count leap years from 2000 to 2100
count = 0
for year in range(2000, 2101):
    if is_leap(year):
        count += 1

print("Leap years from 2000 to 2100:", count)
print()