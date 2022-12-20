from random import randrange
from loguru import logger

logger.remove(handler_id=None)
logger.add('laba_8.log', format='{time} {level} {message}', level='INFO', rotation='1000 KB', compression='zip')

#переменные
n = 0
number = 0
not_used_numbers = []
used_numbers = []
button = 2

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

for i in range(1, n + 1):
    not_used_numbers.append(i)

logger.info('Not_used_numbers = ' + str(not_used_numbers))

#проверка кол-ва оставшихся бочонков и
while len(used_numbers) < n:

    #проверка ввода кнопки продолжения/завершения
    while button == 2:

        try:
            button = int(input('Для продолжения введите - 1, для завершения - 0 = '))

            if button != 0 and button != 1:
                logger.error('Button = ' + str(button))
                print('Ошибка ввода!')
                button = 2

        except ValueError:
            print('Ошибка ввода!')
            logger.error('Button = ' + str(button))

    logger.info('Button = ' + str(button))

    #выбор случайного бочонка
    if button == 1:

        #получение номера
        i = randrange(0, len(not_used_numbers))
        number = not_used_numbers[i]

        #изменение списков
        not_used_numbers.remove(number)
        used_numbers.append(number)
        logger.info('Selected_number = ' + str(number))
        logger.info('Used_numbers = ' + str(used_numbers))
        logger.info('Not_used_numbers = ' + str(not_used_numbers))

        button = 2
        print('Номер случайно выбранного бочонка = ' + str(number))

    else:
        n = 0

print('Работа программы завершена.')
logger.info('Program finished!')