"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
# а)

import time

def profiler(func):
    def wrapper(*args):
        now = time.time()
        result = func(*args)
        print((time.time() - now) * 10000)
        return result

    return wrapper


@profiler
def list_generator(n):  # O(n)
    return [i for i in range(0, n)]  # O(n)


@profiler
def dict_generator(n):  # O(n)
    return {i: None for i in range(0, n)}  # O(n)


print('a:')
print('Списки:')
lst1 = list_generator(10000000)
lst2 = list_generator(10000000)
lst3 = list_generator(10000000)

print('Словари:')
dct1 = dict_generator(10000000)
dct2 = dict_generator(10000000)
dct3 = dict_generator(10000000)


# Из-за хэширования ключей словарь заполняется дольше

# b)

@profiler
def get_list_item(lst: list, el):  # O(n)
    for itm in lst:  # O(n)
        if itm == el:  # O(1)
            return itm  # O(1)


@profiler
def get_dict_item(dct: dict, el):  # O(1)
    return dct[el]  # O(1)


print('b:')
list_element = get_list_item(lst1, 1000000)
dict_element = get_dict_item(dct1, 1000000)

# Время поиска элемента в списке линейно зависят от n, а в словаре константно.
# Поиск в списке требует времени, а в словаре мгновенно

# c)

@profiler
def del_list_item(lst: list, el):  # O(n)
    lst.remove(el)  # O(n)


@profiler
def del_dict_item(dct: dict, el):  # O(1)
    del dct[el]  # O(1)


print('c:')
del_list_item(lst1, 1000000)
del_dict_item(dct1, 1000000)


# Время поиска элемента в списке линейно зависят от n, а в словаре константно.
# Поиск в списке требует времени, а в словаре мгновенно

