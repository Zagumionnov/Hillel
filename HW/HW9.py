"""
Сделал универсальную программу на ввод. Работает на все числа из примера.
"""

n1 = int(input('Введите число:'))
x = 2
y = 1
z = 0
h = 0

while y <= n1 and n1 > 0:
    if n1 == 1:
        z = y
        print(h, z)
        break
    y *= x
    if y <= n1:
        z = y
        h += 1
    if y > n1:
        print(h, z)
        break
else:
    print("zero")

