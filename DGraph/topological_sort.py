class Graph:

    def __init__(self,no_vertices):
        self.graph = {k:[] for k in range(no_vertices)}
        self.no_vertices = no_vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,n,visited,stack):
        visited[n] = True
        for element in self.graph[n]:
            if visited[element] == False:
                self.dfs(element,visited,stack)
        stack.insert(0,n)

    def topologicalSort(self):
        visited = [False]*self.no_vertices
        stack =[]
        for element in range(self.no_vertices):
            if visited[element] == False:
                self.dfs(element,visited,stack)
        print(stack)

graph = Graph(5)
graph.addEdge(0,1);
graph.addEdge(0,3);
graph.addEdge(1,2);
graph.addEdge(2,3);
graph.addEdge(2,4);
graph.addEdge(3,4);

print("The Topological Sort Of The Graph Is:  ")

graph.topologicalSort()