
def add_pos(num1, num2):
    'Складывает два неотрицательных числа'

    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1
    res = []

    while i>=0 or j>=0 or carry:
        s1 = int(num1[i]) if i >= 0 else 0
        s2 = int(num2[j]) if j >= 0 else 0
        total = s1 + s2 + carry
        carry = total // 10
        res.append(str(total%10))
        i -= 1
        j -= 1
    return ''.join(res[::-1])

def subtract_pos(num1, num2):
    'Вычитает 2 неотрицательных числа'

    if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
        sign = '-'
        num1, num2 = num2, num1
    else:
        sign = ''
    
    borrow = 0
    i = len(num1) - 1
    j = len(num2) - 1
    res = []
    
    while i >= 0:
        s1 = int(num1[i])
        s2 = int(num2[j]) if j >= 0 else 0
        diff = s1 - s2 - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else: 
            borrow = 0
        res.append(str(diff))
        i-=1
        j-=1
    res = ''.join(res)[::-1].lstrip('0') or '0'
    return sign+res

def normalized(s):
    'Обработка входящего числа'

    if s.startswith('-'):
        s = s[1:]
        s = s.lstrip('0') or '0'
        if s == '0':
            return '0'
        else:
            return '-' + s
    else:
        s = s.lstrip('0') or '0'
        return s

def add_signed(num1, num2):
    'Складывает два числа (с обработкой отрицательных)'

    a = normalized(num1)
    b = normalized(num2)
    if a.startswith('-'):
        if b.startswith('-'):
            return '-'+add_pos(a[1:], b[1:])
        else:
            return subtract_pos(b, a[1:])
    else:
        if b.startswith('-'):
            return subtract_pos(a, b[1:])
        else:
            return add_pos(a, b)

def subtract_signed(num1, num2):
    'Вычитает два числа (с обработкой отрицательных)'
    
    a = normalized(num1)
    b = normalized(num2)
    if a.startswith('-'):
        if b.startswith('-'):
            return subtract_pos(b[1:], a[1:])
        else:
            return '-' + add_pos(a[1:], b)
    else:
        if b.startswith('-'):
            return add_pos(a, b[1:])
        else:
            return subtract_pos(a, b)


def main():
    num1 = input()
    operation = input()
    num2 = input()

    if operation == '+':
        print(add_signed(num1, num2))
    elif operation == '-':
        print(subtract_signed(num1, num2))

if __name__ == '__main__':
    main()