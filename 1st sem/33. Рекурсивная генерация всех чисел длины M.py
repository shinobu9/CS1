"""
n! - количество перестановок n чисел в n позиций
Как же выдать все перестановки с помощью питончика?
Ответ прост - рекурсия!

Сгенерировать все перестановки, которые начинаются на 0, 1, 2, 3, ..., N - 1
N- основание системы исчисления
M - количество чисел
"""

#для любой системы исчисления
def generate_numbers(N:int, M:int, prefix = None): #prefix - начало чиселки, т.е. ф
    #функция генерирует все числа (с началом 0) в N-ричной системе счисления(N <= 10)
    #длины M
    prefix = prefix or []  # если префикс равен нану, то это ложь, создается пустой список
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M - 1, prefix)
        prefix.pop()

"""
Отличие от рекурсивного обычного исполнения в том, что мы вызываем рекурсию в цикле.
"""

"""
Более простой вариант без цикла (только для двоичной системы исчисления):
"""
def gen_bin(M, prefix=''):
    if M == 0:
        print(prefix)
        return
    gen_bin(M - 1, prefix + '0')
    gen_bin(M - 1, prefix + '1')
    
generate_numbers(3, 2)