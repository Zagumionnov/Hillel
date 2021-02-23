"""
Я не понял нужно использовать конкретные числа с примера
или любые целые на ввод, поэтому сделал 2 варианта.
"""

n1 = int(input('Ваше число:'))
x = 1
z = 0
while x ** 2 <= n1:
    z = x ** 2
    print(z, end='. ')
    x += 1

"""
n1 = 50
x = 1
z = 0
while x ** 2 <= n1:
    z = x ** 2
    print(z, end='. ')
    x += 1

n2 = 10
x = 1
z = 0
print("\n")
while x ** 2 <= n2:
    z = x ** 2
    print(z, end='. ')
    x += 1

n3 = 9
x = 1
z = 0
print("\n")
while x ** 2 <= n3:
    z = x ** 2
    print(z, end='. ')
    x += 1

n4 = 4
x = 1
z = 0
print("\n")
while x ** 2 <= n4:
    z = x ** 2
    print(z, end='. ')
    x += 1

n5 = 1
x = 1
z = 0
print("\n")
while x ** 2 <= n5:
    z = x ** 2
    print(z, end='. ')
    x += 1

n6 = 100
x = 1
z = 0
print("\n")
while x ** 2 <= n6:
    z = x ** 2
    print(z, end='. ')
    x += 1

n7 = 99
x = 1
z = 0
print("\n")
while x ** 2 <= n7:
    z = x ** 2
    print(z, end='. ')
    x += 1
"""