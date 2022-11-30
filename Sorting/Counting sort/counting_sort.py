'''
В сортировке подсчетом предполагается, что каждый элемент - целое положительное
число не больше константы k. Для каждого элемента массива x подсчитывается
количество элемнтов, которые меньше x. На основе этой информации определяется
место, которое должен занимать каждый из элементов.
'''


def counting_sort(A):
    n = len(A)
    if n > 0 and min(A) >= 0:
        k = max(A) + 1
        C = [0 for _ in range(k)]
        B = [0 for _ in range(n)]
        for i in range(n):
            C[A[i]] += 1
        for i in range(1, k):
            C[i] += C[i-1]
        for i in range(-1, -n-1, -1):
            B[C[A[i]]-1] = A[i]
            C[A[i]] -= 1
        for i in range(n):
            A[i] = B[i]


def main():
    A = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    counting_sort(A)
    print(A)


if __name__ == '__main__':
    main()
