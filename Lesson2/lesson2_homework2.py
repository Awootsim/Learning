
a = 3
b = -10
c = 3

D = (b ** 2) - (a * c * 4)
# Посчитали дискриминант
x1 = ((b * -1) - (D ** 0.5)) / (2 * a)
x2 = ((b * -1) + (D ** 0.5)) / (2 * a)
# Посчитали корни
print(round(x1, 2))
print(round(x2, 2))
# Округлили
