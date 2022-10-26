'''
Процедура relabel_to_front решает задачу поиска максимального потока в
графе между вершинами s и t. Данный алгоритм основан на методе проталкивания
предпотока между вершинами, при этом поддерживается очередь из вершин. Если
после разгрузки вершины изменяется её высота, то данная вершина помещается в
начало очереди.
'''

try:
    from Graph.graph import Graph, Vertex
except ImportError:
    import sys
    sys.path.append('..')
    from Graph.graph import Graph, Vertex

from collections import deque


def relabel_to_front(graph: Graph, start: Vertex, end: Vertex) -> int:
    graph = copy_graph(graph, start, end)
    f = initialize_preflow(graph)
    L = deque([
        vertex for vertex in graph.vertices
        if vertex != graph.start and vertex != graph.end
        ])
    for vertex in L:
        vertex.current = 0
    while len(L) > 0:
        u = L.popleft()
        old_h = u.h
        discharge(u, f)
        if u.h > old_h:
            L.append(u)
    return graph.end.e


def discharge(u: Vertex, f: dict) -> None:
    while u.e > 0:
        i = u.current
        if i == len(u.N):
            relabel(u, f)
            u.current = 0
        else:
            v, weight = u.N[i]
            if f.get((u, v), None) is not None:
                cond = weight - f[(u, v)] > 0
            else:
                cond = f[(v, u)] > 0

            if cond and u.h == v.h + 1:
                push(u, v, weight, f)
            else:
                u.current += 1


def push(u: Vertex, v: Vertex, weight: int, f: dict) -> None:
    d = min(u.e, weight - f.get((u, v), 0))
    if f.get((u, v), None) is not None:
        f[(u, v)] += d
    else:
        f[(v, u)] -= d
    u.e -= d
    v.e += d


def relabel(u: Vertex, f: dict) -> None:
    minimum = float('inf')
    for v, weight in u.N:
        if f.get((u, v), None) is not None:
            cond = weight - f[(u, v)] > 0
        else:
            cond = f[(v, u)] > 0
        if cond:
            minimum = min(minimum, v.h)
    u.h = 1 + minimum


def initialize_preflow(graph: Graph) -> dict:
    for vertex in graph.vertices:
        vertex.e = 0
        vertex.h = 0
    f = {(u, v): 0 for u in graph.vertices for v, weight in u.neighbours}
    graph.start.h = len(graph.vertices)
    for v, weight in graph.start.neighbours:
        f[(graph.start, v)] = weight
        v.e = weight
        graph.start.e -= weight
    return f


def copy_graph(graph: Graph, start: Vertex, end: Vertex) -> Graph:
    graphCopy = Graph(weight=True)
    ind = {}
    for i in range(len(graph.vertices)):
        val = graph.vertices[i].value
        vertex = Vertex(val)
        graphCopy.add_vertex(vertex)
        ind[val] = i
    for vertex in graph.vertices:
        for v, weight in vertex.neighbours:
            vertex1 = graphCopy.vertices[ind[vertex.value]]
            vertex2 = graphCopy.vertices[ind[v.value]]
            graphCopy.add_edge(vertex1, vertex2, weight)
    for vertex in graphCopy.vertices:
        vertex.N = vertex.neighbours.copy()
    for vertex in graphCopy.vertices:
        for v, weight in vertex.neighbours:
            v.N.append((vertex, weight))
    graphCopy.start = graphCopy.vertices[ind[start.value]]
    graphCopy.end = graphCopy.vertices[ind[end.value]]
    return graphCopy


def main():
    values = ['s', 'v1', 'v2', 'v3', 'v4', 't']
    edges = [
        (0, 1, 16),
        (0, 2, 13),
        (1, 3, 12),
        (2, 1, 4),
        (2, 4, 14),
        (3, 2, 9),
        (3, 5, 20),
        (4, 3, 7),
        (4, 5, 4),
        ]
    graph = Graph(values=values, edges=edges, weight=True)
    max_f = relabel_to_front(graph, graph.vertices[0], graph.vertices[-1])
    print(max_f)


if __name__ == '__main__':
    main()
