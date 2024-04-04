# First example for loop while
# counter = 0
#
# while counter < 5:
#     print(f'Counter value = {counter}')
#     counter += 1


# Task 1 Enter all values from list that device on entered number

# numbers = [1, 5, 10, 16, 100, 200, 67, 56, 4, 8]
# number = int(input("Enter number for divide: "))
# expected_result = list()
# i = 0
#
# while len(numbers) > i:
#     if numbers[i] % number == 0:
#         expected_result.append(numbers[i])
#     i += 1
#
# print(f'All this {expected_result} numbers divide by {number}')


# Second decision

# numbers = [1, 5, 10, 16, 100, 200, 67, 56, 4, 8]
# number = int(input("Enter number for divide: "))
# expected_result = list()
#
#
# while numbers:
#     if numbers[0] % number == 0:
#         expected_result.append(numbers[0])
#     numbers.remove(numbers[0])
#
#
# print(f'All this {expected_result} numbers divide by {number}')


# Task 2. Write a program to find the first non-sequential number in a list
# First decision
# numbers = [1, 5, 10, 16, 100, 200, 67, 56, 4, 8]
# numbers = [1, 2, 3, 4]
# idx = 0

# while len(numbers) > idx:
#     if numbers[idx] + 1 != numbers[idx + 1]:
#         print(f'{numbers[idx + 1]} is the first non-sequential number in a {numbers} list')
#         break
#     idx += 1
# else:
#     print(f'{numbers} list is sequential')  # IndexError: list index out of range

# Second decision
# while len(numbers) - 1 > idx:
#     if numbers[idx] + 1 != numbers[idx + 1]:
#         print(f'{numbers[idx + 1]} is the first non-sequential number in a {numbers} list')
#         break
#     idx += 1
# else:
#     print(f'{numbers} list is sequential')


#Task 3
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# number = int(input("Enter number: "))
# hight = 1
#
# while hight <= number:
#     width = 1
#     while width <= hight:
#         print(width, end=' ')
#         width += 1
#     print()
#     hight += 1
