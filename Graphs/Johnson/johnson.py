'''
Алгоритм Джонсона решает задачу поиска кратчайших путей между всеми парами
вершин в ориентированном графе с помощью запуска алгоритма Дейкстры для каждой
вершины графа. Данный алгоритм наиболее эффективен для разреженных графов
'''


try:
    from Graph.graph import Graph, Vertex
except ImportError:
    import sys
    sys.path.append('..')
    from Graph.graph import Graph, Vertex

from priority_queue import PriorityQueue

from typing import List


def johnson(graph: Graph) -> None:
    new_graph = get_new_graph(graph)
    distance, cond = bellman_ford(new_graph, new_graph.start)
    if not cond:
        print('Входной граф содержит цикл с отрицательным весом')
    else:
        for u in new_graph.vertices:
            for i in range(len(u.neighbours)):
                v, weight = u.neighbours[i]
                weight = weight + distance[u] - distance[v]
                u.neighbours[i] = v, weight
        new_graph.delete_vertex(new_graph.start)
        n = len(new_graph.vertices)
        accord = {new_graph.vertices[i]: i for i in range(n)}
        D = [[None for _ in range(n)] for _ in range(n)]
        P = [[None for _ in range(n)] for _ in range(n)]
        for u in new_graph.vertices:
            d_p = dijkstra(new_graph, u)
            for v in d_p:
                D[accord[u]][accord[v]] = d_p[v][0] + distance[v] - distance[u]
                if d_p[v][1] is not None:
                    P[accord[u]][accord[v]] = accord[d_p[v][1]]
        print_paths(D, P, graph)


def get_new_graph(graph: Graph) -> Graph:
    new_graph = Graph(weight=True)
    ind = {}
    for i in range(len(graph.vertices)):
        val = graph.vertices[i].value
        new_vertex = Vertex(val)
        new_graph.add_vertex(new_vertex)
        ind[val] = i
    for vertex in graph.vertices:
        for v, weight in vertex.neighbours:
            vertex1 = new_graph.vertices[ind[vertex.value]]
            vertex2 = new_graph.vertices[ind[v.value]]
            new_graph.add_edge(vertex1, vertex2, weight)
    start = Vertex('s')
    new_graph.add_vertex(start)
    for new_vertex in new_graph.vertices[:-1]:
        new_graph.add_edge(start, new_vertex, 0)
    new_graph.start = start
    return new_graph


def bellman_ford(graph: Graph, start: Vertex) -> bool:
    '''
    Возвращает True, если в графе нет отрицательных циклов, False - в противном
    случае.
    '''
    distance = {
        vertex: float('inf') for vertex in graph.vertices
        }
    distance[start] = 0
    for _ in range(len(graph.vertices)-1):
        for u in graph.vertices:
            for v, weight in u.neighbours:
                distance[v] = min(distance[v], distance[u] + weight)
    for u in graph.vertices:
        for v, weight in u.neighbours:
            if distance[v] > distance[u] + weight:
                return distance, False
    return distance, True


def dijkstra(graph: Graph, start: Vertex) -> dict:
    distance_parent = {
        vertex: [float('inf'), None] for vertex in graph.vertices
        }
    distance_parent[start][0] = 0
    priority_queue = PriorityQueue(
        [(distance_parent[vertex][0], vertex) for vertex in graph.vertices]
        )
    while priority_queue.size != 0:
        u = priority_queue.extract_min()
        for v, weight in u.neighbours:
            if distance_parent[v][0] > distance_parent[u][0] + weight:
                distance_parent[v][0] = distance_parent[u][0] + weight
                distance_parent[v][1] = u
                priority_queue.replace_key(distance_parent[v][0], v)
    return distance_parent


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
    johnson(graph)


if __name__ == '__main__':
    main()
