text = '5-53+21-33/6*12*3-4'
count_plus = 0
count_minus = 0
count_multiply = 0
count_share = 0
lst = []
lst_num = []
for i, n in enumerate(text):
    if n == '+':
        count_plus = i
        lst.append(count_plus)
    elif n == '-':
        count_minus = i
        lst.append(count_minus)
    elif n == '/':
        count_share = i
        lst.append(count_share)
    elif n == '*':
        count_multiply = i
        lst.append(count_multiply)
lst.sort()
lst_num.append(text[:lst[0]])
i = 0
while i < len(lst)-1:
    lst_num.append(text[lst[i]+1:lst[i+1]])
    i += 1
lst_num.append(text[lst[len(lst)-1]+1:])
print(lst)
print(lst_num)
