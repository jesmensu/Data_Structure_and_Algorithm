class DGraph:
    def __init__(self, nodes: list[list]):
        self.number_nodes = len(nodes)
        self.adj_matrix = nodes
        self.result = []
        self.out_degree = [row.count(1) for row in nodes]
        self.in_degree = []

    def depth_first_search(self, node):
        stack = []
        visited = [False]*self.number_nodes
        cycles = []
        stack.append(node)
        no_cycle = 0
        
        while stack:
            node = stack.pop()
            visited[node] = True
            cycles.append(node)
            print(node, "-->", end= " ")
            for i in range(len(self.adj_matrix[node])):
                if self.adj_matrix[node][i] == 1:
                    if visited[i] == True:
                        if i in cycles:
                            self.result.append(cycles[i+1:])

                            no_cycle += 1
                            del cycles[i+1:]
                            stack.append(i)
                            continue
                        else:
                            while self.out_degree[cycles[-1]]<2:
                                cycles.pop()
                            stack.append(cycles[-1])
                            continue
                else:
                    stack.append(i)

        print()
        print(no_cycle)

    def dfs(self,node,visited,path):
        visited[node] = True
        path.append(node)
        cycle = []

        for i in range(self.number_nodes):
            if self.adj_matrix[node][i] == 1:
                neighbor = i
                if neighbor in path:  # Cycle detected
                    idx = path.index(neighbor)
                    cycle = path[idx:]
                elif not visited[neighbor]:
                    cycle = self.dfs(neighbor, visited, path)
                
                if cycle:
                    break
        
        path.pop()
        return cycle

    def detect_cycle(self):
        visited = [False]*self.number_nodes
        cycles = []

        for node in range(self.number_nodes):
            if not visited[node]:
                cycle = self.dfs(node, visited, [])
                if cycle:
                    cycles.append(cycle)
    
        return cycles




lst= [[0,1,1,0,0,0,0],[0,0,1,1,0,0,1],[0,0,0,0,0,0,0],[0,0,0.0,1,1,0],[1,0,0,0,0,0,0],[0,0,0,0,1,0,0],[1,0,0,0,0,0,0]]
dg = DGraph(lst)

# dg.depth_first_search(0)
# print(dg.result)
print(dg.detect_cycle())
