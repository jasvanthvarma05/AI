import itertools

def travelling_salesman(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = None
    min_cost = float('inf')

    for permutation in itertools.permutations(vertices):
        current_cost = 0
        k = start
        for j in permutation:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][start]
        if current_cost < min_cost:
            min_cost = current_cost
            min_path = (start,) + permutation + (start,)

    print(f"Minimum Cost: {min_cost}")
    print(f"Path: {' -> '.join(min_path)}")

graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

travelling_salesman(graph, 'A')
