# Функция - это полноправный обьект
# Декоратор - это некая обвертка вокруг другой функции, которая добавляет ей дополниельного поведения
# Декоратор - це функція яка приймає іншу функцію як аргумент, додає їй функціональність та повертає її

# def summ(number_1: int, number_2: int):
#     return number_1 + number_2


def decorator_function(original_function):
    def wrapper():
        # add some functionality
        return original_function()

    return wrapper


def access_to_call(func):
    def wrapper():
        from datetime import datetime
        if datetime.now().hour > 18:
            raise PermissionError("You can call from 9.00 to 18.00")
        return func()

    return wrapper


def logger(func):
    def wrapper(number_1, number_2):  # аргументы от summ()   *args
        print(f'{func.__name__} started')
        result = 2 * func(number_1, number_2)  # *args
        print(f'{func.__name__} finished')
        return result

    return wrapper


def type_int(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError(f"{arg} should be integer, now {type(arg)}")
        return func(*args)

    return wrapper


@type_int
@logger
def summ(number_1: int, number_2: int):
    return number_1 + number_2


@access_to_call
def phone_call():
    return 'Calling .....'


if __name__ == '__main__':
    function = logger(summ)
    print(function)  # <function logger.<locals>.wrapper at 0x00000228137CA280>
    print(function(2, 3))

    print(logger(summ)(2, 3))
    test = logger(summ)
    print(test(2, 3))

    print(summ(2, 3))
    print(phone_call())
