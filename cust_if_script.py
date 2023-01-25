#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'You got a '

# wrap connection in a float() to accept decimals as numbers
grade = float(input("What is the final score on your test?"))

# if input value was higher or equal to 25
if grade >= 90:
    message = message + 'A.'
elif grade >= 80:
    message = message + 'B.'
elif grade >= 70:
    message = message + 'C.'
elif grade >= 60:
    message = message + 'D.'
else:
    message = message + 'F.'
print(message)

