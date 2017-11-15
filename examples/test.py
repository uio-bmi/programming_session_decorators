from functools import wraps

def print_nice_result(function):

    @wraps(function)
    def new_function(a, b, *args, **kwargs):
        output = function(a, b, *args, **kwargs)
        print("Result %s: %d" % (function, output))
        return output
    return new_function


@print_nice_result
def multiply(number1, number2):
    return number1 * number2

@print_nice_result
def sum_numbers(number1, number2):
    return number1 + number2

@print_nice_result
def subtract(a, b):
    return a-b

@print_nice_result
def add_three_numbers(a, b, c):
    return a + b + c

multiply(2, 3)
subtract(5, 4)
add_three_numbers(1, 2, 1)








