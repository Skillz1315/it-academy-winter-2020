"""Даны два списка чисел. Посчитайте, сколько различных чисел
содержится одновременно как в первом списке, так и во втором.
"""


list_1 = [1, 2, 3, 4, 6, ]
list_2 = [1, 7, 2, 2, 3, 3, 4, 4, 5, 5, ]

set_1 = set(list_1) & set(list_2)
print(len(set_1))
