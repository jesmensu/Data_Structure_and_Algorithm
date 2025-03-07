class graph:
    def __init__(self, vertex_no):
        self.vertex_no = vertex_no
        self.adj_list = {i:[] for i in range(vertex_no)}

    def insert_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start_node):
        queue = []
        visited = [False]*self.vertex_no
        queue.append(start_node)
        visited[start_node] = True
        while queue:
            node = queue.pop()
            print(node)
            for neighbor in self.adj_list[node]:
                if visited[neighbor] == False:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def dfs(self, start_node):
        stack = []
        visited = [False]*self.vertex_no
        stack.append(start_node)
        visited[start_node] = True
        while stack:
            node = stack.pop(0)
            print(node)
            for neighbor in self.adj_list[node]:
                if visited[neighbor] == False:
                    stack.append(neighbor)
                    visited[neighbor] = True


if __name__ == "__main__":
    g =  graph(5)
    g.insert_edge(2,3)
    g.insert_edge(0,3)
    g.insert_edge(2,4)
    g.insert_edge(0,1)
    g.insert_edge(1,3)
    g.insert_edge(3,4)
    g.dfs(0)