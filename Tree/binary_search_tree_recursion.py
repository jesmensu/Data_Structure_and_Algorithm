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

    def search(self, data):
        return self.rec_search(self.root, data)
    
    def rec_search(self, node, data):
        if node == None or node.data == data:
            return node
        elif data < node.data:
            node = self.rec_search(node.left, data)
        else:
            node = self.rec_search(node.right, data)
        return node
            
    def preorder_traverse(self):
        self.rec_preorder_traverse(self.root)

    def rec_preorder_traverse(self, node):
        if node != None:
            print(node.data)
            self.rec_preorder_traverse(node.left)
            self.rec_preorder_traverse(node.right)

    def inorder_traverse(self):
        self.rec_inorder_traverse(self.root)

    def rec_inorder_traverse(self, node):
        if node != None:
            self.rec_inorder_traverse(node.left) 
            print(node.data)
            self.rec_inorder_traverse(node.right)
        

    def postorder_traverse(self):
        self.rec_postorder_traverse(self.root)

    def rec_postorder_traverse(self, node):
        if node != None:
            self.rec_postorder_traverse(node.left)
            self.rec_postorder_traverse(node.right)
            print(node.data)

    def getMin(self):
        print(self.get_min(self.root).data)
    def get_min(self, temp_root):
        if temp_root.left == None:
            return temp_root
        else:
            min = self.get_min(temp_root.left)
            return min
        
    def getMax(self):
        print(self.get_max(self.root).data)
    def get_max(self, temp_root):
        if temp_root.right == None:
            return temp_root
        else:
            max = self.get_max(temp_root.right)
            return max

    def delete_item(self, key):
        self.root = self.rec_delete(self.root, key)

    def rec_delete(self, node, key):
        if node == None:
            return node
        if key < node.data:
            node.left = self.rec_delete(node.left, key)
        elif key > node.data:
            node.right = self.rec_delete(node.right, key)
        else:
            if node.left == None:
                return node.right
            if node.right == None:
                return node.left
            node.data = self.get_min(node.right).data
            self.rec_delete(node.right, node.data)
        return node

    
    def delete(self,data):
        self.root=self.rdelete(self.root, data)
        print(data, "deleted")
    def rdelete(self, temp_root, data):
        if temp_root is None:
            return temp_root
        if data < temp_root.data:
            temp_root.left = self.rdelete(temp_root.left, data)
        elif data > temp_root.data:
            temp_root.right = self.rdelete(temp_root.right, data)
        else:
            if temp_root.right == None:
                return temp_root.left
            if temp_root.left == None:
                return temp_root.right
            temp_root.data = self.get_max(temp_root.left).data
            self.rdelete(temp_root.left, temp_root.data)
        return temp_root
        
    def find_pred(self, node, key):
        # pred = node
        if node != None:
            if key<node.data:
                node = self.find_pred(node.left, key)
            elif key>node.data:
                pred = node
                if node.right.left == None:
                    return pred
                node = self.find_pred(node.right, key)

            else:
                node = node.left
                if node != None:
                    pred = self.get_max(node)
        return pred
        
    def find_succ(self, node, key):
        pred = None
        succ = None
        if node.data == key:
            if node.left != None:
                node = node.left
                while(node.right != None):
                    node = node.right
                pred = node

            if node.right != None:
                node = node.right
                while(node.left != None):
                    node = node.left
                succ = node

        elif node.data < key:
            succ = node
            pred, succ = self.find_succ(node.right, key)

        else:
            pred = node
            pred, succ = self.find_succ(node.left, key)

        return pred, succ
    
    def get_pred_succ(self, data):
        pred = self.find_pred(self.root, data)
        print(pred.data)
       
t = Tree()
t.insert(20)
t.insert(10)
t.insert(40)
t.insert(30)
t.insert(50)
t.insert(80)
t.insert(100)
t.insert(70)
t.insert(45)
t.insert(47)

# t.preorder_traverse()
# t.inorder_traverse()
# t.postorder_traverse()
# t.get_pred_succ(50)
# t.getMin()
# t.getMax()
# t.get_pred_succ(50)
t.delete(50)
# t.inorder_traverse()
t.preorder_traverse()
