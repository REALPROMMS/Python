per_day = int(input('Введите сколько машина проезжает за день: '))
total_distance = int(input('Введите сколько машина должна проезать всего: '))

days = (total_distance + per_day -1)//per_day

print(f'На маршрут в {total_distance} км машина потратит {days} дня')