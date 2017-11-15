import numpy as np
from timeit import timeit
from functools import wraps

def memoize(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if hasattr(wrapper, "memo"):
            if args in wrapper.memo:
                return wrapper.memo[args]

        output = function(*args, **kwargs)
        wrapper.memo = {}
        wrapper.memo[args] = output
        return output

    return wrapper

@memoize
def sum_numbers(n):
    return np.sum(range(0, n))

print(timeit("sum_numbers(1000)", "from __main__ import sum_numbers", number=10000))