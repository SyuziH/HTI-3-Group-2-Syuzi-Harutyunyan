from time import time, sleep


def warn_slow(func):
    def inner(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        duration = end - start
        if duration >= 2:
            print('{}{}{}'.format('execution of func_slow with ',(*args, *kwargs.values()),' took more than 2 seconds'))
        return res

    return inner


@warn_slow
def func_slow(x, y):
    sleep(3)
    return x ** y


@warn_slow
def func_fast(x, y):
    print(x, y)


print(func_slow(2, 3))
print(func_fast(2, 3))
