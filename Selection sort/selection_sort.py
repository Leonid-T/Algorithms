def selection_sort(A, reverse=False):
    if reverse:
        compare = lambda x, y: x > y
    else:
        compare = lambda x, y: x < y
    for i in range(len(A)-1):
        k = i
        for j in range(i, len(A)):
            if compare(A[j], A[k]):
                k = j
        A[i], A[k] = A[k], A[i]


def main():
    A = [31, 41, 59, 26, 41, 58]
    selection_sort(A)
    print(A)


if __name__ == '__main__':
    main()
