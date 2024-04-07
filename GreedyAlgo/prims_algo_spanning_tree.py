import sys
import heapq

# With 
class Graph:
    def __init__(self, vertex_no) -> None:
        self.vertex_no = vertex_no
        self.graph_adj_list = {k:[] for k in range(vertex_no)}
        # self.pq = heapq

    def print_adj_list(self):
        for i in self.graph_adj_list.items():
            print(i)

    def add_edge(self, u, v, weight = 7):
        self.graph_adj_list[u].append((v, weight))
        self.graph_adj_list[v].append((u, weight))


    def has_edge(self, u, v):
        for vertex, weight in self.graph_adj_list[u]:
            if vertex == v:
                return True
        return False
    
    # def create_heap(self, src):
    #     for u in self.graph_adj_list:
    #         for 
    #         edge = 

    #     pq = heapq.heappush()

    def add_to_queue(self, queue, edge_weight):
        i = 0
        while i < len(queue) and queue[i][0]<edge_weight[0]:
            i +=1
        queue.insert(i, edge_weight)


    def spanning_tree_prims_algo_queue(self, src):
        cost = 0
        tree_path = []
        visited = []
        pqueue = []
        # visited.append(src)
        pqueue.append((0, (src, src)))
        while pqueue:
            weight, edge = pqueue.pop(0)
            current = edge[1]
            if current in visited:
                continue
            visited.append(current)
            cost += weight
            tree_path.append(edge)

            for neibour, weight in self.graph_adj_list[current]:
                if neibour not in visited:
                    edge = (current, neibour)
                    self.add_to_queue(pqueue, (weight, edge))


        print(tree_path)
        print(cost)


    def spanning_tree_prims_algo_heap(self, src):
        cost = 0
        tree_path = []
        visited = []
        pq = []
        # visited.append(src)
        heapq.heappush(pq, (0, (src, src)))
        while heapq:
            weight, edge = heapq.heappop()
            current = edge[1]
            if current in visited:
                continue
            visited.append(current)
            cost += weight
            tree_path.append(edge)

            for neibour, weight in self.graph_adj_list[current]:
                if neibour not in visited:
                    edge = (current, neibour)
                    heapq.heappush(pq, (weight, edge))


        print(tree_path)
        print(cost)





g = Graph(5)
g.add_edge(0,1, 3)
g.add_edge(1,2, 6)
g.add_edge(1,3, 4)
g.add_edge(2,4, 9)
g.add_edge(3,4, 1)
g.print_adj_list()
# print(g.has_edge(1,3))
# g.get_shortest_path_using_heap(0)
g.spanning_tree_prims_algo_queue(0)