arr = [64, 34, 25, 12, 22, 11, 30]

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
    
print(quick_sort(arr))

def in_plase_quick_sort(arr):
    middle = len(arr)//2
    pivot = arr[middle]
    left, right = 0, len(arr) - 1
    while left < middle and right > middle:
        print(f"Текущий вид списка: {arr}")
        print(f"Текущий левый элемент: {arr[left]}, Текущий правый элемент: {arr[right]}")
        if arr[left] < pivot:
            if arr[right] > pivot:
                left += 1
                right -= 1
                continue
            else:
                left += 1
                continue
        else:
            if arr[right] > pivot:
                right -= 1
                continue
            else:
                arr[right], arr[left] = arr[left], arr[right]
    else:
        if left < middle:
            arr[left], arr[middle] = arr[middle], arr[left]
        else:
            arr[right], arr[middle] = arr[middle], arr[right]
    return arr

print(in_plase_quick_sort(arr))
