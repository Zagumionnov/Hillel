num = int(input('Введите число:'))
amount = 0
summa = 0
min_num = num
max_num = num
amount_even = 0
amount_odd = 0

while num > 0:
    summa += num
    amount += 1
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
    if num % 2:
        amount_odd += 1
    else:
        amount_even += 1
    if num == 0:
        break
    num = int(input('Введите число:'))

print("Всего чисел:", amount)
print("Сумма чисел:", summa)
print("Среднее арифметическое:", summa / amount)
print("Минимальное значение:", min_num)
print("Максимальное значение:", max_num)
print("Количество четных элементов:{0}\nКоличество нечетных элементов:{1}".format(amount_even, amount_odd))