#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

n = int(input("Введите количество элементов в массиве A: "))
massive_a = [random.randint(1, 10) for i in range(n)]
print(massive_a)
x = int(input("Введите искомое число: "))
count = 0
for i in massive_a:
    if i == x:
        count += 1
print(count)