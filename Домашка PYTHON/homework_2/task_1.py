# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

from random import randint

coin = randint(5, 10)
coin_eagle = 0
coin_tails = 0
count = 0 
print(f"Число монет: {coin}")

for i in range(coin):
	coin_random = randint(0,1)
	print(coin_random)
	if coin_random == 0:
		coin_tails += 1
	elif coin_random == 1:
		coin_eagle += 1

if coin_tails >= coin_eagle:
	print(f"Минимальное количество монет нужно повернуть: {coin_eagle}")
else:
	print(f"Минимальное количество монет нужно повернуть: {coin_tails}")




