'''
В данной программе производится построение ориентированного графа на основе
вещей, которые нужно надевать в определённом порядке. Топологическая сортировка
графа даёт порядок одевания.
'''


try:
    from Graph.graph import Graph, Vertex
except ImportError:
    import sys
    sys.path.append('..')
    from Graph.graph import Graph, Vertex


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


def main():
    values = [
        'Трусы',
        'Носки',
        'Брюки',
        'Туфли',
        'Часы',
        'Рубашка',
        'Ремень',
        'Галстук',
        'Пиджак',
        ]
    edges = [
        (0, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (2, 6),
        (5, 6),
        (5, 7),
        (6, 8),
        (7, 8),
        ]
    graph = Graph(values=values, edges=edges)
    topological_sort(graph)
    for i in range(len(graph.vertices)):
        print(f'{i+1}. {graph.vertices[i].value}')


if __name__ == '__main__':
    main()
