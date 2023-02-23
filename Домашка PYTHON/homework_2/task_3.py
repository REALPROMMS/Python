# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

random_number = int(input("Введите любое 2х значное число: "))
degree = 1
while degree <= random_number:
    print(degree,end = ' ')
    degree = degree * 2
