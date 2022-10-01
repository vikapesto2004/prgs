com = input('Доступны действия: транспонировать (А), умножить (В), определить ранг (С) \nВведите команду: ').upper()
res = []

# КОРРЕКТНОСТЬ ВВОДА КОМАНДЫ
while com not in ['A', 'B', 'C']:
    com = input('Некорректный ввод. Повторите: ').upper()


# ВЫВОД МАТРИЦЫ ПО СТРОКАМ
def pp(n):
    for i in n:
        print(*i)


# ТРАНСПОНИРОВАНИЕ
def transp(rows, cols, m):
    res = []
    if rows == cols:  # ТРАНСПОНИРОВАНИЕ КВАДРАТНОЙ МАТРИЦЫ
        for i in range(rows):
            t = []
            for j in range(cols):
                c = m[j][i]
                t.append(c)
            res.append(t)
    elif cols > rows:  # СТОЛБЦОВ БОЛЬШЕ, ЧЕМ СТРОК
        for i in range(cols):
            t = []
            for j in range(rows):
                c = m[j][i]
                t.append(c)
            res.append(t)
    else:  # СТРОК БОЛЬШЕ, ЧЕМ СТОЛБЦОВ
        for i in range(cols):
            t = []
            for j in range(rows):
                c = m[j][i]
                t.append(c)
            res.append(t)
    return res


# РАНГ (МЕТОД ГАУССА)
def r(rows, m):
    rang, res = rows, m
    if m == [[0] * rows] * rows:  # ЕСЛИ ВСЯ МАТРИЦА НУЛЕВАЯ, ТО ЕЕ РАНГ РАВЕН 0
        rang = 0
    else:
        for i in range(1, rows):
            k = res[i][0] / res[0][0]
            for j in range(rows):
                res[i][j] -= res[0][j] * k
        if rows == 3:
            k = res[2][1] / res[1][1]
            for j in range(1, rows):
                res[2][j] -= res[1][j] * k
        for i in range(rows):  # ПРОВЕРКА НА КОЛИЧЕСТВО НУЛЕВЫХ СТРОК В ПОЛУЧИВШЕЙСЯ МАТРИЦЕ
            if res[i] == [0] * rows:
                rang -= 1
    return rang


# УМНОЖЕНИЕ
def multi(rows, cols, m1, m2):
    res = []
    m2 = transp(cols, rows, m2)
    if rows == 1 and (cols == 2 or cols == 3):  # 1x2 * 2x1 ИЛИ 1x3 * 3x1
        for i in range(rows):
            t = 0
            for j in range(cols):
                t += m1[i][j] * m2[i][j]
            res.append([t])
    elif (rows == 2 or rows == 3) and cols == 1:  # 2x1 * 1x2 ИЛИ 3x1 * 1x3
        for i in range(rows):
            t = []
            for j in range(rows):
                t.append(m1[j][0] * m2[i][0])
            res.append(t)
        res = transp(rows, rows, res)
    elif rows == cols == 2:
        for i in range(cols):
            for j in range(cols):
                a = m1[i][0] * m2[0][0] + m1[i][1] * m2[0][1]
                b = m1[i][0] * m2[1][0] + m1[i][1] * m2[1][1]
            res.append((a, b))
    elif rows == cols == 3:
        for i in range(cols):
            for j in range(cols):
                a = m1[i][0] * m2[0][0] + m1[i][1] * m2[0][1] + m1[i][2] * m2[0][2]
                b = m1[i][0] * m2[1][0] + m1[i][1] * m2[1][1] + m1[i][2] * m2[1][2]
                c = m1[i][0] * m2[2][0] + m1[i][1] * m2[2][1] + m1[i][2] * m2[2][2]
            res.append((a, b, c))
    return res


if com == 'A':
    rows, cols, m = int(input('Строк: ')), int(input('Столбцов: ')), []
    print('Введите элементы матрицы: ')
    for i in range(rows):
        m.append([int(input()) for j in range(cols)])
    print('Ваша матрица:'), pp(m), print('Результат:'), pp(transp(rows, cols, m))

elif com == 'C':
    rows, m = int(input('Столбцов и строк: ')), []
    print('Введите элементы матрицы:')
    for i in range(rows):
        m.append([int(input()) for j in range(rows)])
    print('Ваша матрица:'), pp(m), print('Ранг матрицы: ', r(rows, m))

elif com == 'B':
    m1, m2 = [], []
    rows, cols, = int(input('Строк в матрице 1: ')), int(input('Стобцов в матрице 1: '))
    print('Введите элементы матрицы 1:')
    for i in range(rows):  # ЗАПОЛНЕНИЕ МАТРИЦЫ 1
        m1.append([int(input()) for j in range(cols)])

    print('Введите элементы матрицы 2:')
    for i in range(cols):  # ЗАПОЛНЕНИЕ МАТРИЦЫ 2
        m2.append([int(input()) for j in range(rows)])
    print('Матрица 1:'), pp(m1)
    print('Матрица 2:'), pp(m2)
    print('Результат: '),  pp(multi(rows, cols, m1, m2))