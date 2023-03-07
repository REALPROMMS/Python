



number = int(input("Enter number: "))

for i in range(1, number):
    for j in range(i, number):
        temp_sum_1 = 0
        temp_sum_2 = 0
        for k in range(1, i):
            if i % k == 0:
                temp_sum_1 += k
        for k in range(1, j):
            if j % k == 0:
                temp_sum_2 += k
        if temp_sum_1 == j and temp_sum_2 == i and i != j:
            print(f"{i} and {j}")