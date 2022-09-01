def is_sum_of_two(x, A):
    d = {}
    for i in range(len(A)):
        d[A[i]] = i
    for i in range(len(A)):
        if d.get(x - A[i]) and d.get(x - A[i]) != i:
            return True
    return False


def main():
    A = [3, 4, 8, 4, 45, 23, 5, 7, 11, 10]
    x = 17
    print(is_sum_of_two(x, A))


if __name__ == '__main__':
    main()
