"""19) Алгоритм обращения чисел в массиве. Реализация циклом, без срезов"""
def reverse_array(array):
    n = len(array)
    for i in range(n // 2):
## доходим до половины массива только. Если идти дальше, то массив перевернется обратно
        array[i], array[n - 1 - i] = array[n - 1 - i], array[i]