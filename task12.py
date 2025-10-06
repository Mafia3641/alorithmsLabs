def compare(a, b):
    if a[1] > b[1]:
        return True
    if a[1] < b[1]:
        return False
    if a[2] < b[2]:
        return True
    if a[2] > b[2]:
        return False
    return len(a[0]) >= len(b[0])


def partition(arr, left, right):
    pivot = arr[right]
    left_index = left - 1
    for j in range(left, right):    
        if compare(arr[j], pivot):
            left_index += 1
            arr[left_index], arr[j] = arr[j], arr[left_index]
    pivot_index = left_index + 1
    arr[right], arr[pivot_index] = arr[pivot_index], arr[right]
    return pivot_index


def in_place_sort(arr, left, right):
    if left<right:
        pivot_index = partition(arr, left, right)
        in_place_sort(arr, left, pivot_index-1)
        in_place_sort(arr, pivot_index+1, right)
    return arr


def manage(arr):
    for pos, competitor in enumerate(in_place_sort(arr, 0, len(arr) - 1), start=1):
        print(f"На", pos, "месте оказался", competitor[0])


arr = [
    ['alla', 4, 100],
    ['gena', 6, 1000],
    ['gosha', 2, 90],
    ['rita', 2, 90],
    ['Timofey', 4, 80]
]

manage(arr)
