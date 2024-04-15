def find_cycles(graph):
    def dfs(node, visited, path, cycles):
        visited[node] = True
        path.append(node)

        for neighbor in graph[node]:
            if neighbor in path:  # Cycle detected
                idx = path.index(neighbor)
                cycle = path[idx:]
                cycles.append(cycle)
            elif not visited[neighbor]:
                dfs(neighbor, visited, path, cycles)
        
        path.pop()
        visited[node] = False

    cycles = []
    num_nodes = len(graph)
    visited = [False] * num_nodes

    for node in range(num_nodes):
        path = []
        dfs(node, visited, path, cycles)

    return cycles

# Example usage:
graph = {
    0: [1, 2],
    1: [2, 3, 6],
    2: [],
    3: [4, 5],
    4: [0],
    5: [4],
    6: [0]
}

print("All cycles in the graph:", find_cycles(graph))
