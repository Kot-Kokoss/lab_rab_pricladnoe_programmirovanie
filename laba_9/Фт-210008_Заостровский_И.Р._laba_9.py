from random import randrange
from loguru import logger

logger.remove(handler_id=None)
logger.add('laba_9.log', format='{time} {level} {message}', level='INFO', rotation='10 KB', compression='zip')

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
            logger.error('N = ' + str(n))
            print('Ошибка ввода! Введите число побольше')
            n = 0
    except ValueError:
        print('Ошибка ввода!')
        logger.error('N = ' + str(n))

logger.info('N = ' + str(n))

#присвоение значения значения для загадываемого числа
hidden_number = randrange(1, n, 2)
logger.info('hidden_number = ' + str(hidden_number))

#проверка ввода количества попыток
while k == 0:

    try:
        k = int(input('Введите количество попыток K = '))
        if k < 1:
            logger.error('K = ' + str(k))
            print('Ошибка ввода! Введите число побольше')
            k = 0
    except ValueError:
        print('Ошибка ввода!')
        logger.error('K = ' + str(k))

logger.info('K = ' + str(k))

while k > 0:

    #проверка ввода предполагаемого числа
    while user_number == 0:

        try:
            user_number = int(input('Введите число = '))
            if user_number < 1:
                print('Ошибка ввода! Введите число побольше')
                logger.error('user_number = ' + str(user_number))
                user_number = 0
            elif user_number > n:
                print('Ошибка ввода! Введите число поменьше')
                logger.error('user_number = ' + str(user_number))
                user_number = 0
        except ValueError:
            print('Ошибка ввода!')
            logger.error('user_number = ' + str(user_number))

    #обработка ответов
    if hidden_number > user_number:
        message = 'Загаданное число больше вашего'
        logger.info('Attemppt_result = ' + message)
    elif hidden_number < user_number:
        message = 'Загаданное число меньше вашего'
        logger.info('Attemppt_result = ' + message)
    else:
        message = 'Поздравляем, вы угадали!'
        k = 0
        logger.info('End_result = ' + message)
    print(message)
    user_number = 0
    k -= 1

if message != 'Поздравляем, вы угадали!':
    logger.info('End_result = Увы, но попытки закончились')
    print('Увы, но попытки закончились')
