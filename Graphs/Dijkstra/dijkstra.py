'''
Алгоритм Дейкстры решает задачу поиска кратчайших путей из одной вершины во
взвешенном ориентированном графе в случае, когда веса рёбер неотрицательны.
'''


try:
    from Graph.graph import Graph, Vertex
except ImportError:
    import sys
    sys.path.append('..')
    from Graph.graph import Graph, Vertex

from priority_queue import PriorityQueue


def dijkstra(graph: Graph, start: Vertex) -> None:
    distance_parent = initialize_single_sourse(graph, start)
    priority_queue = PriorityQueue(
        [(distance_parent[vertex][0], vertex) for vertex in graph.vertices]
        )
    while priority_queue.size != 0:
        u = priority_queue.extract_min()
        for v, weight in u.neighbours:
            relax(u, v, weight, distance_parent, priority_queue)
    print_paths(graph, start, distance_parent)


def initialize_single_sourse(graph: Graph, start: Vertex) -> dict:
    distance_parent = {
        vertex: [float('inf'), None] for vertex in graph.vertices
        }
    distance_parent[start][0] = 0
    return distance_parent


def relax(u: Vertex, v: Vertex, weight: int,
          distance_parent: dict, priority_queue: PriorityQueue) -> None:
    if distance_parent[v][0] > distance_parent[u][0] + weight:
        distance_parent[v][0] = distance_parent[u][0] + weight
        distance_parent[v][1] = u
        priority_queue.replace_key(distance_parent[v][0], v)


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
    values = ['s', 't', 'x', 'y', 'z']
    edges = [
        (0, 1, 10),
        (0, 3, 5),
        (1, 2, 1),
        (1, 3, 2),
        (2, 4, 4),
        (3, 1, 3),
        (3, 2, 9),
        (3, 4, 2),
        (4, 2, 6),
        (4, 0, 7),
        ]
    graph = Graph(values=values, edges=edges, weight=True)
    dijkstra(graph, graph.vertices[0])


if __name__ == '__main__':
    main()
