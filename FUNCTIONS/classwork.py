def check_user_operation(operation: str) -> str:
    correct_symbols = ['+', '-', '*', '/']
    if operation not in correct_symbols:
        raise ValueError(f'Invalid operation, you should enter on of this operation {correct_symbols}')
    return operation


def validate_datatype(variable, expected_type):
    if isinstance(variable, expected_type):
        return variable
    else:
        raise ValueError(f'Expected datatype for variable {variable} is {expected_type}.'
                         f'\n Actual is {type(variable)}'
                         f'\nTry again')


def add_num(num_1: int, num_2: int) -> int:
    return num_1 + num_2


def minus_num(num_1: int, num_2: int) -> int:
    return num_1 - num_2


def multiply_num(num_1: int, num_2: int) -> int:
    return num_1 * num_2


def divide_num(num_1: int, num_2: int):
    if num_2 != 0:
        return num_1 / num_2
    else:
        raise ValueError("Division by zero prohibited")


def calculate_numbers(num_1, num_2, operation):
    if operation == '+':
        result = add_num(num_1, num_2)
    elif operation == '-':
        result = minus_num(num_1, num_2)
    elif operation == '*':
        result = multiply_num(num_1, num_2)
    elif operation == '/':
        result = divide_num(num_1, num_2)

    else:
        raise ValueError("Incorrect operation")
    return result


def run_calculator(number_1, number_2, operation):
    operation = check_user_operation(operation)
    number_1 = validate_datatype(number_1, int)
    number_2 = validate_datatype(number_2, int)
    run_result = calculate_numbers(number_1, number_2, operation)
    return run_result


# Run program

user_operation = input("Please, choose and enter one of the following symbols (+, -, *, /): ")
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

result = run_calculator(number_1, number_2, user_operation)
print(f'You result is {result}')
