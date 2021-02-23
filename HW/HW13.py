s = str(input("Ваша строка:"))
w = s.count(" ") + 1
n = s.find(" ")
x = s.rfind(" ") + 1
c = len(s)
d = 0
g = 0
#проверка на первый пробел
if n == 0:
    w -= 1
#проверка на последний пробел
if x == c:
    w -= 1
#проверка на повторы пробелов
i = 0
i1 = -1
while not i == i1:
    d = s.find(" ", i)
    g = s.find(" ", d+1)
    i = g
    d += 1
    if d == g:
        w -= 1

print(w)
