
def simple_multipy(num1, num2):
    higher = max(num1, num2)
    lower = min(num1, num2)
    res = 0
    for i in range(lower):
        res += higher
    return res

def multiply(num1, num2):
    higher = str(max(num1, num2))
    lower = str(min(num1, num2))
    res = []
    remainder = 0
    for i in lower:
        for j in higher:
            curr_step = simple_multipy(int(i), int(j))
            if curr_step > 9:
                remainder = curr_step // 10
                whole_part = curr_step % 10
            else:
                remainder = 0
                whole_part = curr_step
            res.append(whole_part)
    """НАДО ЗАКОНЧИТЬ (или переписать)"""

         