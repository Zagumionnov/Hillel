from random import randint

m = int(input("Введите кол-во строк: "))
n = int(input("Введите кол-во колонок: "))

lst1 = [[randint(1, 50) for j in range(n)] for i in range(m)]

total = 0

for i in range(m):
    for j in range(n):
        total += lst1[i][j]
        print('{:<3}'.format(lst1[i][j]), end='  ')
    print('  ', total)
    total = 0
print()

total1 = [0 for i in range(n)]
for y in range(len(lst1)):
    total1 = [total1[index] + i for index, i in enumerate(lst1[y])]

for i in range(len(total1)):
    print('{:<3}'.format(total1[i]), end='  ')





