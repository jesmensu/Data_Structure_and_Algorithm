class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def insert_from_preorder(self, lst):
        stack = []
        self.root = Node(lst.pop(0))
        p = self.root
        for i in lst:
            node = Node(i)
            if i < p.data:
                p.left = node
                stack.append(p)
                p = p.left
            elif i> p.data:
                if stack:
                    if i< stack[-1].data:
                        p.right = node
                    else:
                        p = stack.pop()
                        p.right = node
                else:
                    p.right = node
                    p = p.right

    def inorder_traverse(self, node):
        if node != None:
            self.inorder_traverse(node.left) 
            print(node.data)
            self.inorder_traverse(node.right)

l = [20,10,40,30,50,45,47,80,70,100]
t = Tree()
t.insert_from_preorder(l)
t.inorder_traverse(t.root)