# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

first_lst = [5, 10, 8, 15, 26, 7, 45, 32, 18, 7, 44, 10]


def sum_lst(lst=[]):
    sum_list = 0
    for i in range(1, len(lst), 2):
        sum_list = sum_list + first_lst[i]
    print(sum_list)


sum_lst(first_lst)