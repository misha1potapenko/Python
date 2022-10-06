# 2 Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]


def mnoj():
    number = int(input("Введите число N = "))
    lst_num = []
    k = 2
    while number != 1:
        if number % k == 0:
            lst_num.append(k)
            number /= k
        else:
            k += 1
    print(lst_num)


mnoj()