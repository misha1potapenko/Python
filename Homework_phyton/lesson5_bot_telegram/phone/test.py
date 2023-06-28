text = '55/3*25/2-53+21-33/6*12*3/4-4'

count_plus = 0
count_minus = 0
count_multiply = 0
count_share = 0
# создаем список из позиций действий
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
# создаем список из чисел в строке
lst_num.append(text[:lst[0]])
i = 0
while i < len(lst)-1:
    lst_num.append(text[lst[i]+1:lst[i+1]])
    i += 1
lst_num.append(text[lst[len(lst)-1]+1:])
print(lst)
print(lst_num)
count = None
text1 = None
for i, n in enumerate(text):
    share = 0
    if n == '/' and i in lst:
        share = 0
        # находим индекс элемента в списке
        count = lst.index(i)
        if count == 0:
            share = float(lst_num[0])/float(lst_num[1])
            share = str(share)
            text1 = text.replace(text[:lst[count + 1]], share)
            print(text[:lst[count + 1]])
            print(text1)
        else:
            share = float(lst_num[count]) / float(lst_num[count+1])
            share = str(share)
            text1 = text.replace(text[lst[count-1]+1:lst[count+1]], share)
            print(share)
            print(text[lst[count-1]+1:lst[count+1]])
            print(text1)
