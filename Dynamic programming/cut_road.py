'''
Динамическое программирование.
Задача:
Компания покупает стержени длиной n, режет их и продаёт по кускам. Стоимость
каждого куска записана в массиве p в зависимости от длины - индекса. Порезка
стержней имеет нулевую стоимость. Требуется разрезать стержни на куски таким
образом, чтобы прибыль была максимальной.
'''


def memoized_cut_rod(p, n):
    '''
    Низходящий метод
    '''
    r = [-1 for _ in range(n+1)]
    r[0] = 0
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    else:
        q = -1
        for i in range(1, n+1):
            pi = 0 if i >= len(p) else p[i]
            q = max(q, pi + memoized_cut_rod_aux(p, n-i, r))
        r[n] = q
        return q


def bottom_up_cut_rod(p, n):
    '''
    Восходящий метод
    '''
    r = [0 for _ in range(n+1)]
    s = [0 for _ in range(n+1)]
    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            pi = 0 if i >= len(p) else p[i]
            if q < pi + r[j-i]:
                q = pi + r[j-i]
                s[j] = i
        r[j] = q
    return r[n], s


def cut_rod_solution(p, n):
    r, s = bottom_up_cut_rod(p, n)
    res = ''
    i = n
    while i > 0:
        res += f'{s[i]} '
        i -= s[i]
    return f'lenght: {n}; cost: {r}; parts: {res}'


def main():
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 5
    print(cut_rod_solution(p, n))
    print(f'cost: {memoized_cut_rod(p, 5)}')


if __name__ == '__main__':
    main()
