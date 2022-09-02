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


def min_max(A):
    n = len(A)
    if n > 0:
        if n % 2:
            minimum, maximum = A[0], A[0]
            start = 1
        elif A[0] < A[1]:
            minimum, maximum = A[0], A[1]
            start = 2
        else:
            minimum, maximum = A[1], A[0]
            start = 2
        for i in range(start, n-1, 2):
            if A[i] < A[i+1]:
                i_min, i_max = i, i+1
            else:
                i_min, i_max = i+1, i
            if A[i_min] < minimum:
                minimum = A[i_min]
            if A[i_max] > maximum:
                maximum = A[i_max]
        return minimum, maximum


def bucket_sort(A):
    n = len(A)
    min_, max_ = min_max(A)
    B = [[] for _ in range(n+1)]
    for i in range(n):
        B[n*(A[i]-min_)//(max_-min_)].append(A[i])
    for i in range(n+1):
        insertion_sort_binary_modification(B[i])
    A.clear()
    for i in range(n+1):
        A.extend(B[i])


def main():
    A = [17, 27, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    bucket_sort(A)
    print(A)


if __name__ == '__main__':
    main()
