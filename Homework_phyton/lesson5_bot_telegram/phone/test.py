text = '5*3-53+21/3*11-33/3*12*325-44'
count_plus = []
count_minus = []
count_multiply = []
count_share = []
lst = []
lst_num = []
# поиск действий /*-+
for i, n in enumerate(text):
    if n == '+':
        # count_plus = i
        lst.append(i)
    elif n == '-':
        # count_minus = i
        lst.append(i)
    elif n == '/':
        count_share.append(i)
        lst.append(i)
    elif n == '*':
        count_multiply.append(i)
        lst.append(i)

print(f'/ = {count_share}')
print(f'* = {count_multiply}')
# создание списка из цифр без действий
lst_num.append(text[:lst[0]])
i = 0
while i < len(lst)-1:
    lst_num.append(text[lst[i]+1:lst[i+1]])
    i += 1
lst_num.append(text[lst[len(lst)-1]+1:])
print(lst)
print(lst_num)
# делаем деление
res = []

for k in count_share:
    for i, n in enumerate(lst):
        if k == n:
            res.append(float(lst_num[i]) / float(lst_num[i + 1]))
# заменяем результат
for m in range(len(res)):
    for k in count_share:
        for i, n in enumerate(lst):
            if k == n:
                lst_num[i] = res[m]


print(lst_num)
print(res)

# делаем умножение
# res_mul = []
# for k in count_multiply:
#     for i, n in enumerate(lst):
#         if k == n:
#             res_mul.append(float(lst_num[i]) * float(lst_num[i + 1]))
# print(res_mul)
# print(lst_num)
