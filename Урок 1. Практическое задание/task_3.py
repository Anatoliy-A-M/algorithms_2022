"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

# 1 способ
user_list = sorted(list(companies.values()), reverse=True)[:3]                     # O(n*log n)
for el in user_list:                                                               # O(1)
    for k, v in companies.items():                                                   # O(n)
        if v == el:
            print(k, ':', v)                                                         # O(1)


# Сложность - O(n*log n)

# 2 способ
user_list = sorted(companies, key=companies.get, reverse=True)[:3]    # O(n*log n)
for i in user_list:                                                   # O(n)
    print(i, ':', companies.get(i))                                          # O(1)

    
# Сложность -  O (n *log n)
