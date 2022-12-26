from loguru import logger

#переменные
example = [ ]
alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operation = ['+', '-', '*', '/']
value = 0
s = 0

#создание файла с логами
logger.remove(handler_id=None)
logger.add('laba_12.log', format='{time} {level} {message}', level='INFO', rotation='10 KB', compression='zip')

#ввод выражения с проверкой его правильности
while s == 0:

    s = str(input('Введите математическое выражение = '))

    for i in range(0, len(s)):

        if (s[i] not in alphabet) and (s[i] not in operation):
            print('Ошибка ввода, недопустимый символ!!!')
            s = 0
            logger.error('S = ' + str(s))

logger.info('S = ' + str(s))

#разбиение выражения на числа и операторы
for i in range(0, len(s)):

    if s[i] in alphabet:
        if value == 0:
            value = s[i]
        else:
            value += s[i]

    else:
        example.append(value)
        example.append(s[i])
        value = 0
example.append(value)
logger.info('Example = ' + str(example))

#выполнение функций операторов
while len(example) != 1:

    #операторы 1 приоритета
    i = 1
    while ('*' in example) or ('/' in example):

        #умножение
        if example[i] == '*':
            example[i - 1] = int(example[i - 1]) * int(example[i + 1])
            example.remove(example[i])
            example.remove(example[i])

        #деление
        elif example[i] == '/':
            example[i - 1] = int(example[i - 1]) / int(example[i + 1])
            example.remove(example[i])
            example.remove(example[i])

        else:
            i += 1
    logger.info('Example_after_1_order= ' + str(example))

    #операторы 2 приоритета
    i = 1
    while ('+' in example) or ('-' in example):

        #сложение
        if example[i] == '+':
            example[i - 1] = int(example[i - 1]) + int(example[i + 1])
            example.remove(example[i])
            example.remove(example[i])

        #вычитание
        elif example[i] == '-':
            example[i - 1] = int(example[i - 1]) - int(example[i + 1])
            example.remove(example[i])
            example.remove(example[i])
    logger.info('Example_after_2_order= ' + str(example))
    logger.info('Result = ' + str(example))

#вывод результатов
print('Результат вычислений = ', example[0])
logger.info('Program finished!')