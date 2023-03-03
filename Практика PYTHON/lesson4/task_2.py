string = 'слово слово слово цифра строка строка'

list_string = string.lower().split()
print(list_string)

catalog = {}

for word in list_string:
    catalog[word] = catalog.get(word, 0) + 1

count = 0
for word in catalog:
    count += 1
print(count)


key = catalog.keys()
print(len(key))

print(len(set(list_string)))