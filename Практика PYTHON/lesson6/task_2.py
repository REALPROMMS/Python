# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

import random
length_mass_1 = int(input("Введите длинну массива: "))
random_mass_1 = [random.randomint(1, 10) for _ in range (length_mass_1)]
print(random_mass_1)
count = 0
for i in range(-1, length_mass_1-1):
    if random_mass_1[i-1] < random_mass_1[i] and random_mass_1[i+1] < random_mass_1[i]:
	# if random_mass_1[i-1] < random_mass_1[i] > random_mass_1[i+1]:
      count += 1
        
print(count)