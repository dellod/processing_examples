# Session3 - Lists, Operators, and Conditions: Example 8 - Difference in if statements
# SCRP
# Daryl Dang

"""
What is the difference between method 1 and 2?
"""
percentage_grade = 85

# Method 1
if percentage_grade >= 95:
    print("You get an A+")
if percentage_grade >= 85:
    print("You get an A")
if percentage_grade >= 80:
    print("You get a B+")
if percentage_grade >= 75:
    print("You get a B")
if percentage_grade < 75:
    print("You get a grade less than B")

# Method 2
if percentage_grade >= 95:
    print("You get an A+")
elif percentage_grade >= 85:
    print("You get an A")
elif percentage_grade >= 80:
    print("You get a B+")
elif percentage_grade >= 75:
    print("You get a B")
else:
    print("You get a grade less than B")
