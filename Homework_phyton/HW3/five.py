# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fib():
    number_fib = int(input("Введите целое число: "))
    lst_fib = [1, 0, 1]
    for i in range(3, number_fib + 2):
        lst_fib.append(lst_fib[i - 1] + lst_fib[i - 2])
    # print(lst_fib)
    lst_fib_1 = []
    j = -1
    for i in range(3, number_fib + 2):
        lst_fib_1.append(lst_fib[i] * j)
        j *= -1
    lst_fib_2 = lst_fib_1[::-1]
    # print(lst_fib_2)
    lst = lst_fib_2 + lst_fib
    print(lst)

fib()

