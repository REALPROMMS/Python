import random


my_list = [random.randint(1, 10) for _ in range(10)]
print(my_list)

my_dict = {}

for item in my_list:
    my_dict[item] = my_dict.get(item, 0) + 1

print(my_dict)

new_list = []

for key, value in my_dict.items():
    if value == 1:
        new_list.append(key)
        
print(new_list)
	


"""
import random


my_list = [random.randint(1, 10) for _ in range(10)]
print(my_list)

new_list = []

for item in my_list:
	if my_list.count(item) == 1:
		new_list.append(item)
        
print(new_list)


"""