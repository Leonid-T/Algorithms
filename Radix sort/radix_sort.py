def counting_sort_for_radix_sort(A, d, k=10):
    n = len(A)
    C = [0 for _ in range(k)]
    B = [0 for i in range(n)]
    for i in range(n):
        C[radix(A[i], d)] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(-1, -n-1, -1):
        B[C[radix(A[i], d)]-1] = A[i]
        C[radix(A[i], d)] -= 1
    for i in range(n):
        A[i] = B[i]


def radix(x, d, k=10):
    return (x // k ** d) % k


def radix_sort(A):
    n = len(A)
    if n > 0 and min(A) >= 0:
        d = len(str(max(A)))
        for i in range(d):
            counting_sort_for_radix_sort(A, i)


def main():
    A = [329, 457, 657, 839, 436, 720, 355]
    radix_sort(A)
    print(A)


if __name__ == '__main__':
    main()
