'''
Процедура permutation(A, k) возвращает случайный набор k чисел из множества A.
'''


from random import randint


def permutation(A, k):
    A = A.copy()
    n = len(A)
    if k <= n:
        for i in range(k):
            m = randint(i, n-1)
            A[i], A[m] = A[m], A[i]
        return A[:k]


def main():
    N = 10
    A = [i+1 for i in range(N)]
    B = permutation(A, 5)
    print(B)


if __name__ == '__main__':
    main()
