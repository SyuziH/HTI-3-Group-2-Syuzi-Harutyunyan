import sys


def is_odd(value):
    is_odd = True
    for i in str(value):
        if int(i) % 2 == 0:
            is_odd = False
            break
    return is_odd


def odd_numbers(start, stop):
    for i in range(int(start), int(stop)):
        if is_odd(i):
            yield i


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError
    start = sys.argv[1]
    stop = sys.argv[2]

    for el in odd_numbers(start, stop):
        print(el, end=' ')
