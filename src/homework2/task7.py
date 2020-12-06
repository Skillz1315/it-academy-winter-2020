""" Напишите программу, которая считывает два натуральных числа a и b
    (гарантируется, что a < b),
    после чего для всех чисел от a до b выводит:
    “Fizz”, если это число делится на 3;
    “Buzz”, если это число делится на 5;
    “FizzBuzz”, если выполнены оба предыдущих условия;
    само это число в остальных случаях.
"""


num = int(input())
num1 = int(input())
for x in range(num, num1 + 1):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)


""" Напишите программу, которая по введённому натуральному числу определит,
    является ли год с данным номером високосным и
    выведет количество дней в нём (365 или 366).
    Подсказка: в соответствии с григорианским календарем
    год является високосным
    если его номер кратен 4, но не кратен 100, а также если он кратен 400
"""


year = int(input())
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print(365)
else:
    print(366)
