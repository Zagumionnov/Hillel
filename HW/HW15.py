from random import randint

klass = [randint(130, 200) for _ in range(int(input("Количество детей в классе: ")))]
petya = int(input("Рост Пети: "))

klass.sort(reverse=True)

c_shk = 0
for i in klass:
    if i >= petya:
        c_shk += 1
    else:
        break
print(c_shk+1)