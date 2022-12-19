from random import randrange

#переменные
n = 0
k = 0
user_number = 0
hidden_number = 0

#проверка ввода максимального числа
while n == 0:

    try:
        n = int(input('Введите максимальное число N = '))
        if n < 2:
            print('Ошибка ввода! Введите число побольше')
            n = 0
    except ValueError:
        print('Ошибка ввода!')

#присвоение значения значения для загадываемого числа
hidden_number = randrange(1, n, 2)

#проверка ввода количества попыток
while k == 0:

    try:
        k = int(input('Введите количество попыток K = '))
        if k < 1:
            print('Ошибка ввода! Введите число побольше')
            k = 0
    except ValueError:
        print('Ошибка ввода!')

while k > 0:

    #проверка ввода предполагаемого числа
    while user_number == 0:

        try:
            user_number = int(input('Введите число = '))
            if user_number < 1:
                print('Ошибка ввода! Введите число побольше')
                user_number = 0
        except ValueError:
            print('Ошибка ввода!')

    #обработка ответов
    if hidden_number > user_number:
        message = 'Загаданное число больше вашего'

    elif hidden_number < user_number:
        message = 'Загаданное число меньше вашего'

    else:
        message = 'Поздравляем, вы угадали!'
        k = 0

    print(message)
    user_number = 0
    k -= 1

if message != 'Поздравляем, вы угадали!':
    print('Увы, но попытки закончились')