
#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))
print(divide(num1, num2))

#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.


def get_integer_input(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid integer.")

try:
    num = get_integer_input("Enter an integer: ")
    print(f"You entered the integer: {num}")
except ValueError as e:
    print(e)




#3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.


def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."

filename = input("Enter the filename to open: ")
print(open_file(filename))


#4. Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical

def add_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers.")
    return a + b

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The sum of {num1} and {num2} is {add_numbers(num1, num2)}.")
except ValueError:
    print("Invalid input. Please enter numerical values.")
except TypeError as e:
    print(e)
