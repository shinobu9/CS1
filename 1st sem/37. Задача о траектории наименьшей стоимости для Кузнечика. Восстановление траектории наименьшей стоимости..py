"""
Пусть теперь за нахождение в каждой клетке взимается определенная сумма денег.
Необходимо определить минимальную сумму, к-рую требуется заплатить, чтобы добраться до нужной клетки.
Задаем список цен нахождения в каждой клетке Price и список C, в который для
каждой клетки будет задаваться минимальная стоимость ее достижения.
Стоимость достижения i-ой клетки будет равна сумме стоимости нахождения в  ней
и минимальной из стоимостей достижения соседних клеток.
Вторая часть алгоритма - нахождение, какая именно траектория обладает наименьшей
стоимостью.
Сделаем массив Path, который будем заполнять номерами клеток, через которые проходила
искомая траектория.
Нужно двигаться с конца, выбирая ту клетку из двух, стоимость пребывания в которой
меньше. В конце массив нужно перевернуть
"""

Price = [10, 20, 5, 3, ...]
n = int(input())
C = [0]*(n + 1)
C[0] = Price[0]
C[1] = C[0] + Price[1]
for i in range(2, n + 1):
    C[i] = Price[i] + min(C[i - 1], C[i - 2])
print(C[n])


Path = [n]
while Path[-1] != 0:
    i = Path[-1]
    if C[i - 1] < C[i - 2]:
        Path.append(i - 1)
    else:
        Path.append(i - 2)
Path = Path[::-1]