"""
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


list_ = [1, 1, 1, 2, 2, 2, 2, ]
print(sum(list_.count(x) - 1 for x in list_) // 2)

