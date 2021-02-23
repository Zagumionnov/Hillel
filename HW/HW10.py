s = str(input('Ваша строка:'))
print(s[0] + s[1:-1].replace('h', 'H') + s[-1])