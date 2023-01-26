#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'You got a '

# wrap connection in a float() to accept decimals as numbers
grade = float(input("What is the final score on your test?"))

# if input value was higher or equal to 25
match grade:
    case grade if 90 <= grade:
        message = message + 'A.'
    case grade if  80 <= grade:
        message = message + 'B.'
    case grade if => 70:
        message = message + 'C.'
    case grade if  => 60:
        message = message + 'D.'
    case _:
        messase = message + 'F.'
print(message)

