# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open("HW_5.txt", "w") as data:
    data.write("abc dfgsdabc jfhjkhj fsafas rttrey uyutyu abcdsgfg abc  ghtryr")
with open("HW_5.txt", "r") as data:
    string = data.readline().split()
result = list(filter(lambda x: True if x.find("abc") == -1 else False, string))
print(result)
