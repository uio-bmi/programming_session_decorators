class Decorator(object):
    pass


class PrintOnCall(Decorator):
    def __init__(self, print_str="Running function"):
        self._print_str = print_str

    def __call__(self, func):
        def new_func(*args, **kwargs):
            print(self._print_str)
            return func(*args, **kwargs)
        return new_func


class PrintArgs(Decorator):

    def __call__(self, func):
        def new_func(*args, **kwargs):
            print(args, kwargs)
            return func(*args, **kwargs)
        return new_func


class AssertOutputType(Decorator):
    def __init__(self, dtype=int):
        self._dtype = dtype

    def __call__(self, func):
        def new_func(*args, **kwargs):
            out = func(*args, **kwargs)
            assert isinstance(out, self._dtype)
            return out

        return new_func


class Log(Decorator):
    def __init__(self, file_name):
        self._file_name = file_name

    def __call__(self, func):
        def new_func(*args, **kwargs):
            with open(self._file_name, "w") as f:
                f.write("%s: %s, %s\n" % (func.__name__,
                                          args, kwargs))
            return func(*args, **kwargs)
        return new_func


class Takes(Decorator):
    def __init__(self, *types):
        self._types = types

    def _check(self, args):
        assert all(isinstance(arg, t) for
                   arg, t in zip(args, self._types))

    def __call__(self, func):
        def new_func(*args):
            self._check(args)
            return func(*args)
        return new_func


class Memoize(Decorator):
    def __init__(self):
        self._memo = {}

    def __call__(self, func):
        def new_func(*args):
            if args in self._memo:
                print("Memo: %s" % (args,))
            else:
                self._memo[args] = func(*args)
            return self._memo[args]
        return new_func


class Count(Decorator):
    def __init__(self):
        self._count = 0

    def __call__(self, func):
        def new_func(*args):
            self._count += 1
            print("%s called %s times" % (
                func.__name__, self._count))
            return func(*args)
        return new_func


if __name__ == "__main__":

    @PrintArgs()
    @AssertOutputType(int)
    @PrintOnCall("Hei")
    @Log("log.txt")
    @Takes(int, int)
    @Count()
    @Memoize()
    def my_func(a, b):
        return a + b

    my_func(10, 20)
    my_func(10, 20)
