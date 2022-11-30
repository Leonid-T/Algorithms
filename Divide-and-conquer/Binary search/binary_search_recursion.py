'''
Рекурсивная реализация бинарного поиска.
Бинарный поиск используется для поиска индекса элемента в отсортированной
последовательности. При этом искомый элемент сравнивается с элементом в
середине последовательности, и дальнейший поиск продолжается в соответствующей
части массива.
'''


def binary_search(A, v, begin=0, end=None):
    if end is None:
        end = len(A)-1
    index = None
    middle = (begin + end) // 2
    if begin < end:
        if v < A[middle]:
            index = binary_search(A, v, begin, middle)
        elif v > A[middle]:
            index = binary_search(A, v, middle+1, end)
        else:
            index = middle
    return index


def main():
    A = [26, 31, 41, 41, 58, 59]
    v = 31
    index = binary_search(A, v)
    print(index)


if __name__ == '__main__':
    main()
