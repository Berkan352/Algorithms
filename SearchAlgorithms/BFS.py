# Breadth First Search Algorithm
from some_trainings.data_structres.graph import Graph

def bfs(graph, start, end):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        visited.add(vertex)
        if vertex == end:
            return True
        for neighbour in graph.edges[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
    return False


if __name__ == '__main__':
    graph = Graph()
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')

    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 1)
    graph.add_edge('B', 'D', 1)
    graph.add_edge('C', 'E', 1)
    print(graph.edges)
    print(bfs(graph, 'A', 'D'))

