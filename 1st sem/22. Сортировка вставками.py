"""
Сортировка вставками.
Идея - берём первый элемент. Он отсортирован. Двигаемся вперёд.
Если второй элемент больше первого, то ничего не делаем.
В противном случае меняем их местами. Двигаемся дальше.
Если третий элемент меньше второго, мы путём обмена местами ставим его
на место второго и затем сравниваем с первым.....
"""
def insert_sort(array):
    N = len(array)
    for top in range(1, N): ## top - индекс элемента, который мы хотим вставить в отсортированную часть
        k = top
        while k > 0 and array[k] < array[k - 1]:
            array[k], array[k - 1] = array[k - 1], array[k]
            k -= 1

if __name__ == "__main__":          
    a = [3,46,345,2,23,3452,0,34,32,1,8,92,4]
    insert_sort(a)
    print(a)