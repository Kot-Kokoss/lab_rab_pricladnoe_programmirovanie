#массивы и переменные
n = 1
a = ''
itog = ''
abc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
c = -1
x = 2
o = 0
#получение значений переменных с обработкой ошибок ввода
while x != 0 and x != 1:
	try:
	    x = int(input('Чтобы зашифровать сообщение введите - "0", чтобы расшифровать сообщение введите - "1". = '))
	    if x != 0 and x != 1:
	        print('Ошибка ввода, введите 0 или 1!')    
	except ValueError:
		    print('Ошибка ввода, введите 0 или 1!')
while o == 0:	    
	try:
	    s = str(input('Введите сообщение (одно слово или слитно) = '))
	    o = 1
	    for i in range(0, len(s)):
	    	if s[i] not in abc:
	    		o = 0
	    if o == 0:
	    	print('Ошибка ввода, введите слово кириллицей!')    
while c < 0:
	try:
	    c = int(input('Введите отступ = '))
	    if c < 0:
	        print('Ошибка ввода, введите число больше 0!')
	except ValueError:
	    print('Ошибка ввода, введите число больше 0!')
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
#расшифровка
if x == 1:
    for i in range(0, len(s)):
        a = chunks[i]
        ind = abc.index(a) - c
        if ind < 0:
            ind = 33 - (c - abs(0 - abc.index(a)))
        itog = itog + abc[ind]
print(itog)
