"""
    Содержание:
    1. Множества
    2. Словари



Коллекции:
Множества и словари:

Многие вещи в питоне построены на словарях.

Множества:
    s = set() - создание множеств и конвертирует послед. в множество

        строку конвертируем в множество:

        s = "fdfsdfsdfs"
        new_set = set(s)
        print(new_set)
        Получим:
        {'d', 'f', 's'} <class 'set'>


    set - хранит только уникальные объекты. Все объекты в разброс (все объекты хэшируются для оптимизац.)
    Поэтому не можем обращаться к элементу по индексу.
    Set - Используется для математических исчислений (как вариант, если нужно исключить из коллекции
          повторяющееся значение

    new_set.add(45) - добавления объекта в множество (куда это значение будет вставлено, мы не знаем)
    print(new_set)

    перебираем элементы set можно циклом
    for el in net_set:
        print(el, end=' ')

    Сеты можно сравнивать и можно применять спец. операции которые позволят получить из 2х наборов
    какуюто определенную выборку:

    s1 = {33, 40, 41, 10, 11, 13, 15, 16, 17, 18, 48, 49, 19, 25, 29, 31}
    s2 = {35, 36, 40, 41, 44, 45, 46, 15, 48, 49, 18, 13, 24, 25, 27, 29, 31}
    print(s1)
    print(s2)

    # A | B или A.union(B) - объединение (получим новый сет)
    # A |= B или A.update(B) - обновит сет А

    print(s1 | s2)
    print(s1 |= s2)

    # A & B - A.intersection(B) - пересичения двух сетов (Получаем только эл. которые присутствуют как
                                                          в первом так и во втором сете)
    # A & B - A.intersection_update(B) - или с апдейтом А

    print(s1 & s2)

    # A - B или A.difference(B) - получаем только те значения которых есть в первом но нет во втором
    # A -= B или A.difference_update(B)

    print(s1 - s2)

    # A * B или A.symmetric_difference(B) - получаем уникальные ел. из первого и уник. ел из второго сета
                                            и результат объеденить
    # A *= B или A.symmetric_difference_update(B)

    print(s1 * s2)

    #set.remove(36) - удаляет елемент из сета
    #set.discard(36) - удаляет елемент из сета. (В случае если передаем не сущ. значение,
                                                    не выдаст ошибку)

    set, т.к. это коллекция, всегда можно конвертировать например в скписок или кортеж

    ###frozen_set - неизменяемый объект.
    Можно применять все что и для сет, если не изменяет фрозенсет.

    fs = frozenset():
    print(fs, type(fs))

Словари:

    d = {
        key: value, (Если нам нужно обратиться, изменить или добавить значене в словарь,
        key: value,  то обращаемся по ключу. Ключ что-то типо индекса в строках)
    }

    Способы создания:

    d = {}
    d = dict()
    d = {1: 'one', 2: 'two'}

    Словарь можно создать из списка кортежей:

    d = dict(
        [
            (1, 'one'),
            (2, 'two'),
        ]
    )
    print(d, type(d))

    Так же словарь можно создать с помощью именованых параметров:

    d = dict(
        one=1,
        two=2,
    )
    print(d, type(d))

    Может возникнуть заблужд. что мы обращаемся к словарю по индексу. Мы обращаемся по ключу!!!

    d = {
        0: 'zero'
        1: 'one'
        2: 'two'
        -1: 'negative one'
    }
    print(d[0]) - обращаемся к значению по ключу
    print(d[-1]) - обращаемся к значению по ключу

    В качестве ключа может быть - кортеж, число, строка (те типы данных которые не изменяются)

    Словарь изменяемый тип объекта. Мы можем в него что-то добавить:

    d['name'] = 'Ivan' - если такого ключа в словаре небыло, то клч будет добавлен
    print(d)
    d['surname'] = 'Petrov'
    print(d)
    d['name'] = 'Petr' - если такой ключ уже сущ., то он будет обновлен

     Может хранить список:
     d['children'] = ['Sergey', 'Maria', 'Olga']
     print(d['children'][1])

     Может хранить словарь:
     d['pets'] = {'cat': 'Fox', 'dog': 'Pluto'}
     print(d['pets']['cat'])

     len() - возвращает кол-во записей в словаре
     print(len(d))

     d.clear() - очищает словарь, но не удаляет
     print(d)

     get(key, default_value) - для обращения к словарю.  default_value не обязательно
     print(d.get('name1', 'Alyona' )) - если я укажу не сущ ключ - вернеться None. Если еще укажу
                                        default_value то функция вернет мне дефолтное значение.

     keys() - получем список ключей
     print(d.keys())

     values() - получаем список значений
     print(d.values())

     items() - возвращает список кортежей
     print(d.items())
     Этот список можно перебирать циклом
     - на каждой итерации будет возвращен 1 кортеж, этот кортеж можно разпаковать сразу в переменную
     for key, value in d.items():
        print(key, value)

     pop(key) - возвращ запись по ключу и запись будет удалена
     print(d.pop('surname'))
     print(d)

     popitem() - будет возвращать случайную пару из словаря и запись из словаря удаляется
     print(d.popitem())

     update(dict) - позв. обновить записи одного словаря, записями дурого словаря, если в перво словаре
                    нет таких ключей как во втором, они будут добавлены

     d1 = {'a': 10, 'b':20, 'c': 30, 'd': 40}
     d2 = {'e': 200, 'b':300}
     print(d1)
     print(d2)
     d1.update(d2)
     print(d1)

     Можно словарь создать из списка(.fromkeys()). В качестве кулючей будут использованы эл. списка, а в качестве
     значений - None. Позже, когда нам нужно значения можно туда добавить

     lst = ['One', 'Two', 'Three']
     d = dict.fromkeys(lst)
     print(d)











"""
