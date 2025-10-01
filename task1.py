mas = [0, 1, 2, 3, 4, 5, 0, 1, 2, 0]
len = 10
counter1 = 0
counter2 = 0
result = []

for i in mas:
    result.append(i)


for cur1 in range(0, len - 1):
    cur2 = len - 1 - cur1

    if mas[cur1] == 0:
        counter1 = 0
    else:
        counter1 += 1

    if mas[cur2] == 0:
        counter2 = 0
    else:
        counter2 += 1

    if cur1 == cur2:
        result[cur1] = min(counter1, counter2)

    if cur2 < cur1:
        result[cur2] = min(counter2, result[cur2])
        result[cur1] = min(counter1, result[cur1])
    else:
        result[cur1] = counter1
        result[cur2] = counter2

print(mas)
print(result)
