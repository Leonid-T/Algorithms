'''
Реализация бинарного поиска без рекурсии.
Бинарный поиск используется для поиска индекса элемента в отсортированной
последовательности. При этом искомый элемент сравнивается с элементом в
середине последовательности, и дальнейший поиск продолжается в соответствующей
части массива.
'''


def binary_search(A, v, start=0, end=None):
    if end is None:
        end = len(A)
        
    index = None
    
    while start < end:
        middle = (start + end) // 2
        
        if v < A[middle]:
            end = middle
        elif v > A[middle]:
            start = middle + 1
        else:
            index = middle
            break
    return index


def main():
    A = [26, 31, 41, 41, 58, 59, 70]
    v = 31
    index = binary_search(A, v)
    print(index)


if __name__ == '__main__':
    main()
