# Python program for floyd warshall algorithm for
# all path shortest path algorithm. The program is
# for adjacency matrix representation of the graph
# Uses Dynamic algorithm
import sys


class Graph:
    def __init__(self, vertex_no) -> None:
        self.vertex_no = vertex_no
        self.graph_adj_matrix = [[float("inf")]*vertex_no for v in range(vertex_no)]

    def print_adj_matrix(self):
        for i in self.graph_adj_matrix:
            print(i)

    def add_edge(self, u, v, weight):
        self.graph_adj_matrix[u][v] = weight

    def has_edge(self, u, v):
        edge_weight = self.graph_adj_matrix[u][v]
        return edge_weight != 0
    
    def get_adj_vertex(self, u, spt=[]):
        adj_list = []
        for i in range(len(self.graph_adj_matrix[u])):
            if i not in spt and self.graph_adj_matrix[u][i] != 0:
                adj_list.append(i)
        return adj_list
    
    def get_all_pair_path(self):
        for i in range(self.vertex_no):
            for j in range(self.vertex_no):
                if i == j:
                    self.graph_adj_matrix[i][j] = 0
        print(self.graph_adj_matrix)
        for k in range(self.vertex_no):
            for i in range(self.vertex_no):
                for j in range(self.vertex_no):
                    if i==j or k==j or k==i:
                        continue
                    new_weight = self.graph_adj_matrix[i][k] + self.graph_adj_matrix[k][j]
                    if self.graph_adj_matrix[i][j] > new_weight:
                        self.graph_adj_matrix[i][j] = new_weight

        print(self.graph_adj_matrix)






g = Graph(5 )
g.add_edge(0,1,4)
g.add_edge(0,3,8)
g.add_edge(1,2,6)
g.add_edge(1,4,11)
g.add_edge(2,3,7)
g.add_edge(2,0,3)
g.add_edge(4,0,1)
g.add_edge(3,4,2)
# g.add_edge(3,4,9)
# g.add_edge(4,5,10)
# g.add_edge(5,6,2)
# g.add_edge(7,6,1)
# g.add_edge(6,8,6)
# g.add_edge(7,8,7)
# g.add_edge(2,5,4)
# g.add_edge(3,5,14)
# g.add_edge(2,8,2)

g.print_adj_matrix()
# print(g.get_adj_vertex(2, [1]))

g.get_all_pair_path()