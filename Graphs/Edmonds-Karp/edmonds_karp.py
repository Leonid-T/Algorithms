'''
Алгоритм Эдмондса-Карпа решает задачу поиска максимального потока в графе между
вершинами s и t. Данный алгоритм основан на методе Форда-Фалкерсона с
применением алгоритма поиска в ширину BFS для вычисления увеличивающего пути.
'''


try:
    from Graph.graph import Graph, Vertex
except ImportError:
    import sys
    sys.path.append('..')
    from Graph.graph import Graph, Vertex

from collections import deque


def edmonds_karp(graph: Graph, start: Vertex, end: Vertex) -> int:
    f = 0
    re_net = get_residual_network(graph, start, end)
    minimum, visited = BFS(re_net, re_net.start, re_net.end)
    while minimum is not None:
        for i in range(len(visited)-1):
            u = visited[i]
            v = visited[i+1]
            for j in range(len(u.neighbours)):
                vertex, weight = u.neighbours[j]
                if vertex == v:
                    weight -= minimum
                    if weight == 0:
                        u.neighbours.pop(j)
                    else:
                        u.neighbours[j] = vertex, weight
                    break
        f += minimum
        minimum, visited = BFS(re_net, re_net.start, re_net.end)
    return f


def get_residual_network(graph: Graph, start: Vertex, end: Vertex) -> Graph:
    residual_network = Graph(weight=True)
    ind = {}
    for i in range(len(graph.vertices)):
        val = graph.vertices[i].value
        vertex = Vertex(val)
        residual_network.add_vertex(vertex)
        ind[val] = i
    for vertex in graph.vertices:
        for v, weight in vertex.neighbours:
            vertex1 = residual_network.vertices[ind[vertex.value]]
            vertex2 = residual_network.vertices[ind[v.value]]
            residual_network.add_edge(vertex1, vertex2, weight)
    residual_network.start = residual_network.vertices[ind[start.value]]
    residual_network.end = residual_network.vertices[ind[end.value]]
    return residual_network


def BFS(graph: Graph, start: Vertex, end: Vertex) -> None:
    distance_parent_weight = {
        vertex: (None, None, None) for vertex in graph.vertices
        }
    distance_parent_weight[start] = (0, None, float('inf'))
    verties_process = deque()
    verties_process.append(start)
    while len(verties_process) != 0:
        u = verties_process.popleft()
        for v, weight in u.neighbours:
            if distance_parent_weight[v][0] is None:
                distance_parent_weight[v] = (
                    distance_parent_weight[u][0] + 1, u, weight
                    )
                verties_process.append(v)

    if distance_parent_weight[end][0] is None:
        return None, None
    else:
        visited = []
        vertex = end
        minimum = distance_parent_weight[vertex][2]
        while vertex is not None:
            visited.insert(0, vertex)
            minimum = min(minimum, distance_parent_weight[vertex][2])
            vertex = distance_parent_weight[vertex][1]
        return minimum, visited


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
    max_f = edmonds_karp(graph, graph.vertices[0], graph.vertices[-1])
    print(max_f)


if __name__ == '__main__':
    main()
