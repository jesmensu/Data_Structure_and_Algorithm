
class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

class AVL:
    def __init__(self):
        pass

    def get_height(self, root):
        if root == None:
            return -1
        else:
            return root.height
    
    def right_rotation(self, root):
        y = root.left
        temp = y.right
        root.left = temp
        y.right = root
        return y
    
    def left_rotation(self, root):
        y = root.right
        temp = y.left
        root.right = temp
        y.left = root
        return y
    
    def rotate_for_balance(self, root, balance, data):
        # if balance is >1, LL case Right rotation
        if balance>1 and data < root.left.data:
            self.right_rotation(root)
        # if balance is <-1, RR case Left rotation
        if balance<-1 and data > root.right.data:
            self.left_rotation(root)
        # if balance is >1, LR case Right rotation
        if balance>1 and data > root.left.data:
            root.left = self.left_rotation(root.left)
            self.right_rotation(root)
        # if balance is <-1, RL case Left rotation
        if balance<-1 and data < root.right.data:
            root.right = self.right_rotation(root.right)
            self.left_rotation(root)


    def insert_node(self, root , data):
        if root == None:
            root = Node(data)
        else:
            if data<root.data:
                root.left = self.insert_node(root.left, data)
            elif data>root.data:
                root.right = self.insert_node(root.right, data)
            root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
            balance = self.get_height(root.left) - self.get_height(root.right)
        self.rotate_for_balance(root, balance)
        return root
        
avl = AVL()
root = avl.insert_node(None, 4)
root = avl.insert_node(root, 5)
root = avl.insert_node(root, 1)
root = avl.insert_node(root, 6)
root = avl.insert_node(root, 10)
root = avl.insert_node(root, 3)