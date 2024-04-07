# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
# Uses Greedy algorithm
import sys


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

    def has_edge(self, u, v):
        edge_weight = self.graph_adj_matrix[u][v]
        return edge_weight != 0
    
    def get_adj_vertex(self, u, spt=[]):
        adj_list = []
        for i in range(len(self.graph_adj_matrix[u])):
            if i not in spt and self.graph_adj_matrix[u][i] != 0:
                adj_list.append(i)
        return adj_list
    

    def get_shortest_path(self, src):
        spt = []
        dist = [sys.maxsize]* self.vertex_no
        dist[src] = 0
        shotrest_path = [False]* self.vertex_no
        while len(spt) < self.vertex_no:
            min_dist_vertex = self.get_min_dist_vertex(dist, shotrest_path)
            spt.append(min_dist_vertex)
            adj_vertex_list = self.get_adj_vertex(min_dist_vertex, spt)
            shotrest_path[min_dist_vertex] = True
            for v in adj_vertex_list:
                new_dist = dist[min_dist_vertex] + self.graph_adj_matrix[min_dist_vertex][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                
            
        for i in range(self.vertex_no):
            print(i, dist[i])


    def get_min_dist_vertex(self, dist, shotrest_path):
        min_dist_vertex = None
        min_dist = sys.maxsize
        for v in range(self.vertex_no):
            if shotrest_path[v] == False:
                if dist[v]< min_dist:
                    min_dist = dist[v]
                    min_dist_vertex = v
        
        return min_dist_vertex

    def shortest_path_2(self, src):   # Propper solution
        dist = [sys.maxsize]* self.vertex_no
        dist[src] = 0
        shotrest_path = [False]* self.vertex_no

        for v in range(self.vertex_no):
            min_dist_vertex = self.get_min_dist_vertex(dist, shotrest_path)
            shotrest_path[min_dist_vertex] = True

            for u in range(self.vertex_no):
                if self.graph_adj_matrix[min_dist_vertex][u] != 0 and shotrest_path[u] == False:
                    new_dist = dist[min_dist_vertex] + self.graph_adj_matrix[min_dist_vertex][u]
                    if new_dist < dist[u]:
                        dist[u] = new_dist

        for i in range(self.vertex_no):
            print(i, dist[i])
    
    def shortest_path_3(self, src):   
        # Solution with path
        dist = [sys.maxsize]* self.vertex_no
        dist[src] = 0
        shotrest_path = [False]* self.vertex_no
        path = {i:[] for i in range(self.vertex_no)}
        for v in range(self.vertex_no):
            min_dist_vertex = self.get_min_dist_vertex(dist, shotrest_path)
            shotrest_path[min_dist_vertex] = True
            
            for u in range(self.vertex_no):
                if self.graph_adj_matrix[min_dist_vertex][u] != 0 and shotrest_path[u] == False:
                    new_dist = dist[min_dist_vertex] + self.graph_adj_matrix[min_dist_vertex][u]
                    if new_dist < dist[u]:
                        dist[u] = new_dist
                        path[u] = path[min_dist_vertex] + [min_dist_vertex]
                    
        for i in range(self.vertex_no):
            print(i, dist[i])

        print(path)



g = Graph(9)
g.add_edge(0,1,4)
g.add_edge(0,7,8)
g.add_edge(1,2,8)
g.add_edge(1,7,11)
g.add_edge(2,3,7)
g.add_edge(3,4,9)
g.add_edge(4,5,10)
g.add_edge(5,6,2)
g.add_edge(7,6,1)
g.add_edge(6,8,6)
g.add_edge(7,8,7)
g.add_edge(2,5,4)
g.add_edge(3,5,14)
g.add_edge(2,8,2)

g.print_adj_matrix()
# print(g.get_adj_vertex(2, [1]))

# g.get_shortest_path(0)
g.shortest_path_3(0)