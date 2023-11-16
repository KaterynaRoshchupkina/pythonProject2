import math


def calculator_function(operation, a, b):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero!")
    elif operation == 'sqrt':
        if a >= 0:
            return math.sqrt(a)
        else:
            raise ValueError("Cannot take the square root of a negative number!")
    else:
        raise ValueError("Invalid operation!")
