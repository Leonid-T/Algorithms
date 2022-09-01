def insertion_sort_binary_modification(A, reverse=False):
    if reverse:
        compare = lambda x, y: x > y
    else:
        compare = lambda x, y: x < y
    for j in range(1, len(A)):
        key = A[j]
        index = binary_search(A, key, compare, 0, j-1)
        if j != index:
            A.pop(j)
            A.insert(index, key)
    return A


def binary_search(A, v, compare, begin=0, end=None):
    if end is None:
        end = len(A)-1
    middle = (begin + end) // 2
    if begin < end:
        if compare(v, A[middle]):
            index = binary_search(A, v, compare, begin, middle-1)
        elif compare(A[middle], v):
            index = binary_search(A, v, compare, middle+1, end)
        else:
            index = middle
    else:
        if compare(v, A[middle]):
            index = middle
        else:
            index = middle + 1
    return index


def main():
    A = [31, 41, 59, 26, 41, 58]
    insertion_sort_binary_modification(A)
    print(A)


if __name__ == '__main__':
    main()
