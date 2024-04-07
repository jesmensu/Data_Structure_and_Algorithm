class Graph:
    def __init__(self, edges, no_vertices):
        self.graph_edges = edges
        self.no_vertices = no_vertices
        self.parents = [i for i in range(no_vertices)]
        self.rank = [0]*no_vertices

    def find_abs_paretnt(self, node):
        if self.parents[node] == node:
            return node
        self.parents[node] = self.find_abs_paretnt(self.parents[node])
        return self.parents[node]

    def krushkal_algo(self):
        self.graph_edges = sorted(self.graph_edges, key = lambda item: item[0])
        cost = 0
        result = []
        for weight_and_edge in self.graph_edges:
            weight = weight_and_edge[0]
            u, v = weight_and_edge[1]
            ap_u = self.find_abs_paretnt(u)
            ap_v = self.find_abs_paretnt(v)
            if ap_u == ap_v:
                continue
            if self.rank[ap_u]< self.rank[ap_v]:
                self.parents[ap_u] = ap_v
            elif self.rank[ap_u]> self.rank[ap_v]:
                self.parents[ap_v] = ap_u
            else:
                self.parents[ap_v] = ap_u
                self.rank[ap_u] += 1
            result.append((u,v))
            cost += weight
        print(result)
        print(cost)




        



if __name__ == "__main__":
    edges = [[3, (0,1)],
            [6, (1,2)],
            [4, (1,3)],
            [9, (2,4)],
            [1, (3,4)]]
    g = Graph(edges, 5)
    # print(g.find_abs_paretnt(0))
    g.krushkal_algo()
    # print(g.graph_edges)

