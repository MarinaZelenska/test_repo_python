# Closure - Замыкания
# Замыкание - это внутренняя функция, которая возвращается из внешней функции и имеет доступ к переменным из внешнего скоупа
# Замыкание - потому что захват переменной
# Замыкания хранят разные состояния
# Замыкания полезны для борьбы с глобализмом
# Замыкание - это полноценный обьект у которого есь данные и есть метод для работы с этими данными (данные инкапсулированы + метод который мы прописали и указываем как с ним работать)
# Хранит состояние и предоставляет инструмент для работы с ними, скрывает данные и помогает избегать global

def names():
    all_names = []

    def inner(name: str) -> list:  # У функции inner() есть ссылка на переменную all_names - захват
        all_names.append(name)
        return all_names

    return inner


def average():
    values = []

    def inner(*args) -> float:
        for el in args:
            values.append(el)
        return sum(values) / len(values)

    return inner


def counter():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner


def pow_(base):

    def inner(value: int) -> int:
        return value ** base

    return inner

def pow_test(base):
    return lambda value: value ** base


if __name__ == '__main__':
    students = names()
    # print(students('Maryna'))  # ['Maryna']
    # print(students.__closure__[0].cell_contents)
    # print(students('Nastya'))  # ['Maryna', 'Nastya']
    # print(students('Oleg'))    # ['Maryna', 'Nastya', 'Oleg']
    ###################
    # boys = names()
    # girls = names()
    # boys("Oleg")
    # print(boys("Nikita"))  # ['Oleg', 'Nikita']
    # girls("Olga")
    # print(girls("Maryna"))  # ['Olga', 'Maryna'] замыкания хранят разные состояния
    #########################
    # test_av = average()
    # print(test_av(3, 10, 28, 56))
    # #####
    # test_count = counter()
    # print(test_count(5))
    # print(test_count(7))
    #####
    #
    # test = pow_(3)
    # print(test(2))

    # ets = pow_test(2)
    # print(ets(3))



