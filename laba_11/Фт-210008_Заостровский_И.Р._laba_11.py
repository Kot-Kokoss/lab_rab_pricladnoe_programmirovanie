#переменные
c_and_c = {}
country = 0
capital = 0
capital_search = 0
n = 0

#открытие файла с названиями стран и столиц
with open('countries_and_capitals.txt', 'r', encoding='utf-8') as f:

    #создание словаря
    for i in f:
        couple = f.readline().split('_')
        c_and_c[couple[0]] = couple[1].rstrip()

#выбор функции програмы
while n == 0:

    try:
        n = int(input('Выберите нужную вам функцию\n1) вывод столицы заданного государства;\n2) вывод государства, столицей которого является заданный город.\n и введите номер = '))
        if n != 1 and n != 2:
            print('Введите 1 или 2!')
            n = 0
    except ValueError:
        print('Введите 1 или 2!')
        n = 0

#получение наименования государства с обработкой ошибок ввода
if n == 1:

    while country == 0:

        try:
            country = str(input('Введите название государства = '))
        except ValueError:
            print('Ошибка, введите название кириллицей!')
            country = 0

    print('Столица - ', c_and_c.get(country, 'Такого государства нет!'))

#получение наименования государства с обработкой ошибок ввода
if n == 2:

    while capital_search == 0:

        try:
            capital_search = str(input('Введите название столицы = '))
        except ValueError:
            print('Ошибка, введите название кириллицей!')
            capital_search = 0

    for country, capital in c_and_c.items():

        if capital == capital_search:
            print('Страна - ', country)
        else:
            print('Такой столицы нет!')