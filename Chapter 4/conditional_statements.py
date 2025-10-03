"""
if condition:
    perform some task
elif another_condition:
    perform some task
elif another_condition:
    perform some task
else:
    run some task if all conditions were false
"""

score = int(input("Enter a score: "))

if score >= 90:
    print("Your grade is A")
elif score >= 80:
    print("Your grade is B")
elif score >=70:
    print("Your grade is C")
else:
    print("You did not get an A or B or C")