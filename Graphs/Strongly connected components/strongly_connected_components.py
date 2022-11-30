try:
    from Graph.graph import Graph, Vertex
except ImportError:
    import sys
    sys.path.append('..')
    from Graph.graph import Graph, Vertex

from typing import List


def strongly_connected_components(graph: Graph) -> None:
    topological_sort(graph)
    graphT = graph.transposition()

    not_used = {vertex: True for vertex in graphT.vertices}
    values = []
    for vertex in graphT.vertices:
        if not_used[vertex]:
            values.append('')
            connect_components(vertex, not_used, values)
    return values


def topological_sort(graph: Graph) -> None:
    not_used = {vertex: True for vertex in graph.vertices}
    for vertex in graph.vertices.copy():
        if not_used[vertex]:
            DFS_visit(graph, vertex, not_used)


def DFS_visit(graph: Graph, vertex: Vertex, not_used: dict) -> None:
    not_used[vertex] = False
    for v in vertex.neighbours:
        if not_used[v]:
            DFS_visit(graph, v, not_used)
    i = graph.vertices.index(vertex)
    v = graph.vertices.pop(i)
    graph.vertices.insert(0, v)


def connect_components(vertex: Vertex, not_used: dict, values: List) -> None:
    not_used[vertex] = False
    values[-1] += vertex.value
    for v in vertex.neighbours:
        if not_used[v]:
            connect_components(v, not_used, values)


def main():
    values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    edges = [
        (0, 1),
        (1, 2),
        (1, 4),
        (1, 6),
        (2, 3),
        (2, 6),
        (3, 2),
        (3, 7),
        (4, 0),
        (4, 6),
        (5, 6),
        (6, 5),
        (6, 7),
        (7, 7),
        ]
    graph = Graph(values=values, edges=edges)
    print(
        'Strongly connected components:', *strongly_connected_components(graph)
        )


if __name__ == '__main__':
    main()
