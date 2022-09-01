def counting_sort(A):
    n = len(A)
    if n > 0 and min(A) >= 0:
        C = []
        B = []
        k = max(A) + 1
        for _ in range(k):
            C.append(0)
        for i in range(n):
            C[A[i]] += 1
            B.append(0)
        for i in range(1, k):
            C[i] += C[i-1]
        for i in range(-1, -n-1, -1):
            B[C[A[i]]-1] = A[i]
            C[A[i]] -= 1
        for i in range(n):
            A[i] = B[i]

def main():
    A = [6, 0, 2, -1, 1, 3, 4, 6, 1, 3, 2]
    counting_sort(A)
    print(A)

if __name__ == '__main__':
    main()