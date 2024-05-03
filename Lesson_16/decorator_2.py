def decorator_function(original_function):
    def wrapper():
        # add some functionality
        return original_function()

    return wrapper


from functools import wraps


def logger(func):
    import logging

    logging.basicConfig(filename=f'{func.__name__}.log', level=logging.INFO)

    @wraps(func)
    def wrapper(*args):
        logging.info(f'Function run with arguments {args}')
        return func(*args)

    return wrapper


def my_time(func):
    import time
    @wraps(func)
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        time.sleep(5)
        end = time.time() - start
        print(f'Duration {end}')
        return result

    return wrapper


@logger
@my_time
def get_info(name: str, age: int) -> str:
    return f'Name is {name}, age is {age}'


if __name__ == '__main__':
    get_info("Nikita", 45)
