from random import randint

random_number = randint(100, 999)
print(random_number)

sum = int(str(random_number)[0]) + int(str(random_number)[1]) + int(str(random_number)[2])
print(f"Сумма каждого эелмента числа {random_number}, равняется = {sum}")


# второй вариант

# random_number = int(input("Введите любое трёхзначное число: "))
# print(random_number)

# sum = int(str(random_number)[0]) + int(str(random_number)[1]) + int(str(random_number)[2])

# print(f"Сумма каждого эелмента числа {random_number}, равняется = {sum}")