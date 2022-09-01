def left(i):
    return 2*(i + 1) - 1


def right(i):
    return 2*(i + 1)


def heapify(A, i, heap_size, compare):
    l = left(i)
    r = right(i)
    if l <= heap_size-1 and compare(A[l], A[i]):
        largest = l
    else:
        largest = i
    if r <= heap_size-1 and compare(A[r], A[largest]):
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest, heap_size, compare)


def build_heap(A, compare):
    heap_size = len(A)
    for i in range(len(A)//2-1, -1, -1):
        heapify(A, i, heap_size, compare)


def heap_sort(A, reverse=False):
    if reverse:
        compare = lambda x, y: x < y
    else:
        compare = lambda x, y: x > y
    build_heap(A, compare)
    heap_size = len(A)
    for i in range(-1, -len(A)-1, -1):
        A[i], A[0] = A[0], A[i]
        heap_size -= 1
        heapify(A, 0, heap_size, compare)


def main():
    A = [17, 27, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    heap_sort(A)
    print(A)


if __name__ == '__main__':
    main()
