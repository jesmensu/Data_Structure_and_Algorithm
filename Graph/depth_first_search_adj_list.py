class Graph:
    def __init__(self, vertex_no) -> None:
        self.vertex_no = vertex_no
        self.graph_adj_list = {k:[] for k in range(vertex_no)}

    def print_adj_list(self):
        for i in self.graph_adj_list.items():
            print(i)

    def add_edge(self, u, v, weight = 7):
        self.graph_adj_list[u].append((v,weight))
        # self.graph_adj_list[v].append((u, weight))
    
    def has_edge(self, u, v):
        for vertex, weight in self.graph_adj_list[u]:
            if vertex == v:
                return True
        return False
    
    def print_vertex_dfs(self, node):
        visited = [False]*self.vertex_no
        stack = []

        stack.append(node)
        visited[node] = True
        while stack:
            node = stack.pop()
            print(node, end=" ")
            for neibour_vertex, weight in self.graph_adj_list[node]:
                if visited[neibour_vertex] == False:
                    stack.append(neibour_vertex)
                    visited[neibour_vertex] = True

    def dfs(self,n,visited,stack):
        visited[n] = True
        for element, weight in self.graph_adj_list[n]:
            if visited[element] == False:
                self.dfs(element,visited,stack)
        stack.insert(0,n)




g = Graph(7)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(1,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.add_edge(5,6)
g.print_adj_list()
g.print_vertex_dfs(0)
# print(g.has_edge(1,3))
visited = [False]*g.vertex_no
stack = []
g.dfs(0, visited, stack)
print(stack)
