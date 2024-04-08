def add_number(number_1: int, number_2: int) -> int:
    return number_1 + number_2


def substract_number(number_1: int, number_2: int) -> int:
    return number_1 - number_2


def multiply_number(number_1: int, number_2: int) -> int:
    return number_1 * number_2


def divide_number(number_1: int, number_2: int) -> float:
    if number_2 == 0:
        raise ZeroDivisionError("You can't division by 0")
    return number_1 / number_2


def calculator(number_1: int, number_2: int, action: str):
    if action == "+":
        result = add_number(number_1, number_2)
    elif action == "-":
        result = substract_number(number_1, number_2)
    elif action == "*":
        result = multiply_number(number_1, number_2)
    elif action == "/":
        result = divide_number(number_1, number_2)
    else:
        raise NotImplemented('This operation is not implemented for calculator')
    return result


number_1 = int(input('Enter first number :'))
action = input('Enter action (you can use: +,-,/,* ) ')
number_2 = int(input('Enter second number : '))

result = calculator(number_1, number_2, action)

print(f'Result for operation {action} for numbers {number_1, number_2} is {result}')
