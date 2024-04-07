import sys
import heapq

# With 
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
    
    def get_shortest_path_using_heap(self, src):
        dist = {k: float("inf") for k in range(self.vertex_no)}
        dist[src] = 0 
        self.q = []
        heapq.heappush(self.q, (0, src))        #  self.heapsort(vertex_with_weight)
        while self.q:
            min_weight, vertex = heapq.heappop(self.q)  # logn
            dist[vertex] = min_weight
            for neibour, weight in self.graph_adj_list[vertex]:
                new_weight = min_weight + weight
                if new_weight< dist[neibour]:
                    dist[neibour] = new_weight
                    heapq.heappush(self.q, (new_weight, neibour))
        print(dist)

    def update_queue(self, q, dist, vertex):
        if vertex in q:
            q.remove(vertex)
        index = 0
        while index<len(q) and dist[vertex]< dist[q[index]]:
            index += 1
        q.insert(index, vertex)


    def get_shortest_path_using_queue(self, src):
        dist = {k: float("inf") for k in range(self.vertex_no)}
        dist[src] = 0 
        self.q = []
        self.q.append(0)
        final_path = {}
        final_path[src] = []

        while self.q:
            vertex = self.q.pop(0)  # logn
            min_weight = dist[vertex]
            for neibour, weight in self.graph_adj_list[vertex]:
                new_weight = min_weight + weight
                if new_weight< dist[neibour]:
                    dist[neibour] = new_weight
                    self.update_queue(self.q, dist, neibour)
                    final_path[neibour] = final_path[vertex] + [vertex]
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
# g.get_shortest_path_using_heap(0)
g.get_shortest_path_using_queue(0)