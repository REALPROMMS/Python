import random
my_list = [random.randint(1,5) for _ in range(10)]
print(my_list)

my_dict = {}

for i in my_list:
	my_dict[i] = my_dict.get(i, 0) + 1
# print(my_dict)
	print(i if my_dict.get(i) == 1 else f'{i}_{my_dict.get(i) -1}', end=' ')

# print('\n' + f'{my_dict}')
