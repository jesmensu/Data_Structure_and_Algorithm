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
    
    def print_vertex_bfs(self, node):
        visited = []
        queue = []

        queue.append(node)
        visited = [False]*self.vertex_no
        visited[node] = True
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            for neighbor, weight in self.graph_adj_list[node]:
                if visited[neighbor] == False:
                    queue.append(neighbor)
                    visited[neighbor] = True


    def breadth_first_search(self, node):
        queue = []
        queue.append(node)
        visited = [False]*self.vertex_no
        visited[node] = True
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            for neibour_vertex, weight in self.graph_adj_list[node]:
                if visited[neibour_vertex] == False:
                    queue.append(neibour_vertex)
                    visited[neibour_vertex] = True

    def bfs_rec(self, node, queue, visited):
        if not queue:
            return
        node = queue.pop(0)
        print(node, end=" ")
        for neighbor, weight in self.graph_adj_list[node]:
            if visited[neighbor] == False:
                queue.append(neighbor)
                visited[neighbor] = True
        self.bfs_rec(node, queue, visited)

    def bfs(self, node):
        queue = []
        visited = [False]*self.vertex_no
        queue.append(node)
        visited[node] = True
        self.bfs_rec(node, queue, visited)

    def bfs_disconected(self):
        queue = []
        visited = [False]*self.vertex_no
        for node in self.graph_adj_list.keys():
            if visited[node] == False:
                queue.append(node)
                visited[node] = True
                self.bfs_rec(node, queue, visited)



g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.print_adj_list()
# g.print_vertex_bfs(3)
print()
# print(g.has_edge(1,3))
g.breadth_first_search(0)
print()
g.bfs_disconected()