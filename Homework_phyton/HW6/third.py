# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# first_lst = [5, 10, 8, 1, 3, 7, 4, 2, 1, 7, 3]
#
#
# def sum_lst(lst=[]):
#     second_list = []
#     j = len(lst)
#     if j % 2 == 0:
#         for i in range(j-1):
#             second_list.append(lst[i] * lst[j-1])
#             j -= 1
#             if j == len(lst)/2:
#                 break
#     else:
#         for i in range(j-1):
#             second_list.append(lst[i] * lst[j-1])
#             j -= 1
#             if j == i:
#                 break
#     print(second_list)
#
#
# sum_lst(first_lst)

first_lst = [5, 10, 8, 1, 3, 7, 4, 2, 1, 7, 3]
second_lst = first_lst[::-1]
finish_lst = [a + b for a, b in zip(first_lst, second_lst)]
if len(finish_lst) % 2 == 0:
    len_lst = int(len(first_lst) / 2)
    print(finish_lst[:len_lst])
else:
    print(finish_lst[:(len(first_lst)) // 2 + 1])
