'''
Динамическое программирование.
Задача:
Для заданной последовательности n матриц (A1, A2, ..., An), в которой матрица
A(i+1) i = 0, 1, ..., n имеет размер pi x p(i+1). С помощью скобок следует
полностью определить порядок умножения в матричном произведении
A1 x A2 x ... x An, при котором количество скалярных умножений сведётся к
минимуму.
'''


def matrix_chain_order(p):
    n = len(p) - 1
    m = [[None for _ in range(n)] for _ in range(n)]
    s = [[None for _ in range(n)] for _ in range(n-1)]
    for i in range(n):
        m[i][i] = 0
    for t in range(1, n):
        for i in range(n-t):
            j = i + t
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return optimal_parens(s, 0, n-1, '')


def optimal_parens(s, i, j, res):
    if i == j:
        res += f'A{i+1}'
    else:
        res += '('
        res = optimal_parens(s, i, s[i][j], res)
        res += 'x'
        res = optimal_parens(s, s[i][j]+1, j, res)
        res += ')'
    return res


def main():
    p = [5, 10, 3, 12, 5, 50, 6]
    print(matrix_chain_order(p))


if __name__ == '__main__':
    main()
