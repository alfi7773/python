
from math import pi

radius = int(input('Радиус орбиты (млн. км): '))
v = int(input('Орбитальная скорость (км/с): '))
radius = float(radius)
v = float(v)

radius = radius * 1000000

year = 2 * pi * radius / v
year = year / (60*60*24)

print(round(year))