class Node:
    def __init__(self, item = None):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert_at_start(self, item):
        n = Node(item)
        if self.head != None:
            n.next = self.head
        self.head = n
        print("Item", item, "inserted at start")

    def insert_at_end(self, item):
        n = Node(item)
        if self.head == None:
            self.head = n
        else:
            current = self.head
            while(current.next != None): 
                current = current.next
            current.next = n

        print("Item", item, "inserted at end")

class Graph:
    def __init__(self, vertex_no) -> None:
        self.vertex_no = vertex_no
        self.graph_adj_link_list = {k: LinkedList() for k in range(vertex_no)}

    def print_adj_link_list(self):
        for key, linklist in self.graph_adj_link_list.items():
            node = linklist.head
            print(key, end="")
            while node != None:
                print("-->", node.item, end="")
                node = node.next
            print("")

    def add_edge(self, u, v, weight = 7):
        for key, linklist in self.graph_adj_link_list.items():
            node = linklist.head
            if key == u:
                linklist.insert_at_end(v)
            if key == v:
                linklist.insert_at_end(u)
    
    def print_vertex_bfs(self, node):
        visited = []
        queue = []

        queue.append(node)
        visited.append(node)
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            linklist = self.graph_adj_link_list[node]
            current = linklist.head
            while current != None:
                item = current.item
                if item not in visited:
                    queue.append(item)
                    visited.append(item)
                current = current.next

g = Graph(7)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(1,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.add_edge(5,6)
g.print_adj_link_list()
g.print_vertex_bfs(2)
# print(g.has_edge(1,3))