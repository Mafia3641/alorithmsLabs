def MOD(a, b):
    """
    Вычисляет остаток от деления a на b с неотрицательным результатом
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    
    # Для отрицательных чисел корректируем результат
    sign = 1
    if a < 0:
        a = -a
        sign = -1
    
    # Основной алгоритм для неотрицательных чисел
    if a < b:
        remainder = a
    else:
        temp = b
        while temp <= a:
            temp <<= 1
        temp >>= 1
        
        remainder = a
        while temp >= b:
            if remainder >= temp:
                remainder -= temp
            temp >>= 1
    
    # Корректировка для отрицательных чисел
    if sign == -1:
        remainder = b - remainder if remainder != 0 else 0
    
    return remainder

def polinom_calculator(coeffs, x, mod):
    """
    Рекурсивно вычисляет значение полинома по схеме Горнера
    coeffs: коэффициенты от СТАРШЕЙ степени к МЛАДШЕЙ
    x: значение переменной
    mod: модуль (None если не нужно применять)
    """
    senior_stand = len(coeffs) - 1
    coeffs[0] * x 
    if senior_stand == 1:
        return coeffs[0] * x + coeffs[1]
    current_step = polinom_calculator(coeffs[:-1], x, mod)
    tail = coeffs[-1]
    # print(f"{x} * ({current_step}) + {tail}")
    return MOD(x * current_step + tail, mod)
    

def main():
    degree, x_count, mod = list(map(int, input().split()))
    coeffs = []
    args = []
    for _ in range(degree + 1):
        coeffs.append(int(input()))
    for _ in range(x_count):
        args.append(int(input()))
    print("____________________________________________")
    for x in args:
        print(polinom_calculator(coeffs, x, mod))



if __name__ == '__main__':\
    main()
# x2 + 5x + 4 = x(x+5) + 4
# x5 = 

# Схема Горнера:
# ax2 + bx + c == x * (ax + b) + c

# ax4 + bx3 + cx2 + dx + e == x * (ax3 + bx2 + cx + d) + e ==
# == x * (x * (ax2 + bx + c) + d) + e == 
# == x * (x * (x * (ax + b) + c) + d) + e
