from __future__ import annotations

from abc import ABC, abstractmethod

from typing import List


class Vertex:
    def __init__(self, value: any) -> None:
        self.value = value
        self.neighbours = []

    def __str__(self) -> str:
        return f'{__class__.__name__}({self.value})'

    def __repr__(self) -> str:
        return f'{__class__.__name__}({self.value})'

    def add_neighbour(self, vertex: Vertex) -> None:
        self.neighbours.append(vertex)


class Graph:
    def __init__(
            self, values=[], edges=[], symmetric=False, weight=False
            ) -> None:
        self.vertices = []
        if weight:
            self._weight_strategy = Weight
        else:
            self._weight_strategy = Nonweight
        self.add_all_vertices(values=values)
        self.add_all_edges(edges=edges, symmetric=symmetric)

    def __str__(self) -> str:
        return f'{__class__.__name__}({str(self.vertices)[1:-1]})'

    def add_all_vertices(self, values=[]) -> None:
        for val in values:
            vertex = Vertex(val)
            self.add_vertex(vertex)

    def add_all_edges(self, edges=[], symmetric=False):
        self._weight_strategy.add_all_edges(
            self, edges=edges, symmetric=symmetric
            )

    def add_vertex(self, vertex: Vertex) -> None:
        self.vertices.append(vertex)

    def add_edge_symmetric(
            self, vertex1: Vertex, vertex2: Vertex, weight=None
            ) -> None:
        self._weight_strategy.add_edge_symmetric(self, vertex1, vertex2)

    def add_edge(self, vertex1: Vertex, vertex2: Vertex, weight=None) -> None:
        self._weight_strategy.add_edge(self, vertex1, vertex2, weight)

    def transposition(self) -> Graph:
        return self._weight_strategy.transposition(self)

    def delete_vertex(self, vertex: Vertex) -> None:
        self._weight_strategy.delete_vertex(self, vertex)


class WeightStrategy(ABC):
    @abstractmethod
    def add_all_edges(self, edges: List, symmetric: bool) -> None:
        pass

    @abstractmethod
    def add_edge_symmetric(
            self, vertex1: Vertex, vertex2: Vertex, weight=None
            ) -> None:
        pass

    @abstractmethod
    def add_edge(self, vertex1: Vertex, vertex2: Vertex, weight=None) -> None:
        pass

    @abstractmethod
    def transposition(self) -> Graph:
        pass

    @abstractmethod
    def delete_vertex(self, vertex: Vertex) -> None:
        pass


class Nonweight(WeightStrategy):
    def add_all_edges(self, edges: List, symmetric: bool) -> None:
        if symmetric:
            for edge in edges:
                vertex1 = self.vertices[edge[0]]
                vertex2 = self.vertices[edge[1]]
                self.add_edge_symmetric(vertex1, vertex2)
        else:
            for edge in edges:
                vertex1 = self.vertices[edge[0]]
                vertex2 = self.vertices[edge[1]]
                self.add_edge(vertex1, vertex2)

    def add_edge_symmetric(
            self, vertex1: Vertex, vertex2: Vertex, weight=None
            ) -> None:
        vertex1.add_neighbour(vertex2)
        vertex2.add_neighbour(vertex1)

    def add_edge(self, vertex1: Vertex, vertex2: Vertex, weight=None) -> None:
        vertex1.add_neighbour(vertex2)

    def transposition(self) -> Graph:
        graphT = Graph()
        ind = {}
        for i in range(len(self.vertices)):
            val = self.vertices[i].value
            vertex = Vertex(val)
            graphT.add_vertex(vertex)
            ind[val] = i
        for vertex in self.vertices:
            for v in vertex.neighbours:
                vertex1 = graphT.vertices[ind[v.value]]
                vertex2 = graphT.vertices[ind[vertex.value]]
                graphT.add_edge(vertex1, vertex2)
        return graphT

    def delete_vertex(self, vertex: Vertex) -> None:
        if vertex in self.vertices:
            i = self.vertices.index(vertex)
            self.vertices.pop(i)
            for v in self.vertices:
                if vertex in v.neighbours:
                    i = v.neighbours.index(vertex)
                    v.neighbours.pop(i)


class Weight(WeightStrategy):
    def add_all_edges(self, edges: List, symmetric: bool) -> None:
        if symmetric:
            for edge in edges:
                vertex1 = self.vertices[edge[0]]
                vertex2 = self.vertices[edge[1]]
                weight = edge[2]
                self.add_edge_symmetric(vertex1, vertex2, weight)
        else:
            for edge in edges:
                vertex1 = self.vertices[edge[0]]
                vertex2 = self.vertices[edge[1]]
                weight = edge[2]
                self.add_edge(vertex1, vertex2, weight)

    def add_edge_symmetric(
            self, vertex1: Vertex, vertex2: Vertex, weight: int
            ) -> None:
        vertex1.add_neighbour((vertex2, weight))
        vertex2.add_neighbour((vertex1, weight))

    def add_edge(self, vertex1: Vertex, vertex2: Vertex, weight: int) -> None:
        vertex1.add_neighbour((vertex2, weight))

    def transposition(self) -> Graph:
        graphT = Graph()
        ind = {}
        for i in range(len(self.vertices)):
            val = self.vertices[i].value
            vertex = Vertex(val)
            graphT.add_vertex(vertex)
            ind[val] = i
        for vertex in self.vertices:
            for v, weight in vertex.neighbours:
                vertex1 = graphT.vertices[ind[v.value]]
                vertex2 = graphT.vertices[ind[vertex.value]]
                graphT.add_edge(vertex1, vertex2, weight)
        return graphT

    def delete_vertex(self, vertex: Vertex) -> None:
        if vertex in self.vertices:
            i = self.vertices.index(vertex)
            self.vertices.pop(i)
            for v in self.vertices:
                neighbours = [ver for ver, weight in v.neighbours]
                if vertex in neighbours:
                    i = neighbours.index(vertex)
                    v.neighbours.pop(i)
