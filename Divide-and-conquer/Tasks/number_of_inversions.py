'''
Процедура number_of_inversions(A) подсчитывает число инверсий в массиве A.
Для решения задачи используется модифицированная версия сортировки слиянием.
Инверсией называется пара (i, j) в исходном массиве такая, что i < j и
A[i] > A[j].
'''


from collections import deque


def number_of_inversions(A):
    counter = 0
    return _merge_sort(A, 0, len(A)-1, counter)


def _merge_sort(A, p, r, counter):
    if p < r:
        q = (p + r) // 2
        counter = _merge_sort(A, p, q, counter)
        counter = _merge_sort(A, q+1, r, counter)
        counter = _merge(A, p, q, r, counter)
    return counter


def _merge(A, p, q, r, counter):
    A1 = deque(A[p:q+1])
    A2 = deque(A[q+1:r+1])
    i = p
    while len(A1) > 0 and len(A2) > 0:
        if A1[0] <= A2[0]:
            A[i] = A1.popleft()
        else:
            counter += len(A1)
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
    return counter


def main():
    A = [2, 3, 8, 6, 1]
    print(number_of_inversions(A))


if __name__ == '__main__':
    main()
