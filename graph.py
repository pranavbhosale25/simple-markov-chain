import random


class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.adjacent = {}  # connected vertices
        self.neighbors = []
        self.neighbors_weights = []

    def add_edge_to(self, vertex, weight=0):
        # add edge to the vertex
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        # increment weight of the edge
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_map(self, vertex):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]


class Graph(object):
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        return set(self.vertices.keys())

    def add_vertex(self, value):
        # value will be a word here
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mapping(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map(vertex)
