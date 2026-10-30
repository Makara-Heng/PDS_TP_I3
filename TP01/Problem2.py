# Problem 2. Time Converter

# a. Compute
total_seconds = 9875
hour = total_seconds // 3600
minute = (total_seconds % 3600) // 60
second = total_seconds % 60

print()
print(f"{total_seconds}s = {hour}h {minute}m {second}s")
print()

# b. Rebuild back the total seconds
check_seconds = (hour * 3600) + (minute * 60) + (second)
print(f"Check: {check_seconds == total_seconds}")
print()

# c. Test code
# 3600 second
total_seconds = 3600
hour = total_seconds // 3600
minute = (total_seconds % 3600) // 60
second = total_seconds % 60

print(f"{total_seconds}s = {hour}h {minute}m {second}s")

# 59 seconds
total_seconds = 59
hour = total_seconds // 3600
minute = (total_seconds % 3600) // 60
second = total_seconds % 60

print(f"{total_seconds}s = {hour}h {minute}m {second}s")

# 86399 seconds
total_seconds = 86399
hour = total_seconds // 3600
minute = (total_seconds % 3600) // 60
second = total_seconds % 60

print(f"{total_seconds}s = {hour}h {minute}m {second}s")
print()