class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.rec_insert(self.root, data)

    def rec_insert(self, node, data):
        if node == None:
            n = Node(data, None, None)
            print("inserted data:", data)
            return n   
        if data<node.data:
            n= self.rec_insert(node.left, data)
            node.left =n
        elif data>node.data:
            n = self.rec_insert(node.right, data)
            node.right = n
        return node
    
    def search_items_range(self, x, y):
        result = []
        result = self.search_items_range_rec(self.root, x, y, result)
        return result
    
    def search_items_range_rec(self, root, x, y, result):
        if root == None:
            return result
        current = root
        if current.data< x:
            result = self.search_items_range_rec(current.right, x, y, result)
        if current.data> y:
            result = self.search_items_range_rec(current.left, x, y, result)
        if current.data >= x and current.data<=y:
            result.append(current.data)
            result = self.search_items_range_rec(current.left, x, current.data, result)
            result = self.search_items_range_rec(current.right, current.data, y, result)
        return result

    def search_items_range2(self, node, x, y):
        if node == None:
            return
        else:
            if x <= node.data <= y:
                print(node.data)
                self.search_items_range(node.right, x, y)
                self.search_items_range(node.left, x, y)
            elif node.data < x:
                self.search_items_range(node.right, x, y)
            elif node.data > y:
                self.search_items_range(node.left, x, y)


t = Tree()
t.insert(1)
t.insert(3)
t.insert(6)
t.insert(5)
t.insert(9)
t.insert(11)
print(t.search_items_range(4,7))