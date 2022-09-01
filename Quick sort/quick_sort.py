from random import randint


def quick_sort(A, reverse=False):
    if reverse:
        compare = lambda x, y: x >= y
    else:
        compare = lambda x, y: x <= y
    return _quick_sort(A, 0, len(A)-1, compare)


def _quick_sort(A, p, r, compare):
    if p < r:
        q = randomized_partion(A, p, r, compare)
        _quick_sort(A, p, q-1, compare)
        _quick_sort(A, q+1, r, compare)


def randomized_partion(A, p, r, compare):
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partion(A, p, r, compare)


def partion(A, p, r, compare):
    x = A[r]
    i = p - 1
    count_equal = 0
    for j in range(p, r):
        if compare(A[j], x):
            if A[j] == x:
                count_equal += 1
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    if count_equal == r - p:
        return (p + r) // 2
    else:
        return i + 1


def main():
    A = [13, 19, 9, 5, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    quick_sort(A)
    print(A)


if __name__ == '__main__':
    main()
