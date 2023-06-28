import time


def count(num: int = 1):
    def deco(func):
        def wrapper(*args, **kwargs):
            time_for_count = []
            result = None
            for _ in range(num):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                stop = time.perf_counter()
                time_for_count.append(stop - start)
            print(f' Результат замеров  = {time_for_count}')
            return result

        return wrapper

    return deco


@count(10)
def factorial(n):
    # print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

print(f'{factorial(1000) = }')
print(f'{factorial(1000) = }')