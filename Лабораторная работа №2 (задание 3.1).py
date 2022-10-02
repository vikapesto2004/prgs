import numpy as np
import numpy.linalg as nl


def pp(n):
    for i in n:
        print(*i)


print('Введите элементы матрицы 3x3: ')
a = np.reshape([int(input()) for i in range(9)], (3, 3))
print('Ваша матрица: '), pp(a)
print('Обратная матрица: '), pp(nl.inv(a))
