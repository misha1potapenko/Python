# Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def ten_at_two():
    number = int(input("Введите число: "))
    lst = []
    while number >= 1:
        lst.append(number - (number // 2) * 2)
        number = number // 2
    lst_sec = lst[::-1]
    for i in range(len(lst)):
        print(lst_sec[i], end='')


ten_at_two()
