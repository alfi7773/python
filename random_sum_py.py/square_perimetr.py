import math

AB = input('длина первого катета: ')
AC = input('длина второго катета: ')

AB = float(AB)
AC = float(AC)

BC = math.sqrt(AB ** 2 + AC ** 2)

S = (AB * AC) / 2
P = AB + AC + BC
print(f'площадь треугольника %.2f' % S)
print(f'периметр треугольника %.2f' % P)