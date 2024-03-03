import sys

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


    def has_edge(self, u, v):
        for vertex, weight in self.graph_adj_list[u]:
            if vertex == v:
                return True
        return False
    
    def get_min_dist_vertex(self, dist, shortest_path_vertex):
        min_dist = sys.maxsize
        min_dist_vertex = None
        for k, v in dist.items():
            if k not in shortest_path_vertex and min_dist > v:
                min_dist = v
                min_dist_vertex = k
        return min_dist_vertex
    
    def get_shortest_path(self, src):
        dist = {}
        dist[src] = 0
        shortest_path_vertex = []
        final_path = {}
        final_path[src] = []
        for key, value in self.graph_adj_list.items():
            min_dist_vertex = self.get_min_dist_vertex(dist, shortest_path_vertex)
            shortest_path_vertex.append(min_dist_vertex)
            for v, weight in value:
                new_dist = dist[min_dist_vertex] + weight
                if v not in dist or dist[v]>new_dist:
                    dist[v] = new_dist
                    final_path[v] = final_path[key] + [key]
                   

        print(dist)
        print(final_path)

g = Graph(5)
g.add_edge(0,1, 3)
g.add_edge(1,2, 6)
g.add_edge(1,3, 4)
g.add_edge(2,4, 9)
g.add_edge(3,4, 1)
g.print_adj_list()
# print(g.has_edge(1,3))
g.get_shortest_path(0)