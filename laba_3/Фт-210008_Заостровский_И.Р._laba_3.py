#получение значений переменных
x = int(input('Чтобы зашифровать сообщение нажмите - "0", чтобы расшифровать сообщение введите - "1". = '))
s = str(input('Введите сообщение (одно слово или слитно) = '))
c = int(input('Введите отступ = '))
#массивы и переменные
n = 1
a = ''
itog = ''
abc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#разбиение послания на отдельные элементы
chunks = [s[i:i+n] for i in range(0, len(s), n)]
#шифровка
if x == 0:
    for i in range(0, len(s)):
        a = chunks[i]
        ind = abc.index(a) + c
        if ind > 32:
            ind = c - abs(32 - abc.index(a)) - 1
        itog = itog + abc[ind]
    print(itog)
#расшифровка
if x == 1:
    for i in range(0, len(s)):
        a = chunks[i]
        ind = abc.index(a) - c
        if ind < 0:
            ind = 33 - (c - abs(0 - abc.index(a)))
        itog = itog + abc[ind]
    print(itog)
