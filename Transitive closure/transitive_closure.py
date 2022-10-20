'''
Процедура transitive_closure находит транзитивное замыкание графа, используя
алгоритм Флойда Уоршелла.
'''


try:
    from Graph.graph import Graph
except ImportError:
    import sys
    sys.path.append('..')
    from Graph.graph import Graph

from typing import List


def transitive_closure(graph: Graph) -> None:
    T = get_matrix(graph)
    n = len(T)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                T[i][j] = T[i][j] or (T[i][k] and T[k][j])
    print_paths(T, graph)


def get_matrix(graph: Graph) -> tuple:
    n = len(graph.vertices)
    accord = {graph.vertices[i]: i for i in range(n)}
    W = [[False for j in range(n)] for i in range(n)]
    for i in range(n):
        W[i][i] = True
    for u in graph.vertices:
        for v in u.neighbours:
            W[accord[u]][accord[v]] = True
    return W


def print_paths(T: List, graph: Graph) -> None:
    n = len(T)
    for i in range(n):
        for j in range(n):
            if T[i][j]:
                s = f'Path from {graph.vertices[i]} to {graph.vertices[j]} is exist'
            else:
                s = f'Path from {graph.vertices[i]} to {graph.vertices[j]} is not exist'
            print(s)
        print()


def main():
    values = ['1', '2', '3', '4']
    edges = [
        (1, 2),
        (1, 3),
        (2, 1),
        (3, 0),
        (3, 2),
        ]
    graph = Graph(values=values, edges=edges)
    transitive_closure(graph)


if __name__ == '__main__':
    main()
