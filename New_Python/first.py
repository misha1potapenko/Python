# ✔Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# ✔*Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.
# import random
#
# my_list = []
# for i in range(21):
#     my_list.append(random.randint(20))

# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если
# возможно в один из вариантов ниже: ✔Целое положительное число
# ✔Вещественное положительное или отрицательное число ✔
# Строку в верхнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔Строку в нижнем регистре в остальных случаях

# user_input = input("Введите что-либо ")
#
# if user_input.isdigit():
#     print("Целое число ", user_input)
#
# elif user_input.replace(".", "").replace("-", "").isdigit():
#     print("Вещественное число ", user_input)
#
# elif user_input == user_input.lower():
#     print("Все строчные ", user_input)
#
# else:
#     print("Есть хотябы одна заглавная  ", user_input.upper())

# my_tuple = (3, 4.2, True, "Help", 5, False)
#
# my_dict = {}
#
# for i in my_tuple:
#     if type(i) not in my_dict.keys():
#
#         my_dict[type(i)] = [i]
#     else:
#         my_dict[type(i)].append(i)
# print(my_dict)
#
#
# spam = my_dict.setdefault('five')
#
# eggs = my_dict.setdefault('six', 6)

# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.





