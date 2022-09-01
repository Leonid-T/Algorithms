from collections import deque


def merge_sort(A, reverse=False):
    if reverse:
        compare = lambda x, y: x > y
    else:
        compare = lambda x, y: x < y
    _merge_sort(A, 0, len(A)-1, compare)


def _merge_sort(A, p, r, compare):
    if p < r:
        q = (p + r) // 2
        _merge_sort(A, p, q, compare)
        _merge_sort(A, q+1, r, compare)
        _merge(A, p, q, r, compare)


def _merge(A, p, q, r, compare):
    A1 = deque(A[p:q+1])
    A2 = deque(A[q+1:r+1])
    i = p
    while len(A1) > 0 and len(A2) > 0:
        if compare(A1[0], A2[0]):
            A[i] = A1.popleft()
        else:
            A[i] = A2.popleft()
        i += 1
    if len(A1) != 0:
        while len(A1) != 0:
            A[i] = A1.popleft()
            i += 1
    elif len(A2) != 0:
        while len(A2) != 0:
            A[i] = A2.popleft()
            i += 1


def main():
    A = [31, 41, 59, 26, 41, 58]
    merge_sort(A)
    print(A)


if __name__ == '__main__':
    main()
