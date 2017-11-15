from decorator import decorate
from time import time

def _timeit(f, *args, **kwArgs):
    start = time()
    result = f(*args, **kwArgs)
    print "Elapsed: ", time()-start
    return result

def timeit(f):
    return decorate(f, _timeit)

@timeit
def mycompute(n):
    for i in xrange(n):
        i*i
    return n*n


print(mycompute(10000))