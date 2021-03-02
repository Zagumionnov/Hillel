file1 = open('src_14.txt', encoding='utf-8')
file2 = open('src_14_2.txt', 'w', encoding='utf-8')

cb = 0
p = '{:<15}{:1}'

for line in file1:
    # Разбиваем каждую строку на список строк
    line = line.split()
    # Записываем Фамилию и первую букву имени
    n = line[1] + ' ' + line[0][0] + '.'
    # Считаем средний балл по каждому уч.
    srbu = round(sum([int(s) for s in line[2:]]) / len(line[2:]), 2)
    # Выводим всех уч. чей бал меньше 5
    if srbu < 5:
        print(p.format(n, srbu))
    # Записываем все в новый файл
    file2.write(p.format(n, srbu))
    file2.write('\n')
    cb += srbu

# Ситаем средний балл
print(p.format('Средний балл класса:', round(cb/12, 2)))

file1.close()
file2.close()

