#-------------------------------------------------------------------------------
# Name:        module8
# Purpose:
#
# Author:      HADI
#
# Created:     07/04/2025
# Copyright:   (c) HADI 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

first = input("enter")
operator = input("enter op (+,-,*,/,%)")
sec = input("enter no")
first = int(first)
sec = int(sec)

 if operator ==  "+" :
    print(first + sec)
 elif operator == "-" :
     print(first - sec)
 elif operator == "*" :
     print(first * sec)
 elif operator == "/" :
     print(first / sec)
 elif operator ==" %" :
     print(first % sec)
 else:
     print("invalid")
