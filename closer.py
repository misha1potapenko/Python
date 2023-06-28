import time


def add_one(a):
    names = []

    def add_two(b):
        names.append(b)
        return a + ', ' + ', '.join(names)

    return add_two


hello = add_one('Helolo')
print(hello("Alex"))
print(hello('Masha'))


def add_one_nonlocal(a):
    text = ''

    def add_two_nonlocal(b):
        nonlocal text
        text += ', ' + b
        return a + text

    return add_two_nonlocal


hello = add_one_nonlocal('Helolo')
print(hello("Alex"))
print(hello('Masha'))

# my_list = []
# my_str = 'aasas'
# for i in range(10):
#     my_list.append(str(i))
# print(my_str + '<' + '>'.join(my_list))


def main(func):
    def wrapper(*args, **kwargs):
        print(f'Запуск функции {func.__name__} в {time.time()}')
        result = func(*args, **kwargs)
        print(f'Результат функции {func.__name__} в {result}')
        print(f'Завершение функции {func.__name__} в {time.time()}')
        return result

    return wrapper

@main
def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


# print(f'{factorial(1000)=  }')
factorial(100)
# control = main(factorial)
# print(f'{control.__name__ =  }')
# print(f'{control(1000)=  }')
