class Graph:
    def __init__(self, vertex_no) -> None:
        self.vertex_no = vertex_no
        self.graph_adj_matrix = [[0]*vertex_no for v in range(vertex_no)]

    def print_adj_matrix(self):
        for i in self.graph_adj_matrix:
            print(i)

    def add_edge(self, u, v, weight = 1):
        self.graph_adj_matrix[u][v] = weight
        self.graph_adj_matrix[v][u] = weight
    
    def remove_edge(self, u, v):
        self.graph_adj_matrix[u][v] = 0
        self.graph_adj_matrix[v][u] = 0

    def has_edge(self, u, v):
        edge_weight = self.graph_adj_matrix[u][v]
        return edge_weight != 0
    
    def print_vertex_dfs(self, node):
        visited = []
        stack = []

        stack.append(node)
        visited.append(node)
        while stack:
            node = stack.pop()
            print(node, end=" ")
            neibour_vertex = self.graph_adj_matrix[node]
            for i in range(len(neibour_vertex)):
                if neibour_vertex[i] == 1:
                    if i not in visited:
                        stack.append(i)
                        visited.append(i)



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
g.print_adj_matrix()
g.print_vertex_dfs(0)
# print(g.has_edge(1,3))