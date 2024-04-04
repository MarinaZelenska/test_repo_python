import csv

# 1 - Read csv file
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for line in csv_reader:
#         print(line)

# 2 - Get data in column using indexing
#
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line[2])

# 3 - Write data + delimiter + newline

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#
#     with open('new.csv', 'w', newline='') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#         csv_writer.writerows(csv_reader)
# or
# for line in csv_reader:
#     csv_writer.writerow(line)

# 4 -Work with csv + dict

# 4.1 Read
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         print(line['email'])

# 4.2 Write

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     with open('new_1.csv', 'w', newline='') as new_file:
#         fieldnames = ['first_name', 'last_name', 'email']
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
#
#         csv_writer.writeheader()
#
#         for line in csv_reader:
#             csv_writer.writerow(line)

# 4.3 Write partialy

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     with open('new_1.csv', 'w', newline='') as new_file:
#         fieldnames = ['first_name', 'email']
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
#
#         csv_writer.writeheader()
#
#         for line in csv_reader:
#             del line['last_name']
#             csv_writer.writerow(line)

# With data
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     with open('new_1.csv', 'w', newline='') as new_file:
#         fieldnames = ['first_name', 'email']
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
#
#         csv_writer.writeheader()
#
#         for line in csv_reader:
#             for key in list(line.keys()):
#                 if key not in fieldnames:
#                     del line[key]
#             csv_writer.writerow(line)


