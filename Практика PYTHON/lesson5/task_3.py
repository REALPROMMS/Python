# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

number = int(input("введите число, для проверки на простоту: "))
i = 2
while i < number:
    if number % 1 == 0 and number % number == 0 and number % i == 0:
        print(f"Число {number} является простым!")
        break
    else:
        print(f"Число {number} не является простым!")
        break
