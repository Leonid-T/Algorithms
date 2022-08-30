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
    A = []
    N = 10
    for i in range(N):
       A.append(i+1)
    B = permutation(A, 5)
    print(B)

if __name__ == '__main__':
    main()