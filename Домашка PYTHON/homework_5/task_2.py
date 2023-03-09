# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

number_one = int(input("Введите первое любое число: "))
number_two = int(input("Введите второе любое число: "))

def sum(number_one, number_two):
    if number_two == 0:
        return number_one
    return 1 + sum(number_one, number_two - 1)

print(sum(number_one, number_two))