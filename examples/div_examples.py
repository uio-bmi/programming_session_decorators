

def print_nice_result(function):
    def new_function(number1, number2):
        return "Result is: %d" % function(number1, number2)

    return new_function

@print_nice_result
def multiply(number1, number2):
    return number1 * number2

@print_nice_result
def sum_numbers(number1, number2):
    return number1 + number2

print(multiply(4, 2))
print(sum_numbers(3, 2))