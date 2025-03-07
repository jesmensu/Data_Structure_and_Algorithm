class Graph:

    def __init__(self,no_vertices):
        self.graph = {k:[] for k in range(no_vertices)}
        self.no_vertices = no_vertices
        self.indegree = [0]*self.no_vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.indegree[v] += 1

    def dfs(self,n,visited,stack):
        visited[n] = True
        for element in self.graph[n]:
            if visited[element] == False:
                self.dfs(element,visited,stack)
        stack.append(n)

    def topological_sort_dfs(self):
        visited = [False]*self.no_vertices
        stack =[]
        for element in range(self.no_vertices):
            if visited[element] == False:
                self.dfs(element,visited,stack)
        print(stack[::-1])

    def topological_sort_bfs(self):
        # indegree = [0]*self.no_vertices
        # for key, val in self.graph.items():
        #     for v in val:
        #         indegree[v] += 1

        indegree = self.indegree
        queue =[]
        toposort = []
        for node in range(self.no_vertices):
            if indegree[node] == 0:
                queue.append(node)
        while(queue):
            node = queue.pop(0)
            toposort.append(node)
            for nbr in self.graph[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
        print(toposort)
    
graph = Graph(5)
graph.addEdge(0,1)
graph.addEdge(0,3)
# graph.addEdge(1,2)
# graph.addEdge(2,3)
# graph.addEdge(2,4)
graph.addEdge(3,4)

print("The Topological Sort Of The Graph Is:  ")

graph.topological_sort_dfs()
graph.topological_sort_bfs()