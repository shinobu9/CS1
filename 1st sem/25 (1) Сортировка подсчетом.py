""" 25) Сортировка подсчётом.
Допустим, элементы массива есть цифры от 0 до 9. Ну могут быть и чи
сла от 0 до 999. Потребление памяти
прямопропорционально длине этого отрезка. Пробегая массив просто сч
итаем сколко раз встречались числа из списка.
Дальше очевидно.
"""
N = int(input()) ## длина массива
F = [0] * 10 ## массив - счётчик
for i in range(N):
    x = int(input())
    F[x] += 1 ## F[9] - кол-во встреченных девяток
    for i in range(10):
        for j in range(F[i]):
            print(i, end=' ')
