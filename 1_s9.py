# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5  Output: 120

n = 5
factorial = 1
i = 1
while i <= 5:
    factorial *= i
    i += 1
print(factorial)

