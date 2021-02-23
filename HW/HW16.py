from random import randint

s = [randint(1, 100) for _ in range(10)]
i = randint(0, 9)
print("Начальный список: ", s, type(s), id(s))
print("Индекс: ", i)
while i != len(s) - 1:
    s[i] = s[i + 1]
    i += 1
s.pop()
print("Итоговый список: ", s, type(s), id(s))
