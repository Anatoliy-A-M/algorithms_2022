"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

def func_3():
    return max(array, key=lambda i: array.count(i))

if __name__ == '__main__':
    print(func_1())
    print(func_2())
    print(func_3())

    print(f'Замер функции func_1: {timeit("func_1()", number=10000, globals=globals())}')  # 0.01
    print(f'Замер функции func_2: {timeit("func_2()", number=10000, globals=globals())}')  # 0.014
    print(f'Замер функции func_3: {timeit("func_2()", number=10000, globals=globals())}')  # 0.013

# Задачу удалось написать в одну строку, но к сожалению скорость улучшить не получилось.
