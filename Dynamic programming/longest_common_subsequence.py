'''
Динамическое программирование.
Задача:
Найти наидлиннейшую общую подпоследовательность двух последовательностей
'''


def lcs_lenght(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
    return lcs(c, X, m, n, '')


def lcs(c, X, i, j, s):
    if i == 0 or j == 0:
        return s
    i_next, j_next = max_3(c, i, j)
    if i_next < i and j_next < j:
        s = lcs(c, X, i_next, j_next, s)
        s += str(X[i-1])
    else:
        s = lcs(c, X, i_next, j_next, s)
    return s


def max_3(c, i, j):
    if c[i-1][j] >= c[i][j-1]:
        i_next = i - 1
        j_next = j
    else:
        i_next = i
        j_next = j - 1
    if c[i-1][j-1] >= c[i_next][j_next]:
        i_next = i - 1
        j_next = j - 1
    return i_next, j_next


def main():
    X1 = 'ABCBDAB'
    Y1 = 'BDCABA'
    print(lcs_lenght(X1, Y1))
    X2 = [1, 0, 0, 1, 0, 1, 0, 1]
    Y2 = [0, 1, 0, 1, 1, 0, 1, 1, 0]
    print(lcs_lenght(X2, Y2))


if __name__ == '__main__':
    main()
