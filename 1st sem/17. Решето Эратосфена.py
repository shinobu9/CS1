""" 17) Решето Эратосфена. n - конечное число, до которого мы хотим найти
простые числа
Идея - создаем массив с элементами равными True, потом пробегаем его. И
ндекс элемента и есть число.
Если число простое, то все кратные ему числа - составные.
"""
def eratosfen(n):
    array = [True] * n
    array[0] = False
    array[1] = False ## по определению числа 0 и 1 не считаются простыми
    for i in range(2, n):
        if array[i]: 
            for k in range(2 * i, n, i): ## range(start, stop, step)
                array[k] = False
    for k in range(n):
        print(k, ' - ', 'простое' if array[k] else 'составное')

n = int(input())
eratosfen(n)