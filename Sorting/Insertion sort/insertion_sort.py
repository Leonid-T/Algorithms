'''
Сортировка вставками удобна для сортировки коротких последовательностей. Данный
метод заключается в том, что каждый последующий элемент вставляется в
правильное место в отсортированную часть массива.
'''


def insertion_sort(A, reverse=False):
    if reverse:
        compare = lambda x, y: x < y
    else:
        compare = lambda x, y: x > y
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and compare(A[i], key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key


def main():
    A = [31, 41, 59, 26, 41, 58]
    insertion_sort(A)
    print(A)


if __name__ == '__main__':
    main()
