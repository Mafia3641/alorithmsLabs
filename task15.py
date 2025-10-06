
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

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def andrews_monotone_chain(arr):
    points = quick_sort(arr)

    upper = []
    for p in points:
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    lower = []
    for p in reversed(points):
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    # Объединяем (убираем дубликаты крайних точек)
    return upper[:-1] + lower[:-1]

def calculate_perimeter(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5
arr = [[2, 1], [2, 2], [2, 3], [3, 2], [1, 2]]

points = andrews_monotone_chain(arr)
perim = 0
n = len(points)
for i in range(n):
    # Используем модуль для замыкания многоугольника
    perim += calculate_perimeter(points[i], points[(i+1) % n])

print(f"{perim:.2f}")