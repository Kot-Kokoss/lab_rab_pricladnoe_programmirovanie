#переменные
n = 0
denominations = [64, 32, 16, 8, 4, 2, 1]
used_denominations = []

#ввод и проверка суммы N
while n == 0:

    try:
        n = int(input('Введите сумму = '))
        if n < 1:
            print('Ошибка ввода!!! Введите положительное число')
            n = 0
        elif n % 1 != 0:
            print('Ошибка ввода!!! Введите целое число')
            n = 0
    except ValueError:
        print('Ошибка ввода!')

#отбор и запись номиналов купюр в use_denominations
while n != 0:

    for i in range(0, len(denominations)):

        if n - denominations[i] >= 0:
            used_denominations.append(denominations[i])
            n = n - denominations[i]
            break

#вывод результатов для каждого номинала
print('Купюр по 64 = ' + str(used_denominations.count(64)) +
      '\nКупюр по 32 = ' + str(used_denominations.count(32)) +
      '\nКупюр по 16 = ' + str(used_denominations.count(16)) +
      '\nКупюр по 8 = ' + str(used_denominations.count(8)) +
      '\nКупюр по 4 = ' + str(used_denominations.count(4)) +
      '\nКупюр по 2 = ' + str(used_denominations.count(2)) +
      '\nКупюр по 1 = ' + str(used_denominations.count(1)))