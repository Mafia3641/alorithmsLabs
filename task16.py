from quick_sort import hoare_sort
import time

def get_value(current, M, L):
    return (current * M) % L

def get_array(input_):
    N, K, M, L = map(int, input_.split())
    arr = [K]
    current = K
    time_now = time.time()
    for i in range(0, N-1):
        current = get_value(current, M, L)
        arr.append(current)
    else:
        time.sleep(0.1)
        print(time.time()-time_now-0.1)
    
    sorted_arr = hoare_sort(arr)
    total = sum(sorted_arr[i] for i in range(0, len(sorted_arr), 2)) % L
    return total

print(get_array('5 7 13 100'))