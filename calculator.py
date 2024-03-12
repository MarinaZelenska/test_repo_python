number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))
operation = input("Enter operation (+,-,*,/): ")

if operation == '+':
    result = number_1 + number_2
elif operation == '-':
    result = number_1 - number_2
elif operation == '*':
    result = number_1 * number_2
elif operation == '/':
    if number_2 == 0:
        result = "Division by 0"
    else:
        result = number_1 / number_2
else:
    result = "Invalid operation"

print(result)
print("Something")
