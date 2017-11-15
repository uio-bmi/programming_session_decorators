# Programming session on decorators

Some examples can be [found here](https://github.com/uio-bmi/programming_session_decorators/tree/master/examples).

# Example decorators that can be made

**@print_on_call**
Prints something every time the method is being called.

**@print_arguments_on_call**
Prints string of arguments every time the method is being called.

**@assert_output_is_int**
Checks the output of the method. Asserts that the output is int (`isinstance(output, int)`)

**@assert_output_is(type)**
Asserts that the output is of the given type.

**@log(file_name)**
Logs the method name and input to file.

**@takes(type1, type2, ...)**
Asserts that all arguments are of the given types

**memoize**
Memoizes the output of the function. Using the arguments as unique key.

**@count_calls**
Counts have many time each method is being called. Prints or logs the number of times.

....
