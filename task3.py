
# 1 2 6 8 7 3 4 5 1 0 4 1 6 2 3 9 0


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    arr1 = merge_sort(arr[:mid])
    arr2 = merge_sort(arr[mid:])
    return binary_sort(arr1, arr2)

def binary_sort(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i == len(left):
        result.extend(right[j:])
    if j == len(right):
        result.extend(left[i:])
    return result

def find_unique():
    mas1, mas2 = input().split('0')[:-1]
    mas1 = list(map(int, mas1.split()))
    mas2 = list(map(int, mas2.split()))
    sorted_left = merge_sort(mas1)
    sorted_right = merge_sort(mas2)
    result = []
    i, j = 0, 0
    len_l, len_r = len(sorted_left), len(sorted_right)
    while i < len_l and j < len_r:
        sorter_left_i = sorted_left[i]
        sorted_right_j = sorted_right[j]
        if sorter_left_i == sorted_right_j:
            i += 1
            j += 1
            try:
                result.pop(result.index(sorter_left_i))
            except:
                continue
        if sorter_left_i < sorted_right_j:
            result.append(sorter_left_i)
            i += 1
        else:
            result.append(sorted_right_j)
            j+=1
    
    if i == len_l:
        result.extend(sorted_right[j:])
    else:
        result.extend(sorted_left[i:])

    return result


if __name__ == "__main__":
    print(find_unique())