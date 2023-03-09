# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

number = int(input("Введите любое число: "))
degree = int(input("Введите степень возведения данно числа: "))

def summa(number, degree):
    if degree == 0:
        return 1
    return number * summa(number, degree - 1)

print(summa(number, degree))