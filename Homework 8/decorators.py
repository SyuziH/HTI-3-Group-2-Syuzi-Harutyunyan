import time


@warn_slow
def func_slow(x, y):
    time.sleep(3)
    return '{}{}{}'.format('execution of func_slow with ', (x, y),' took more than 2 seconds')


@warn_slow
def func_fast(x, y):
    print(x, y)


def warn_slow(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)

    return inner


print(func_slow(1, 2))
print(func_fast(1, 2))
