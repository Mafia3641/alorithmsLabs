from task3 import merge_sort


def fast_method(arr):
    sum_1 = 0
    sum_2 = 0
    i = len(arr)
    while i != 0:
        if sum_1 < sum_2:
            sum_1 += arr[-1]
        else:
            sum_2 += arr[-1]
        arr = arr[:-1]
        i -= 1
    return abs(sum_1 - sum_2)

def steady_method(arr):
    S = sum(arr)
    T = S // 2
    max_sum = 0
    dp = [[0, True]]
    for j in range(1, T):
        dp.append([j, False])
    arr = arr[::-1]
    for num in arr:
        for j in range(T, num - 1, -1):
            if dp[j - num][1] == True:
                dp[j][1] = True
    for a, b in dp[::-1]:
        if b == True:
            return S - a - a
    else:
        return None

def main():
    count = int(input())
    arr = list(
            map(
            int, input().split()
            )
        )
    print(steady_method(merge_sort(arr)))

if __name__ == '__main__':
    main()
