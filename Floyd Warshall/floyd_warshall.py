'''
Алгоритм Флойда Уоршелла решает задачу поиска кратчайших путей между
всеми парами вершин в ориентированном графе с помощью методов динамического
программирования.
'''


try:
    from Graph.graph import Graph
except ImportError:
    import sys
    sys.path.append('..')
    from Graph.graph import Graph

from typing import List


def floyd_warshall(graph: Graph) -> None:
    D = get_matrix(graph)
    n = len(D)
    P = [
        [i if i != j and D[i][j] < float('inf') else None for j in range(n)]
        for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = P[k][j]
    print_paths(D, P, graph)


def get_matrix(graph: Graph) -> tuple:
    '''
    Matrix representation of graph
    '''
    n = len(graph.vertices)
    accord = {graph.vertices[i]: i for i in range(n)}
    W = [[float('inf') for j in range(n)] for i in range(n)]
    for i in range(n):
        W[i][i] = 0
    for u in graph.vertices:
        for v, weight in u.neighbours:
            W[accord[u]][accord[v]] = weight
    return W


def print_paths(L: List, P: List, graph: Graph) -> None:
    n = len(L)
    for i in range(n):
        for j in range(n):
            s = path(i, j, P, f'Lenght = {L[i][j]}; Path: ', graph)[:-4]
            print(s)
        print()


def path(i: int, j: int, P: list, s: str, graph: Graph) -> None:
    if i == j:
        s += f'{graph.vertices[i]} -> '
    elif P[i][j] is None:
        s = f'No way from {graph.vertices[i]} to {graph.vertices[j]}    '
    else:
        s = path(i, P[i][j], P, s, graph)
        s += f'{graph.vertices[j]} -> '
    return s


def main():
    values = ['1', '2', '3', '4', '5']
    edges = [
        (0, 1, 3),
        (0, 2, 8),
        (0, 4, -4),
        (1, 3, 1),
        (1, 4, 7),
        (2, 1, 4),
        (3, 0, 2),
        (3, 2, -5),
        (4, 3, 6),
        ]
    graph = Graph(values=values, edges=edges, weight=True)
    floyd_warshall(graph)


if __name__ == '__main__':
    main()
