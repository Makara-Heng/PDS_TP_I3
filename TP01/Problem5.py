# Problem 5. Letter Grade

# a. Test the grade function with list of score
def letter_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 97:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print()
"""Use repr to print the whole thing"""
for score in [99, 90, 85.5, 72, 60, 59.9, -5, 101]:
    print(f"{repr(score):>10} -> {letter_grade(score)}")
print()

# b. The reason A+ must be before A
def letter_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "A"
    elif score >= 97:
        return "A+"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

for score in [99, 90, 85.5, 72, 60, 59.9, -5, 101]:
    print(f"{repr(score):>10} -> {letter_grade(score)}")

print("A+ must be before A because python check the condition from top to bottom so if we put A first then the point that should be A+ will just be A.")
print()