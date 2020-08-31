from collections import namedtuple
#Матрицы смежности
graph = [
    [0, 1, 1, 0],
    [1, 0, 1 ,1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]

print(*graph)
graph = [
    [0, 1, 1, 0],
    [0, 0, 1 ,1],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

print(*graph)

#Списки смежности
graph = []
graph.append([1,2])
graph.append([0,2,3])
graph.append([0,1])
graph.append([1])

print(*graph)

graph_2 = {
    0: {1,2},
    1: {0,2,3},
    2: {0,1},
    3: {1},
}
print(graph_2)

Vertex = namedtuple('Vertex', ['vertex', 'edge'])
graph3 = []

graph3.append([Vertex(1,2), Vertex(2,3)])
graph3.append([Vertex(0,2), Vertex(2,2), Vertex(3,1)])
graph3.append([Vertex(0,3), Vertex(1,2)])
graph3.append([Vertex(1,1)])

print(graph3)

class Graph:
    def __init__(self, vertex, edge, spam):
        self.vertex = vertex
        self.edge = edge
        self.spam = spam

#Списки ребёр

graph = [(0,1), (0,2), (1,2), (2,1), (1,3)]

print(*graph)