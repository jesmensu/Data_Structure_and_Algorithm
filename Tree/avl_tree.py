
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
        t = y.right
        root.left = t
        y.right = root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    
    def left_rotation(self, root):
        y = root.right
        t = y.left
        y.left = root
        root.right = t
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    
    def get_balance(self, root):
        balance = self.get_height(root.left) - self.get_height(root.right)
        return balance

    def get_min(self, temp_root):
        if temp_root.left == None:
            return temp_root
        else:
            min = self.get_min(temp_root.left)
            return min
        
    def rotate_for_balance(self, root, balance, data):
        # LL case Right rotation
        if balance>1 and data < root.left.data:
            return self.right_rotation(root)
        # RR case Left rotation
        elif balance<-1 and data > root.right.data:
            return self.left_rotation(root)
        # LR case Right rotation
        elif balance>1 and data > root.left.data:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        # RL case Left rotation
        elif balance<-1 and data < root.right.data:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)
        
    def rotate_for_balance_after_delete(self, root, balance):
        # LL case Right rotation
        if balance>1:
            # LL case
            if self.get_balance(root.left)>= 0:
                return self.right_rotation(root)
            # LR case
            else:
                root.left = self.right_rotation(root.left)
                return self.left_rotation(root)

        if balance < -1:
            # RR case
            if self.get_balance(root.right)<= 0:
                return self.left_rotation(root)
            # RL case
            else:
                root.right = self.left_rotation(root.right)
                return self.right_rotation(root)


    def insert_node(self, root , data):
        balance = 0
        if root == None:
            root = Node(data)
        else:
            if data<root.data:
                root.left = self.insert_node(root.left, data)
            elif data>root.data:
                root.right = self.insert_node(root.right, data)
            root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

            balance = self.get_height(root.left) - self.get_height(root.right)
            if balance < -1 or balance > 1:
                return self.rotate_for_balance(root, balance, data)
        return root
    
    def delete_node(self, node, key):
        if node == None:
            return node
        if key < node.data:
            node.left = self.delete_node(node.left, key)
        elif key > node.data:
            node.right = self.delete_node(node.right, key)
        else:
            if node.left == None and node.right == None: # if deleting node is leaf node
                return None
            elif node.left == None and node.right != None:  # if only right node exists
                temp = node.right
                node = None
                return temp
            elif node.left != None and node.right == None: # if only left node exists
                temp = node.left
                node = None
                return temp
            else:                                          # If both left node and right node exists
                node.data = self.get_min(node.right).data
                node.right = self.delete_node(node.right, node.data)
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
            balance = self.get_height(root.left) - self.get_height(root.right)
            if balance < -1 or balance > 1:
                return self.rotate_for_balance_after_delete(root, balance)
        return node

    def inorder_traverse(self, node):
        if node != None:
            self.inorder_traverse(node.left) 
            print(node.data)
            self.inorder_traverse(node.right)
        
avl = AVL()
root = avl.insert_node(None, 4)
root = avl.insert_node(root, 5)
root = avl.insert_node(root, 1)
root = avl.insert_node(root, 6)
root = avl.insert_node(root, 10)
root = avl.insert_node(root, 3)
root = avl.insert_node(root, 12)
root = avl.insert_node(root, 7)
root = avl.insert_node(root, 8)
root = avl.insert_node(root, 9)
root = avl.insert_node(root, 2)
root = avl.insert_node(root, 20)
avl.inorder_traverse(root)
root = avl.delete_node(root, 4)
avl.inorder_traverse(root)
