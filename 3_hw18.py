#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
n = int(input("Введите количество элементов в массиве А: "))
list_a = [random.randint(1, 20) for i in range(n)]
print(list_a)
x = int(input("Введите число: "))
index_x = 0
min_x = abs(x - list_a[0])
for i in range(1, n):
    buffer_x = abs(x - list_a[i])
    if buffer_x < min_x:
        min_x = buffer_x
        index_x = i
print(f"Самый близкий по величине элемент к числу: {list_a[index_x]}")
