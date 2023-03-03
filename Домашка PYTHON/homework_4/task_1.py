# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


import random

number_one_set = set(random.randint(1, 10) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(number_one_set)
number_two_set = set(random.randint(1, 10) for i in range(int(input('Введите кол-во элементов второго множества: '))))
print(number_two_set)
sorted_set = sorted(number_one_set.intersection(number_two_set))
print(sorted_set)