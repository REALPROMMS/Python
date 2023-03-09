# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

number = int(input("Введите любое число: "))
step = int(input("Введите шаг чисел: "))
total_number = int(input("Введите сколько всего будет элементов: "))

my_list = []
for i in range(total_number):
    my_list.append(number + i * step)
   #  summa = number + i * step
   #  my_list.append(summa)
print(my_list)