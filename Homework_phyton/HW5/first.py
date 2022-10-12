# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open("HW.txt", "w", encoding="UTF-8") as data:
    data.write("абв аоывоаыабв ываожфыооаабвваыфа абв ваофжао овафжо абв авпвп")
with open("HW.txt", "r", encoding="UTF-8") as data:
    string = data.readline().split()
result = list(filter(lambda x: "абв" not in x, string))
print(result)
