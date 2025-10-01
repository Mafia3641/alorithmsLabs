
def get_similar_count(arr1, arr2):
    res = 0
    i, j = 0, 0
    counter = 0
    while i < len(arr1) and j < len(arr2):
        counter += 1
        pos1 = arr1[i]
        pos2 = arr2[j]
        if pos1 == pos2:
            res += 1
            i+=1
            j+=1
        if pos1 > pos2:
            j+=1
        else:
            i+=1
    return res

def main():
    size_1, size_2 = map(int, input().split())
    array_1 = []
    array_2 = []
    for _ in range(size_1):
        array_1.append(int(input()))
    for _ in range(size_2):
        array_2.append(int(input()))
    print(get_similar_count(array_1, array_2))


if __name__ == "__main__":
    main()
