def find_cycles(graph):
    cycles = []
    path = []
    visited = set()

    for node in graph:
        stack = [node]  # Stack to store (node, path) tuples
        visited.add(0)  # Set to keep track of visited nodes

        while stack:
            current = stack.pop()

            if current in path:
                # If the current node is already visited, it's part of a cycle
                idx = path.index(current)
                cycle = path[idx:]
                del path[idx:]
                cycles.append(cycle)
                stack.append(current)
                continue
            for neighbor in graph[current]:
                
                stack.append(neighbor)


            visited.add(current)



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
