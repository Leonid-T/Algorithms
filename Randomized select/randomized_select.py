from random import randint


def randomized_select(A, i, p=0, r=None):
    if r is None:
        r = len(A)-1
    A = A.copy()
    return _randomized_select(A, i, p, r)


def _randomized_select(A, i, p, r):
    if p == r:
        return A[p]
    q = randomized_partion(A, p, r)
    k = q - p
    if i == k:
        return A[q]
    elif i < k:
        return _randomized_select(A, i, p, q-1)
    else:
        return _randomized_select(A, i-k-1, q+1, r)


def randomized_partion(A, p, r):
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partion(A, p, r)


def partion(A, p, r):
    x = A[r]
    i = p - 1
    count_equal = 0
    for j in range(p, r):
        if A[j] <= x:
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
    print(randomized_select(A, 3))


if __name__ == '__main__':
    main()
