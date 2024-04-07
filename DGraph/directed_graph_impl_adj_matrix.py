class DGraph:
    def __init__(self, nodes: list[list]):
        self.number_nodes = len(nodes)
        self.adj_matrix = nodes
        self.result = []

    def depth_first_search(self, node):
        stack = []
        visited = []
        stack.append(node)
        visited.append(node)
        while stack:
            node = stack.pop()
            print(node, "-->", end= " ")
            for i in range(len(self.adj_matrix[node])):
                if self.adj_matrix[node][i] == 1 and i not in visited:
                        stack.append(i)
                        visited.append(i)
                    



lst= [[0,0,1,0,1],[0,0,0,1,0],[1,0,0.0,0],[0,0,0,0,0],[0,1,0,0,0]]
dg = DGraph(lst)

dg.depth_first_search(0)
