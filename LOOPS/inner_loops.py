# TASK 1
# *****
# *****
# *****
# *****
# hight, width = 4, 5  # hight and  width rectangle
# for i in range(hight):
#     for j in range(width):
#         print('*', end='')
#     print()  # New line

# Task 2
#    *
#   ***
#  *****
# *******
# height = int(input("Enter height of triangle: "))
# for i in range(1, height + 1):
# second decision
# print(' ' * (height - i), '* ' * i)
# first decision
# print(' ' * height, '* ' * i)
# height = height - 1


# Task 3
#    *
# *
# * * *
# * * * *
#
# for i in range(1, 5):
#     print('* ' * i, end='')
#     print()


# Task 4
# Write a program that reads a list of numbers and prints all the even elements of this list.
# first decision
# numbers = [1, 10, 5, 7, 8, 9, 11, 22, 25, 27, 100, 2, 5, 6, 4]
# even_numbers = list()
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
# print(even_numbers)
# second
# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)


# Task 5
# Given a list of numbers. Write a program that prints the elements of a list that appear only once in the list.
# numbers = [1, 10, 5, 7, 8, 9, 11, 22, 25, 27, 100, 2, 5, 6, 4, 11]
# unique_numbers = list()
# for number in numbers:
#     if number not in unique_numbers:
#         unique_numbers.append(number)
# print(unique_numbers)

# for number in numbers:
#     if number in unique_numbers:
#         continue
#     else:
#         unique_numbers.append(number)
# print(unique_numbers)


# Task 6 Write a program that check is elements in list unique or not
# numbers = [1, 10, 5, 7, 8, 9, 11, 22, 25, 27, 100, 2, 5, 6, 4, 11]
# for number in numbers:
#     if numbers.count(number) > 1:
#         print(f'{numbers}- list contain not unique elements, {number} number is repeated')
#         break

# Task 7 check vowels
# data = input("Enter your string: ").lower()
# vowels = "aeiou"
# count = 0
#
# for element in data:
#     if element in vowels:
#         count += 1
#
# print(f"Count of vowels letters: {count}")
#
# my_list = [1, 10, 2, 3, 4, 6, 7, 8]
# for i in range(1, len(my_list)):
#     if my_list[i] != my_list[i-1] + 1:
#         print("Non-consecutive number in the list: ", my_list[i])
#         break
# else:
#     print("The list contains consecutive numbers!")
#

# unsorted_list = [1, 5, 68, 0]
# for num in range(1, len(unsorted_list)):
#     if unsorted_list[num] != unsorted_list[num - 1] + 1:
#         print(f" First inconsistent number in list {unsorted_list} is {unsorted_list[num]}")
#         break
# else:
#     print("The list contains consecutive numbers!")

# for i in range(1,6):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()


# height = int(input('Height of the pyramid: '))
#
# for i in range(1, height + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

