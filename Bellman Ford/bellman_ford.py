'''
Алгоритм Бельмана Форда решает задачу о кратчайшем пути из одной вершины в
общем случае, когда вес каждого из рёбер может быть отрицательным.
'''


try:
    from Graph.graph import Graph, Vertex
except ImportError:
    import sys
    sys.path.append('..')
    from Graph.graph import Graph, Vertex


def bellman_ford(graph: Graph, start: Vertex) -> bool:
    '''
    Возвращает True, если в графе нет отрицательных циклов, False - в противном
    случае.
    '''
    distance_parent = initialize_single_sourse(graph, start)
    for _ in range(len(graph.vertices)-1):
        for u in graph.vertices:
            for v, weight in u.neighbours:
                relax(u, v, weight, distance_parent)
    for u in graph.vertices:
        for v, weight in u.neighbours:
            if distance_parent[v][0] > distance_parent[u][0] + weight:
                return False
    return True


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


def main():
    values = ['s', 't', 'x', 'y', 'z']
    edges = [
        (0, 1, 6),
        (0, 3, 7),
        (1, 2, 5),
        (1, 3, 8),
        (1, 4, -4),
        (2, 1, -2),
        (3, 2, -3),
        (3, 4, 9),
        (4, 2, 7),
        ]
    graph = Graph(values=values, edges=edges, weight=True)
    print(bellman_ford(graph, graph.vertices[0]))


if __name__ == '__main__':
    main()
