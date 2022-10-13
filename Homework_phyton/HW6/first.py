# 15.	Напишите программу, которая принимает на
# вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# o	пусть N = 4, тогда [ 1, 2, 6, 24 ]\
#     (1, 1*2, 1*2*3, 1*2*3*4)


# def factorial(num):
#     numbers = int(input("Введите число "))
#     list = []
#     multiplication = 1
#     for i in range(1, numbers + 1):
#         list.append(multiplication * i)
#         multiplication = multiplication * i
#     print(list)
#
#
# factorial(5)

numbers = int(input("Введите число: "))
lst = [n for n in range(1, numbers + 1)]
print(lst)
def factor(lst):
    sum_ = 1
    lst_ = []
    for i in range(1, len(lst) + 1):
        lst_.append(sum_ * i)
        sum_ = sum_ * i
    print(lst_)

factor(lst)
