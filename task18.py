from quick_sort import quick_sort
import time


def time_to_pos(time: str) -> int:
    """
    Принимает значение времени в формате
    hh:mm
    и возвращает позицию в списке graph
    """
    hour, minute = map(int, time.split(':'))
    pos = hour * 60 + minute
    return pos

def pos_to_time(pos: int) -> str:
    """
    Принимает позицию элемента списка graph
    возвращает точное время этого элемента
    """
    min = pos % 60
    hour = pos // 60
    if min < 10:
        min = f'0{min}'
    return f'{hour}:{min}'

def add_to_graph(start, end, graph):
    for i in range(start, end+1):
        graph[i] += 1

def main():
    data = []
    graph = [0] * 60 * 24

    count = int(input())
    for i in range(count):
        input_ = input()
        e_time, l_time = input_.split()
        data.append([e_time, l_time])

    curr_time = time.time()
    for p in data:
        e_time = time_to_pos(p[0])
        l_time = time_to_pos(p[1])
        add_to_graph(e_time, l_time, graph)
    print(f"Time elapsed: {time.time() - curr_time}")
    
    return quick_sort(graph)[-1]

if __name__ == '__main__':
    print(main())