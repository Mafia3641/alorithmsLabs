k = int(input())

mas = []

for i in range(4):
    row = input()

    for j in row:
        if j == '.':
            mas.append(0)
        else:
            mas.append(int(j))

counters = [0] * 10

for i in mas:
    counters[i] += 1

result = 0

for i in range(1, 10):
    if 0 < counters[i] <= k * 2:
        result += 1

print(result)
