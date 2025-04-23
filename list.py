#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HADI
#
# Created:     20/04/2025
# Copyright:   (c) HADI 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

my_list = [7, 2, 2, 5, 2]
print(my_list)
my_list = [7, 2, 2, 5, 2]
print(my_list)
my_list[1] = 3
print(my_list)
my_list = [7, 2, 2, 5, 2]
print(len(my_list))
numbers = []
numbers.append(5)
numbers.append(10)
numbers.append(3)
print(numbers)
numbers = [1, 2, 3, 4, 5, 6]
numbers.insert(0, 10)
print(numbers)
numbers.insert(2, 20)
print(numbers)
my_list = [1, 2, 3, 4, 5, 6]

my_list.pop(2)
print(my_list)
my_list.pop(3)
print(my_list)
my_list.sort()
print(my_list)
my_list = [5, 2, 3, 1, 4]

greatest = max((my_list))
smallest = min((my_list))
list_sum = sum((my_list))

print("Smallest:", smallest)
print("Greatest:", greatest)
print("Sum:", list_sum)
