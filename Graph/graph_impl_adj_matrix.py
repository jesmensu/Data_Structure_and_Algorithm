class Graph:
    def __init__(self, vertex_no) -> None:
        self.vertex_no = vertex_no
        self.graph_adj_matrix = [[0]*vertex_no for v in range(vertex_no)]

    def print_adj_matrix(self):
        for i in self.graph_adj_matrix:
            print(i)

    def add_edge(self, u, v, weight):
        self.graph_adj_matrix[u][v] = weight
        self.graph_adj_matrix[v][u] = weight
    
    def remove_edge(self, u, v):
        self.graph_adj_matrix[u][v] = 0
        self.graph_adj_matrix[v][u] = 0

    def has_edge(self, u, v):
        edge_weight = self.graph_adj_matrix[u][v]
        return edge_weight != 0

g = Graph(5)
g.add_edge(1,2,7)
g.print_adj_matrix()