# 1 - Example with divide
# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
#
# result = first_number // second_number
#
# print(f'Divide result {result}')  # ZeroDivisionError: integer division or modulo by zero

# 2 - Write block try except

# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
#
# try:
#     result = first_number // second_number
# except ZeroDivisionError:
#     result = 'Division by zero prohibited'
#
# print(f'Divide result {result}')

# 3 - Exception with datatype

# first_number = int(input("Enter first number: "))
# second_number = input("Enter second number: ")
#
# try:
#     result = first_number // second_number
# except (ZeroDivisionError, TypeError):
#     result = 'Division by zero prohibited'
#
# print(f'Divide result {result}')  # TypeError


# first_number = int(input("Enter first number: "))
# second_number = input("Enter second number: ")
#
# try:
#     result = first_number // second_number
# except ZeroDivisionError:
#     result = 'Division by zero prohibited'
# except TypeError:
#     result = 'Invalid datatype'
#
# print(f'Divide result  - {result}')  # TypeError


# 4 - raise

# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
#
# if not isinstance(first_number, int) or not isinstance(second_number, int):
#     raise ValueError("All variables should be integers")
# elif second_number == 0:
#     raise ValueError("Divide by 0!")
# else:
#     result = first_number // second_number
#     print(result)

# 5 - finally

# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
#
# try:
#     result = first_number // second_number
# except ZeroDivisionError:
#     result = 'Division by zero prohibited'
# except TypeError:
#     result = 'Invalid datatype'
# finally:
#     print("Finish")
#
# print(f'Divide result  - {result}')


# 6 - else block

# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Devision by zero")
# else:
#     print("Else when no exception")
#     print(f"Result of division: {result}")

# 8 - assert
# Using the assert statement in Python allows you to check whether the state of the program satisfies certain conditions,
# and raise an AssertionError exception if these conditions are not met.

# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))
#
# assert second_number != 0, 'Division by zero'




