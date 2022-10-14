# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# first_list = [1.9, 3.4, 5.4, 8.42, 1.08, 3, 4.12]
#
#
# def difference(lst=[]):
#     second_lst = []
#     for i in range(len(lst)):
#         second_lst.append(round((lst[i] % 1), 2))
#     min_ind = second_lst[0]
#     max_ind = second_lst[0]
#     for i in range(len(second_lst)):
#         if min_ind > second_lst[i] and second_lst[i] != 0:
#             min_ind = second_lst[i]
#         if max_ind < second_lst[i]:
#             max_ind = second_lst[i]
#     dif = round((max_ind - min_ind), 2)
#     print(second_lst)
#     print(f'{max_ind} - {min_ind} = {dif}')
#
#
# difference(first_list)

first_list = [1.9, 3.4, 5.4, 8.42, 1.08, 3, 4.12]


def difference(lst=[]):
    second_lst = list(map(lambda x: x % 1, first_list))
    min_ind = second_lst[0]
    max_ind = second_lst[0]
    for i in range(len(second_lst)):
        if min_ind > second_lst[i] and second_lst[i] != 0:
            min_ind = second_lst[i]
        if max_ind < second_lst[i]:
            max_ind = second_lst[i]
    dif = round((max_ind - min_ind), 2)
    print(second_lst)
    print(f'{max_ind} - {min_ind} = {dif}')


difference(first_list)
