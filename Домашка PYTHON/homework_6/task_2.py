# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

number = int(input("Введите колличество элементов в массиве: ")) 
min_range = int(input("Введите минимальное число диапазона: ")) 
max_range = int(input("Введите максимальное число диапазона: ")) 

random_mass = [random.randint(-10, 10) for _ in range (number)]
print(random_mass)

new_mass = []

for i in range(len(random_mass)):
    if random_mass[i] >= min_range and random_mass[i] <= max_range:
   #  if min_range <= random_mass[i] <= max_range:
      new_mass.append(i)
        
print(new_mass)


