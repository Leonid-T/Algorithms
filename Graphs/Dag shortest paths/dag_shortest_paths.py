'''
Процедура dag_shortest_paths решает задачу о кратчайшем пути из одной вершины,
рассматривая вершины в порядке топологической сортировки.
'''


try:
    from Graph.graph import Graph, Vertex
except ImportError:
    import sys
    sys.path.append('..')
    from Graph.graph import Graph, Vertex


def dag_shortest_paths(graph: Graph, start: Vertex) -> None:
    topological_sort(graph)
    distance_parent = initialize_single_sourse(graph, start)
    for u in graph.vertices:
        for v, weight in u.neighbours:
            relax(u, v, weight, distance_parent)
    print_paths(graph, start, distance_parent)


def initialize_single_sourse(graph: Graph, start: Vertex) -> dict:
    distance_parent = {
        vertex: [float('inf'), None] for vertex in graph.vertices
        }
    distance_parent[start][0] = 0
    return distance_parent


def relax(u: Vertex, v: Vertex, weight: int, distance_parent: dict) -> None:
    if distance_parent[v][0] > distance_parent[u][0] + weight:
        distance_parent[v][0] = distance_parent[u][0] + weight
        distance_parent[v][1] = u


def topological_sort(graph: Graph) -> None:
    not_used = {vertex: True for vertex in graph.vertices}
    for vertex in graph.vertices.copy():
        if not_used[vertex]:
            DFS_visit(graph, vertex, not_used)


def DFS_visit(graph: Graph, vertex: Vertex, not_used: dict) -> None:
    not_used[vertex] = False
    for v, weight in vertex.neighbours:
        if not_used[v]:
            DFS_visit(graph, v, not_used)
    i = graph.vertices.index(vertex)
    v = graph.vertices.pop(i)
    graph.vertices.insert(0, v)


def print_paths(graph: Graph, start: Vertex, distance_parent: dict) -> None:
    for vertex in graph.vertices:
        s = f'Lenght = {distance_parent[vertex][0]}; Path: '
        s = path(start, vertex, distance_parent, s)[:-4]
        print(s)


def path(start: Vertex, end: Vertex, distance_parent: dict, s: str) -> None:
    if start == end:
        s += f'{start} -> '
    elif distance_parent[end][1] is None:
        s = f'No way to {end}    '
    else:
        s = path(start, distance_parent[end][1], distance_parent, s)
        s += f'{end} -> '
    return s


def main():
    values = ['r', 's', 't', 'x', 'y', 'z']
    edges = [
        (0, 1, 5),
        (0, 2, 3),
        (1, 2, 2),
        (1, 3, 6),
        (2, 3, 7),
        (2, 4, 4),
        (2, 5, 2),
        (3, 4, -1),
        (3, 5, 1),
        (4, 5, -2),
        ]
    graph = Graph(values=values, edges=edges, weight=True)
    dag_shortest_paths(graph, graph.vertices[1])


if __name__ == '__main__':
    main()
