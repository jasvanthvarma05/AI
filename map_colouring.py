def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def csp_map_coloring(graph, colors, assignment={}, node_order=None):
    if len(assignment) == len(graph):
        return assignment
    if node_order is None:
        node_order = list(graph.keys())
    node = node_order[len(assignment)]
    for color in colors:
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            result = csp_map_coloring(graph, colors, assignment, node_order)
            if result:
                return result
            del assignment[node]
    return None

graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

colors = ['Red', 'Green', 'Blue']

solution = csp_map_coloring(graph, colors)
print(solution)
