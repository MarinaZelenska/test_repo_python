# 1 - Built in fuction open()
# file = open('test.txt', 'r')
# print(file)  # <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1251'>
# print(file.mode)
# print(file.name)
# print(file.encoding)

# 2 - Read file data  file.read()
# print(file.read())

# 3 - Read symbols in file
# print(file.read(3))
# print(file.tell())  # get current element
# print(file.seek(0))  # set 0 element
# print(file.tell())
# print(file.read(3))  # start with previous elements

# file.close()  # important close files


# 4 - Encoding error
# file = open('test.txt', 'r', encoding='utf-8')
# print(file.read())
# file.close()

# 5 - Using loop

# file = open('test.txt', 'r', encoding='utf-8')
# for line in file:
#     print(line)
# file.close()


# 6 -  readline() and readlines()
# file = open('test.txt', 'r', encoding='utf-8')
# # print(file.readline())
# # print(file.readline(2))
# print(file.readlines())
# file.close()


# 7 - Read invalid file

# file = open('test_1.txt', 'r', encoding='utf-8') -># FileNotFoundError: [Errno 2] No such file or directory: 'test_1.txt
# print(file.read())
# file.close()


# 8 -  Where program try to find file
# import os
# print(os.getcwd())
# file_name = '../LOOPS/new.txt'
# file_name = 'test_1.txt'
#
# if os.path.exists(file_name):
#     file = open(file_name, 'r', encoding='utf-8')
#     print(file.read())
#     file.close()
# else:
#     print(f'File is not exist')


# 9 - Write data

# file_name = 'test.txt'
# # file = open(file_name, 'r', encoding='utf-8')  # io.UnsupportedOperation: not writable - тому що файл з режимом для читання
# file = open(file_name, 'w', encoding='utf-8')
# file.write('AQA')  # rewrite all file data
# file.close()


# 10 - Created new file when try to write data in unexisting file
# file_name = 'test_1.txt'
# file = open(file_name, 'w', encoding='utf-8')
# file.write('AQA')
# file.close()

# 11 mode 'r+'
# file_name = 'test_1.txt'
# file = open(file_name, 'r+', encoding='utf-8')
# file.write('t')
# file.close()

# 12 - mode 'a'
# file_name = 'test_1.txt'
# file = open(file_name, 'a+', encoding='utf-8')
# file.write('\nnew')
# file.close()


# 13 - with
# with open('test_1.txt', 'r', encoding='utf-8') as file:
#     print(file.readlines())
#
# print(file.closed)

# 14 - with
# with open('test_1.txt', 'r', encoding='utf-8') as file:
#
#     with open('written_file.txt', 'w') as new_file:
#         for line in file:
#             new_file.write(line)



