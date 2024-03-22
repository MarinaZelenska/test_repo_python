# Task 7 check vowels

data = input("Enter your string: ")
vowels = "aeiou"
count = 0

for letter in data.lower():
    if letter in vowels:
        count += 1
print(f'Count of vowels letters in {data} string is {count}')


