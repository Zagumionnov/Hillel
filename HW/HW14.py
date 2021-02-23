lst = [333, 10, 7108, 674, 773, 420, 100, 6000, 234, 1964]
i = 1
summa = 0
while i != len(lst) - 1:
    if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
        summa += 1
        i += 1
    else:
        i += 1
        continue
print(summa)






