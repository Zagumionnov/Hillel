
s = str(input("Ваша строка:"))
ch = str(input("Какой символ найти?:"))
i = 0
if s.find(ch) == 0:
    print(s.find(ch), end='. ')
while i >= 0:
    i = s.find(ch, len(ch)+i)
    if i >= 0:
        print(i, end='. ')
