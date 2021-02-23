n = int(input("Высота фигуры?:"))

#Пустой треугольник

g = 0
for i in range(0, n):
    g += 1
    for j in range(0, n-i):
        print(end="  ")
    for j in range(0, i + g):
        if j == 0 or j == (i + g) - 1 or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

#Заполненный треугольник

g = 0
for i in range(0, n):
    g += 1
    for j in range(0, n-i):
        print(end="  ")
    for j in range(0, i + g):
        print("*", end=" ")
    print()
print()

#Ромб 1 (будет +1 к h, при четных значениях, т.к. высота ромба всегда нечетная)

g = 0
k = n // 2 + 1
for i in range(0, k-1):
    g += 1
    for j in range(0, k-i):
        print(end="  ")
    for j in range(0, i + g):
        print("*", end=" ")
    print()
g = k
for i in range(k, 0, -1):
    g -= 1
    for j in range(0, k + 1 - i):
        print(end="  ")
    for j in range(0, i + g):
        if j == 0 or j == (i + g) - 1 or i == k:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

#Ромб 2
g = 0
k = n // 2 + 1
for i in range(0, k-1):
    g += 1
    for j in range(0, k-i):
        print(end="  ")
    for j in range(0, i + g):
        print("*", end=" ")
    print()
g = k
for i in range(k, 0, -1):
    g -= 1
    for j in range(0, k + 1 - i):
        print(end="  ")
    for j in range(0, i + g):
        if j == 0 or j == (i + g) - 1 or i == k or j == (i + g) // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
