# Depth First Search algorithm
from some_trainings.data_structres.graph import Graph

def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.edges[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))



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
    print(list(dfs(graph, 'A', 'D')))
