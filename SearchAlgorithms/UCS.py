# Uniform Cost Search
from some_trainings.data_structres.graph import Graph


def uniform_cost_search(graph, start, goal):
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph.get(node)
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                frontier.append(new_path)
                if neighbour == goal:
                    return new_path
            explored.add(node)
    return None


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge('S', 'A', 1)
    graph.add_edge('S', 'B', 3)
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'D', 2)
    graph.add_edge('C', 'D', 1)
    graph.add_edge('C', 'G', 3)
    graph.add_edge('D', 'G', 1)
    print(graph.edges)
    path = uniform_cost_search(graph, 'S', 'G')
    print(path)
    cost = sum(graph.distances[(path[i], path[i + 1])] for i in range(len(path) - 1))
    print(cost)






