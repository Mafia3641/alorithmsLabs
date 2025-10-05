def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def andrews_monotone_chain(points):
    # 1. Сортируем точки
    points = sorted(points, key=lambda p: (p[0], p[1]))
    
    # 2. Строим верхнюю оболочку
    upper = []
    for p in points:
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    # 3. Строим нижнюю оболочку  
    lower = []
    for p in reversed(points):
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    # 4. Объединяем (убираем дубликаты крайних точек)
    return upper[:-1] + lower[:-1]

arr = [[1, 1], [1, 2], [1, 3], [2, 4], [2, 6], [3, 1], [3, 3], [3, 9]]
print(andrews_monotone_chain(arr))