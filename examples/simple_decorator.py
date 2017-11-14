

def print_on_run(function):
    def new_function(*original_args, **original_kwargs):
        print("Running")
        return function(*original_args, **original_kwargs)
    return new_function


@print_on_run
def sum_two_numbers(number1, number2):
    return number1 + number2


if __name__ == "__main__":
    sum = sum_two_numbers(2, 3)
    print("Sum: %d" % sum)