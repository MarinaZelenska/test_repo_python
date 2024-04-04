# 1 - Create dictionary
from timeit import timeit

# my_dict = {}  # <class 'dict'>
# my_dict_1 = dict()  # <class 'dict'>
# print(type(my_dict))
# print(type(my_dict_1))
# print(dict.mro())  # [<class 'dict'>, <class 'object'>]


# 2 - Memory
# print(timeit('{}'))
# print(timeit('dict()'))


# 3 - For what we use dictionary
# case with list
# prices = [['orange', 50],
#           ['apple', 30],
#           ['banana', 40]]
#
# for element in prices:
#     if element[0] == 'banana':
#         print(f'Price is {element[1]}')
# case with dictionary
# prices_dict = {'orange': 50, 'apple': 30, 'banana': 40}
# print(f"Price is {prices_dict['orange']}")
# print(f"Price is {prices_dict.get('apple')}")


# 4- key should be unique

# fruits = {'orange': 30, 'apple': 10, 'orange': 15}
# print(fruits)  # last key rewrite first value


# 5 - .formkeys
# names = dict.fromkeys(['Anna', 'Olga', 'Nastya', 'Olga'])
# names = dict.fromkeys(['Anna', 'Olga', 'Nastya', 'Olga'], [10, 11, 23, 67])
# print(names)

# 6 Add element to dictionary
# pearson = {
#     "name": "Maryna",
#     "age": 31,
#     "job": "AQA"
# }
#
# pearson["is_active"] = True
# pearson["name"] = "John"
# pearson["surname"] = "Wik"
# print(pearson)


# 7 setdefault()
# pearson = {
#     "name": "Maryna",
#     "age": 31,
#     "job": "AQA"
# }
# pearson.setdefault('salary')
# pearson.setdefault('salary', 1_000_000)
# print(pearson)


# 8 Get values by key
# pearson = {
#     "name": "Maryna",
#     "age": 31,
#     "job": "AQA"
# }
# print(pearson['name'])
# print(pearson.get('name', False))


# 9 update()
#
# pearson = {
#     "name": "Maryna",
#     "age": 31,
#     "job": "AQA"
# }
#
# pearson.update(language='Python')
# pearson.update(job='Backend developer')
# print(pearson)


# 10 GET elements
# pearson = {
#     "name": "Maryna",
#     "age": 31,
#     "job": "AQA"
# }
#
# print(pearson.items())
# print(pearson.keys())
# print(pearson.values())


# 11 Compare dictionary

# first = {'name': 'Maryna', 'age': 31}
# second = {'age': 31, 'name': 'Maryna'}
# print(first == second)


# 12 Dictionary is ordered data type
# 13 Indexing absent

# 14 Delete elements
# first = {'name': 'Maryna', 'age': 31, 'job': 'AQA'}
#
# first.pop('name')
# first.popitem()  # return tuple
# del first['age']
# print(first)


# 15 len() and sorted()
# first = {'name': 'Maryna', 'age': 31, 'job': 'AQA'}
#
# print(len(first))
# print(sorted(first))

# 16 What type can be in key for dictionary - hashable
# my_list = [1, 2, 3, 4]
# print(hash(my_list))  # TypeError: unhashable type: 'list'

# my_var = 'test'
# print(hash(my_var))

# 17 work with loops

# pearson = {
#     "name": "Maryna",
#     "age": 31,
#     "job": "AQA"
# }

# for element in pearson:
#     print(element, end=' ')  # return list of keys
#
# for key, value in pearson.items():
#     print(key, value, end=' ')



# Tasks 1
# find unique values in dictionary

# my_dict = {'first': 1, 'second': 2, 'third': 3, 'fourth': 1}
#
# elements = my_dict.copy()
#
# for key, value in elements.items():
#     if list(my_dict.values()).count(value) > 1:
#         del my_dict[key]
# print(my_dict.values())
#
# print(set(my_dict.values()))


# Task 2
# Calculate difference in age between elder and yonger
# family = {
#     'grandpa': ('Alex', 76),
#     'grandma': ('Nona', 74),
#     'dad': ('Greg', 48),
#     'mom': ('July', 45),
#     'son_older': ('Bob', 18),
#     'son_middle': ('Alex', 15),
#     'son_young': ('Mark', 10)
#
# }

# ages = []
# for name, age in family.values():
#     ages.append(age)
# result = max(ages) - min(ages)
# print(result)
