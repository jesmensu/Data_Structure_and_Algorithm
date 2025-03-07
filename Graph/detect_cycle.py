class Graph:
    def __init__(self, vertex_no):
        self.vertex_no = vertex_no
        self.adj_graph = {i:[] for i in range(vertex_no)}

    def add_edge(self, u, v):
        self.adj_graph[u].append(v)
        self.adj_graph[v].append(u)

    def detect_cycle_dfs(self, node):
        stack = []
        path = []
        pos_in_path = {}
        visited = [False]*self.vertex_no
        stack.append((node, -1))
        visited[node] = True
        # print(node)
        while(stack):
            node, parent = stack.pop()
            path.append(node)
            pos_in_path[node] = len(path) - 1
            # print(node)
            for neighbor in self.adj_graph[node]:
                if visited[neighbor] == True and neighbor != parent:
                    # print(neighbor, node)
                    path.append(neighbor)
                    print("cycle: ", path[pos_in_path[parent]: ])
                    return "cycle detected"
                if visited[neighbor] == False:
                    # print(neighbor, node)
                    stack.append((neighbor, node))
                    visited[neighbor] = True


g = Graph(7)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(1,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.add_edge(5,6)

print(g.detect_cycle_dfs(0))