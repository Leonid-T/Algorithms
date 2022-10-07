'''
Жадные алгоритмы.
Задача:
Выбрать как можно больше взаимно совместимых процессов. процессы совместимы,
если они не перекрываются, т.е. Activity1.end <= Activity2.begin.
'''


from typing import List


class Activity:
    def __init__(self, begin: int, end: int) -> None:
        self.begin = begin
        self.end = end

    def __repr__(self) -> str:
        return f'{__class__.__name__}({self.begin}, {self.end})'


def greedy_activity_selector(a: List) -> List:
    n = len(a)
    for i in range(n-1):
        if a[i].end > a[i+1].end:
            a.sort(key=lambda x: x.end)

    k = 0
    s = [a[k]]
    for i in range(1, n):
        if a[k].end <= a[i].begin:
            s.append(a[i])
            k = i
    return s


def main():
    a = [
        Activity(1, 4),
        Activity(3, 5),
        Activity(0, 6),
        Activity(5, 7),
        Activity(3, 9),
        Activity(5, 9),
        Activity(6, 10),
        Activity(8, 11),
        Activity(8, 12),
        Activity(2, 14),
        Activity(12, 16)
        ]
    print(*greedy_activity_selector(a), sep='\n')


if __name__ == '__main__':
    main()
