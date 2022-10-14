# 3 Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

lst_first = list(map(int, input("Введите числа через пробел: ").split()))
print(lst_first)
lst_second = []
lst_finish = []
for i in range(len(lst_first)):
    count = 0
    for j in range(len(lst_first)):
        if i == j:
            count += 1
        else:
            if lst_first[i] == lst_first[j]:
                lst_second.append(lst_first[i])
print(lst_second)

lst_finish = [n for i, n in enumerate(lst_first) if n not in lst_second]

print(lst_finish)
