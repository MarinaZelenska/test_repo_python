number = int(input('Enter number :'))


def is_prime(number: int):
    if number not in range(2, 1001):
        raise ValueError(f"{number} is not a valid number. Please, try any number in range from 2 to 1000.")

    for i in range(2, number + 1):
        if number % i == 0 and i != number:
            return False
    return True


result = is_prime(number)
