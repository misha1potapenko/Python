import random


def cache(func):
    _cache_dict = {}

    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]

    return wrapper


@cache
def factorial(n):
    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


@cache
def rnd(a, b):
    return random.randint(a, b)


print(rnd(1, 10))
print(rnd(1, 10))
print(rnd(1, 10))
print(rnd(1, 10))
