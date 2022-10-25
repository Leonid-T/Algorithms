'''
Процедура generic_push_relabel решает задачу поиска максимального потока в
графе между вершинами s и t. Данный алгоритм основан на методе проталкивания
предпотока между вершинами.
'''


try:
    from Graph.graph import Graph, Vertex
except ImportError:
    import sys
    sys.path.append('..')
    from Graph.graph import Graph, Vertex

from typing import List


def generic_push_relabel(graph: Graph, start: Vertex, end: Vertex) -> int:
    graph = copy_graph(graph, start, end)
    f = initialize_preflow(graph)
    push_list = get_push_list(graph, f)
    relabel_list = get_relabel_list(graph, f)
    while push_list or relabel_list:
        for u, v, weight in push_list:
            push(u, v, weight, f)
        for u in relabel_list:
            relabel(u, f)
        push_list = get_push_list(graph, f)
        relabel_list = get_relabel_list(graph, f)
    return graph.end.e


def get_push_list(graph: Graph, f: dict) -> List:
    push_list = [
        (u, v, weight) for u in graph.vertices
                           for v, weight in u.neighbours
        if u.e > 0 and weight - f[(u, v)] > 0 and u.h == v.h + 1
        ]
    return push_list


def push(u: Vertex, v: Vertex, weight: int, f: dict) -> None:
    d = min(u.e, weight - f[(u, v)])
    f[(u, v)] += d
    u.e -= d
    v.e += d


def get_relabel_list(graph: Graph, f: dict) -> List:
    relabel_list = []
    for u in graph.vertices:
        if u.e > 0:
            v_list = [
                v for v, weight in u.neighbours if weight - f[(u, v)] > 0
                ]
            if v_list:
                flag = True
                for v in v_list:
                    if u.h > v.h:
                        flag = False
                if flag:
                    relabel_list.append(u)
    return relabel_list


def relabel(u: Vertex, f: dict) -> None:
    u.h = 1 + min(
        [v.h for v, weight in u.neighbours if weight - f[(u, v)] > 0]
        )


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
    max_f = generic_push_relabel(graph, graph.vertices[0], graph.vertices[-1])
    print(max_f)


if __name__ == '__main__':
    main()
