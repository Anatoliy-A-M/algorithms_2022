"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""
def row_summ(n, num = 1):
    if n == 0:
        return 0
    return num + row_summ(n - 1, num * -0.5)

n = int(input('Введите число: '))
print(f'Количество элементов - {n}, их сумма - {row_summ(n)}.')
