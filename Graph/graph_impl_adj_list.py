class Graph:
    def __init__(self, vertex_no) -> None:
        self.vertex_no = vertex_no
        self.graph_adj_list = {k:[] for k in range(vertex_no)}

    def print_adj_list(self):
        for i in self.graph_adj_list.items():
            print(i)

    def add_edge(self, u, v, weight = 7):
        self.graph_adj_list[u].append((v,weight))
        self.graph_adj_list[v].append((u, weight))
    
    def remove_edge(self, u, v):
        for vertex, weight in self.graph_adj_list[u]:
            if vertex == v:
                self.graph_adj_list[u].remove((vertex,weight))

        for vertex, weight in self.graph_adj_list[v]:
            if vertex == u:
                self.graph_adj_list[v].remove((vertex,weight))


    def has_edge(self, u, v):
        for vertex, weight in self.graph_adj_list[u]:
            if vertex == v:
                return True
        return False

g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.remove_edge(1,3)
g.print_adj_list()
print(g.has_edge(1,3))