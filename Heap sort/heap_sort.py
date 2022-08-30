def parent(i):
    return i // 2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    if l <= heap_size-1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size-1 and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)

def build_max_heap(A):
    heap_size = len(A)
    for i in range(len(A)//2-1, -1, -1):
        max_heapify(A, i, heap_size)

def heap_sort(A):
    build_max_heap(A)
    heap_size = len(A)
    for i in range(-1, -len(A)-1, -1):
        A[i], A[0] = A[0], A[i]
        heap_size -= 1
        max_heapify(A, 0, heap_size)

def main():
    A = [17, 27, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    heap_sort(A)
    print(A)

if __name__ == '__main__':
    main()