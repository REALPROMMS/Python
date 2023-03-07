# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

import random

lenght_mass = int(input("Задайте длинну журнала с оценками: "))
random_mass = [random.randint(1, 5) for _ in range(lenght_mass)]
print(random_mass)

i = 0

while i < len(random_mass):
    if random_mass[i] == 4 or random_mass[i] == 5:
  			random_mass[i] = 1
i += 1
print(random_mass)
    
