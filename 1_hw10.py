n = int(input('введите количество монет')) #
k = 0
for i in range(n):
    v = int(input('введите n раз значения монет 0 или 1 через enter'))
    if v == 1:
        k += 1
print('минимальное количество монет, которое нужно перевернуть, равно: ')
print(k if k < n / 2 else n - k)
