w = {}
p = 1
n = 0
k = -1
#функция для ограничения кол-во знаков после запятой
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
while p == 1:
    itog = 0
    #получение числа критериев с обработкой ошибок ввода
    while n <= 0 or n % 1 > 0:
        try:
            n = int(input('Введите количество критериев целым числом = '))
            if n <= 0:
                print('ОШИБКА, введите число больше 0!')
            if n % 1 > 0:
                print('ОШИБКА, введите целое число!')
        except ValueError:
                print('ОШИБКА, ВВЕДИТЕ ЧИСЛО!!!')
    #создание единичной матрицы размерности n
    A = []
    for i in range(0, n):
        d = []
        for j in range(0, n):
            if i == j:
                d.append(1)
            else:
                d.append(0)
        A.append(d)
    # print(*A, sep="\n", end="\n\n")
    #заполнение матрицы коэффицентами
    for j in range(0, n - 1):
        for i in range(j + 1, n):
            #проверка ввода
            while k < 0 or round(k, 2) != k:
                try:
                    k = float(input('Введите отношение важности для ' + str(j + 1) + ' критерия к ' + str(i + 1) + ' c точностью 0.00 = '))
                    if k < 0:
                        print('ОШИБКА! Введите положительное число')
                    if round(k, 2) != k:
                        print('ОШИБКА! Введите число c точностью 0.00')
                except ValueError:
                    print('ОШИБКА, ВВЕДИТЕ ЧИСЛО!!!')
            A[i][j] = k
            A[j][i] = k ** (-1)
            k = -1
    #расчёт суммы каждой строки
    for i in range(0, n):
        s = 1
        for j in range(0, n):
            s = s * A[i][j]
        s = s ** (1/n)
        w[i] = s
    # print(*A, sep="\n", end="\n\n")
    #расчёт и вывод итогового коэффицента для выбранного критерия c проверкой ввода
    v = n + 1
    for i in w:
        itog += w[i]
    for v in range(0, n):
        print('Итоговый коэффицент w'+ str(v + 1) + '=', toFixed(w[v] / itog, 2))
    p = int(input('Для продолжения работы с программой введите - "1", для завершения введите - "0". = '))
    n = 0
    if p == 0:
        print('Работа программы завершена.')
