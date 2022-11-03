#переменные и массивы
distance = []
distanceId = {}
tarif = []
tarifId = {}
itog_s = {}
s = 0
x = 0
y = 0
itog = 0
#ввод колличества сотрудников с обработкой ошибок ввода
while s <= 0:
	try:
	    s = (int(input('Введите колличество сотрудников числом = ')))
	    if s <= 0:
	        print('ОШИБКА, введите число больше 0')
	except ValueError:
	        print('ОШИБКА, ВВЕДИТЕ ЧИСЛО!!!')
#ввод расстояния до дома сотрудников с проверкой ввода
for i in range(1, s + 1):
    while x <= 0:
	    try:
	        x = int(input('Введите расстояние от работы до дома, ' + str(i) + ' сотрудника в км = '))
	        if x <= 0:
	            print('ОШИБКА, введите число больше 0')
	    except ValueError:
	        print('ОШИБКА, ВВЕДИТЕ ЧИСЛО!!!')
    distance.append(x)
    distanceId[i] = x
#ввод тарифов такси с проверкой ввода
for i in range(1, s + 1):
    while y <= 0:
	    try:
	        y = int(input('Введите стоимость одного км в ' + str(i) + ' такси = '))
	        if y <= 0:
	            print('ОШИБКА, введите число больше 0')
	    except ValueError:
	        print('ОШИБКА, ВВЕДИТЕ ЧИСЛО!!!')
    tarif.append(y)
    tarifId[i] = y
#сортировка
distance.sort(reverse=True)
tarif.sort()
#распределение по такси + расчет стоимости
for i in range(1, s + 1):
    d = distance[i - 1]
    t = tarif[i - 1]
    price = d * t
#рассадка по такси
    for n in range(1, s + 1):
        if d == distanceId[n]:
            d = n
            distanceId[n] = 0
    for n in range(1, s + 1):
        if t == tarifId[n]:
            t = n
            tarifId[n] = 0
    itog_s[d] = t
    itog = itog + price
#вывод результатов
for i in range(1, s + 1):
    print('Сотрудник -', i, 'садится в такси №', itog_s[i])
#присвоение рублей
a1 = itog % 10
a2 = itog // 10 % 10
if a1 > 0:
    if a1 == 1:
        rub = 'рубль'
    if a1 == 1 and a2 == 1:
        rub = 'рублей'
    if a1 == 2:
        rub = 'рубля'
    if a1 == 2 and a2 == 1:
        rub = 'рублей'
    if a1 == 3:
        rub = 'рубля'
    if a1 == 3 and a2 == 1:
        rub = 'рублей'
    if a1 == 4:
        rub = 'рубля'
    if a1 == 4 and a2 == 1:
        rub = 'рублей'
    elif a1 > 4:
        rub = 'рублей'
else:
    rub = 'рублей'
print('Общая стоимость всех поездок = ', itog, rub)
x = itog
n = len(str(x))
itog = ''
x1 = ''
x2 = ''
x3 = ''
x4 = ''
x5 = ''
x6 = ''
if 7 > n > 3:
    c1 = x % 1000
    c2 = x // 1000
elif 0 < n < 4:
    c1 = x
a1 = c1 % 10
a3 = c1 // 100
a2 = (c1 - a3 * 100 - a1) // 10
#присвоение рублей
if a1 > 0:
    if a1 == 1:
        rub = 'рубль'
    if a1 == 1 and a2 == 1:
        rub = 'рублей'
    if a1 == 2:
        rub = 'рубля'
    if a1 == 2 and a2 == 1:
        rub = 'рублей'
    if a1 == 3:
        rub = 'рубля'
    if a1 == 3 and a2 == 1:
        rub = 'рублей'
    if a1 == 4:
        rub = 'рубля'
    if a1 == 4 and a2 == 1:
        rub = 'рублей'
    elif a1 > 4:
        rub = 'рублей'
else:
    rub = 'рублей'
if a1 > 0 and a2 != 1:
    if a1 == 1:
        x1 = 'один'
    if a1 == 2:
        x1 = 'два'
    if a1 == 3:
        x1 = 'три'
    if a1 == 4:
        x1 = 'четыре'
    if a1 == 5:
        x1 = 'пять'
    if a1 == 6:
        x1 = 'шесть'
    if a1 == 7:
        x1 = 'семь'
    if a1 == 8:
        x1 = 'восемь'
    if a1 == 9:
        x1 = 'девять'
if a2 == 1:
    if a1 == 0:
        x2 = 'десять'
    if a1 == 1:
        x2 = 'одиннадцать'
    if a1 == 2:
        x2 = 'двенадцать'
    if a1 == 3:
        x2 = 'тринадцать'
    if a1 == 4:
        x2 = 'четырнадцать'
    if a1 == 5:
        x2 = 'пятнадцать'
    if a1 == 6:
        x2 = 'шестнадцать'
    if a1 == 7:
        x2 = 'семнадцать'
    if a1 == 8:
        x2 = 'восемнадцать'
    if a1 == 9:
        x2 = 'девятнадцать'
elif a2 > 1:
    if a2 == 2:
        x2 = 'двадцать'
    if a2 == 3:
        x2 = 'тридцать'
    if a2 == 4:
        x2 = 'сорок'
    if a2 == 5:
        x2 = 'пятьдесят'
    if a2 == 6:
        x2 = 'шестьдесят'
    if a2 == 7:
        x2 = 'семьдесят'
    if a2 == 8:
        x2 = 'восемьдесят'
    if a2 == 9:
        x2 = 'девяносто'
if a3 > 0:
    if a3 == 1:
        x3 = 'сто'
    if a3 == 2:
        x3 = 'двести'
    if a3 == 3:
        x3 = 'триста'
    if a3 == 4:
        x3 = 'четыреста'
    if a3 == 5:
        x3 = 'пятьсот'
    if a3 == 6:
        x3 = 'шестьсот'
    if a3 == 7:
        x3 = 'семьсот'
    if a3 == 8:
        x3 = 'восемьсот'
    if a3 == 9:
        x3 = 'девятьсот'
if n < 4:
    if x3 != '':
        itog = x3 + ' '
    if x2 != '':
        itog = itog + x2 + ' '
    if x1 != '':
        itog = itog + x1 + ' '
    itog = itog + rub
if n > 3:
    a4 = c2 % 10
    a6 = c2 // 100
    a5 = (c2 - a6 * 100 - a4) // 10
    if a4 > 0 and a5 != 1:
        if a4 == 1:
            x4 = 'одна'
        if a4 == 2:
            x4 = 'две'
        if a4 == 3:
            x4 = 'три'
        if a4 == 4:
            x4 = 'четыре'
        if a4 == 5:
            x4 = 'пять'
        if a4 == 6:
            x4 = 'шесть'
        if a4 == 7:
            x4 = 'семь'
        if a4 == 8:
            x4 = 'восемь'
        if a4 == 9:
            x4 = 'девять'
    if a5 == 1:
        if a4 == 0:
            x5 = 'десять'
        if a4 == 1:
            x5 = 'одиннадцать'
        if a4 == 2:
            x5 = 'двенадцать'
        if a4 == 3:
            x5 = 'тринадцать'
        if a4 == 4:
            x5 = 'четырнадцать'
        if a4 == 5:
            x5 = 'пятнадцать'
        if a4 == 6:
            x5 = 'шестнадцать'
        if a4 == 7:
            x5 = 'семнадцать'
        if a4 == 8:
            x5 = 'восемнадцать'
        if a4 == 9:
            x5 = 'девятнадцать'
    elif a5 > 1:
        if a5 == 2:
            x5 = 'двадцать'
        if a5 == 3:
            x5 = 'тридцать'
        if a5 == 4:
            x5 = 'сорок'
        if a5 == 5:
            x5 = 'пятьдесят'
        if a5 == 6:
            x5 = 'шестьдесят'
        if a5 == 7:
            x5 = 'семьдесят'
        if a5 == 8:
            x5 = 'восемьдесят'
        if a5 == 9:
            x5 = 'девяносто'
    if a6 > 0:
        if a6 == 1:
            x6 = 'сто'
        if a6 == 2:
            x6 = 'двести'
        if a6 == 3:
            x6 = 'триста'
        if a6 == 4:
            x6 = 'четыреста'
        if a6 == 5:
            x6 = 'пятьсот'
        if a6 == 6:
            x6 = 'шестьсот'
        if a6 == 7:
            x6 = 'семьсот'
        if a6 == 8:
            x6 = 'восемьсот'
        if a6 == 9:
            x6 = 'девятьсот'
    #присвоение тысяч
    if 5 > a4 > 0 and a5 != 1:
        if a4 == 1:
            tis = 'тысяча'
        elif a4 == 2:
            tis = 'тысячи'
        elif a4 == 3:
            tis = 'тысячи'
        elif a4 == 4:
            tis = 'тысячи'
    else:
        tis = 'тысяч'
    if x6 != '':
        itog = x6 + ' '
    if x5 != '':
        itog = itog + x5 + ' '
    if x4 != '':
        itog = itog + x4 + ' '
    if x4 != '' or x5 != '' or x6 != '':
        itog = itog + tis + ' '
    if x3 != '':
        itog = itog + x3 + ' '
    if x2 != '':
        itog = itog + x2 + ' '
    if x1 != '':
        itog = itog + x1 + ' '
    itog = itog + rub
#вывод результатов
print('Cумма всех поездок равна:', str.capitalize(itog))
