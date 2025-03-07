import sys
class Graph:
    def __init__(self, edges, no_vertices):
        self.graph_edges = edges
        self.no_vertices = no_vertices


    def shortest_path(self):
        dist = [0] + [sys.maxsize]*(self.no_vertices-1)
        for i in range(self.no_vertices):
            for weight_and_edge in self.graph_edges:
                weight = weight_and_edge[0]
                u = weight_and_edge[1]
                v = weight_and_edge[2]
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        print(dist)





if __name__ == "__main__":
    edges = [[3, 0,1],
            [6, 1,2],
            [4, 1,3],
            [9, 2,4],
            [1, 3,4]]
    g = Graph(edges, 5)
    # print(g.find_abs_paretnt(0))
    g.shortest_path()
    # print(g.graph_edges)

