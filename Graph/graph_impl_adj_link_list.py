
class Node:
    def __init__(self, item = None):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self, item = None):
        self.head = Node(item)

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
        self.graph_adj_link_list = [LinkedList(k) for k in range(vertex_no)]

    def print_adj_list(self):
        for linklist in self.graph_adj_link_list:
            node = linklist.head
            while node != None:
                print(node.item, "-->", end="")
                node = node.next
            print("")

    def add_edge(self, u, v, weight = 7):
        for linklist in self.graph_adj_link_list:
            node = linklist.head
            if node.item == u:
                linklist.insert_at_end(v)
            if node.item == v:
                linklist.insert_at_end(u)
    
    def remove_edge(self, u, v):
        for linklist in self.graph_adj_link_list:
            node = linklist.head
            if node.item == u:
                current = node
                while current.next != None:
                    if current.next.item == v:
                        current.next = current.next.next
                        break
                    current = current.next
            if node.item == v:
                current = node
                while current.next != None:
                    if current.next.item == u:
                        current.next = current.next.next
                        break
                    current = current.next

    def has_edge(self, u, v):
        for linklist in self.graph_adj_link_list:
            node = linklist.head
            if node.item == u:
                current = node
                while current.next != None:
                    if current.next.item == v:
                        return True
                    current = current.next
                return False

g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
# g.remove_edge(1,3)
g.print_adj_list()
print(g.has_edge(0,3))
g.remove_edge(1,3)
print("After delete: ")
g.print_adj_list()