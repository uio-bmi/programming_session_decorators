

def write_output_to_file(file_name):

    def decorator(function):

        def new_function(*original_args, **original_kwargs):
            output = function(*original_args, **original_kwargs)
            with open(file_name, "w") as file:
                file.write(str(output))
            return output

        return new_function

    return decorator


@write_output_to_file("log.txt")
def sum_two_numbers(number1, number2):
    return number1 + number2


if __name__ == "__main__":
    sum = sum_two_numbers(2, 3)
    sum_in_file = open("log.txt").read()
    assert int(sum_in_file) == sum





