import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left, right = [], []

    for elem in arr[:-1]:
        if elem <= pivot:
            left.append(elem)
        else:
            right.append(elem)
    
    return quick_sort(left) + [pivot] + quick_sort(right)


def partition(arr, left, right):
    pivot = arr[right]
    left_index = left - 1
    for j in range(left, right):    
        if arr[j] <= pivot:
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


def hoare_sort_part(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        
        j -= 1
        while arr[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        arr[i], arr[j] = arr[j], arr[i]

def hoare_sort(arr, left=0, right=None):
    if right == None:
        right = len(arr) - 1
    if left<right:
        pivot_index = hoare_sort_part(arr, left, right)
        hoare_sort(arr, left, pivot_index)
        hoare_sort(arr, pivot_index+1, right)
    return arr

def main():
    arr1 = [random.randint(0, 100_000_000) for i in range(1_000_000)]
    arr2 = [random.randint(0, 100_000_000) for i in range(1_000_000)]
    arr3 = [random.randint(0, 100_000_000) for i in range(1_000_000)]

    print("quick_sort: тест времени 1 млн элементов за x секунд:")
    curr_time = time.time()
    quick_sort_test = quick_sort(arr1)
    end_time = time.time()
    elapsed_time = end_time - curr_time
    print(f"Выполнено за {elapsed_time} секунд")


    print("in_place_quick_sort: тест времени 1 млн элементов за x секунд:")
    curr_time = time.time()
    in_place_sort_test = in_place_sort(arr2, 0, 1_000_000-1)
    end_time = time.time()
    elapsed_time = end_time - curr_time
    print(f"Выполнено за {elapsed_time} секунд")


    print("haore_sort: тест времени 1 млн элементов за x секунд:")
    curr_time = time.time()
    hoare_sort_test = hoare_sort(arr3, 0, len(arr3)-1)
    end_time = time.time()
    elapsed_time = end_time - curr_time
    print(f"Выполнено за {elapsed_time} секунд")