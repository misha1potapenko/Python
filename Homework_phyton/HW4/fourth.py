# 4 Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint
k = int(input('Введите натуральную степень k:'))

a_b_c = [randint(0, 100) for i in range(k+1)]
print(a_b_c)
poly = '+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(a_b_c) if j][::-1])
poly = poly.replace('x^1+', 'x+')
poly = poly.replace('x^0', '')
poly += ('', '1')[poly[-1] == '+']
poly = (poly, poly[:-2])[poly[-2:] == '^1']
print(poly, "= 0")
f = open('new_file.txt', 'w')
f.write(f'{poly} = 0')
f.close()
