try:
    from Graph.graph import Graph, Vertex
except ImportError:
    import sys
    sys.path.append('..')
    from Graph.graph import Graph, Vertex

from collections import deque


def BFS(graph: Graph, start: Vertex, end: Vertex) -> None:
    distance_parent = {vertex: [None, None] for vertex in graph.vertices}
    distance_parent[start][0] = 0
    verties_process = deque()
    verties_process.append(start)
    while len(verties_process) != 0:
        u = verties_process.popleft()
        for v in u.neighbours:
            if distance_parent[v][0] is None:
                distance_parent[v][0] = distance_parent[u][0] + 1
                distance_parent[v][1] = u
                verties_process.append(v)
    s = path(start, end, distance_parent, 'BFS\nPath: ')[:-4]
    print(s)


def path(start: Vertex, vertex: Vertex, distance_parent: dict, s: str) -> None:
    if vertex == start:
        s += f'{start} -> '
    elif distance_parent[vertex][1] is None:
        s = 'No way'
    else:
        s = path(start, distance_parent[vertex][1], distance_parent, s)
        s += f'{vertex} -> '
    return s


def DFS(graph: Graph) -> None:
    parent_begin_end = {
        vertex: [None, None, None] for vertex in graph.vertices
        }
    time = 0
    for vertex in graph.vertices:
        if parent_begin_end[vertex][1] is None:
            time = DFS_visit(graph, vertex, time, parent_begin_end)
    print('DFS')
    for vertex in graph.vertices:
        s = parent_begin_end[vertex]
        print(
           f'{vertex}: parent = {s[0]}, time begin = {s[1]}, time end = {s[2]}'
             )


def DFS_visit(
        graph: Graph, vertex: Vertex, time: int, parent_begin_end: dict
        ) -> None:
    time += 1
    parent_begin_end[vertex][1] = time
    for v in vertex.neighbours:
        if parent_begin_end[v][1] is None:
            parent_begin_end[v][0] = vertex
            time = DFS_visit(graph, v, time, parent_begin_end)
    time += 1
    parent_begin_end[vertex][2] = time
    return time


def main():
    values = ['v', 'r', 's', 'w', 't', 'x', 'u', 'y']
    edges = [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 7),
        (3, 5),
        (4, 6),
        (5, 7),
        ]
    graph = Graph(values=values, edges=edges, symmetric=True)
    BFS(graph, graph.vertices[2], graph.vertices[6])
    print()
    DFS(graph)


if __name__ == '__main__':
    main()
