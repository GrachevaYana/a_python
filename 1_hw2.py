# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
number = input('Введите трехзначное число: ')
if len(number)==3:
    print(int(number[0]) +int(number[1])+int(number[2]))
else:
    print('Введено неверное число')

