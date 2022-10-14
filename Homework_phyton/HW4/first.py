# 1 Вычислить число π c заданной точностью d
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
#   pi = 3,1415926535 8979323846 2643383279 5028841971 6939937510




def pi():
    k = float(input("Введите точность от 0,1 до 0,0000000001  :  "))
    d = int(1/k) * 10
    count = -1
    number = 1
    while number < d:
        number *= 10
        count += 1
    pi_for = 1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9
    for i in range(5, d):
        pi_for = pi_for + (1 / (2 * i + 1)) * (-1) ** i
    pi_ = str(pi_for * 4)
    print(f'Точность  pi = {pi_[:count+2]} до {count} знака после запятой')


pi()

