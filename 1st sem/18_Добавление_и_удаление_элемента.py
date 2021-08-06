
# coding: utf-8

# In[2]:


""" 18) Добавление и удаление элемента в начале и в конце массива "вручную"
    Идея -  n, top - соответственно максимальное количество элементов и уровень заполненности.
    Реализуем заполнение массива. Последовательность чисел, которую мы туда вбиваем, заканчивается нулём.
"""
A = [0] * 1000 ## n = 1000
top = 0
x = int(input())
while x != 0:
    A[top] = x
    top += 1
""" Добавление элемента в начало : делаем сдвиг вверх (вправо). top увеличивается на 1. В нулевой элемент вбиваем то,
    что хотим добавить.
    Добавление элемента в конец : просто вписываем в A[top] то что хотим добавить и увеличиваем top на 1.
    Удаление элемента из начала : делаем сдвиг вниз и уменьшаем top на 1. Начальный элемент никуда не вбиваем - он уходит.
    Удаление из конца : последний элемент полагаем равным нулю и уменьшаем top на 1.
    По этому принципу работают методы добавления и удаления элементов в list
"""

