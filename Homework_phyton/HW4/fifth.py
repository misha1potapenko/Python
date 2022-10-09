# 5 Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными,
# так и отрицательными. Степени многочленов могут отличаться.


with open('new_file.txt', 'r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split('+')


with open('file_2.txt', 'r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split('+')

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

# with open('sum.txt', 'w', encoding='utf-8') as file:
#     file.write(sum_pol_2)
sum_pol = []
for i in range(len(list_of_poly_2)):
    sum_pol.append(int(list_of_poly_1[i][:2]) + int(list_of_poly_2[i][:2]))
print(sum_pol)
sum_pol = sum_pol[::-1]
sum_pol_2 = "+".join([f'{(j,"")[j==1]}x^{(i, "")[i==0]}' for i, j in enumerate(sum_pol) if j][::-1])
print(sum_pol_2)


with open('sum.txt', 'w', encoding='utf-8') as file:
    file.write(sum_pol_2[0:-2])

