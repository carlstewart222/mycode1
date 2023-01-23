#!/usr/bin/env python3
""" Stewarts Consulting | Carl S
   print() - concatenate vs print a series of items"""

def main():

    # collect string input from the user
    user_input = input("Please enter an IPv4 IP address:")
    
    # Asking for the name of the vendor
    vendor = input("Please enter the name of the vendor of your PC: ")

    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    print("You told me the IPv4 address is:", user_input)

    # Printing the name of the manufacturer
    print ("The PC manufacturer is:", vendor)

main()

