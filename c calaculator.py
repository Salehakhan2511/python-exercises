#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HADI
#
# Created:     08/04/2025
# Copyright:   (c) HADI 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

first = input("Enter first number: ")
operator = input("Enter operator (+, -, *, /, %): ")
sec = input("Enter second number: ")

first = int(first)
sec = int(sec)

if operator == "+":
    print(first + sec)
elif operator == "-":
    print(first - sec)
elif operator == "*":
    print(first * sec)
elif operator == "/":
    if sec != 0:  # Handle division by zero
        print(first / sec)
    else:
        print("Cannot divide by zero")
elif operator == "%":
    print(first % sec)
else:
    print("Invalid operator")


