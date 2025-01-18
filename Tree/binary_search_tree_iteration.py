class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        n = Node(data, None, None)
        if self.root == None:
            self.root = n
            print("inserted data:", data)
        else:
            prev = None
            current = self.root
            while (current != None):
                if data < current.data:
                    prev = current
                    current = current.left
                else:
                    prev = current
                    current = current.right
            if data < prev.data:
                prev.left = n
                print("inserted data:", data)
            else:
                prev.right = n
                print("inserted data:", data)

            
    def preorder_traverse(self):
        stack = []
        stack.append(self.root)
        while(stack):
            node = stack.pop()
            print(node.data)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)

    def inorder_traverse(self):
        stack = []
        current = self.root
        while(True):  
            if current != None:
                stack.append(current)
                current = current.left
            elif (stack):
                node = stack.pop()
                print(node.data)
                if node.right != None:
                    current = node.right
            else:
                break
 
    def postorder_traversal(self):
        stack = []
        result = []
        stack.append(self.root)
        while(stack):
            node = stack.pop()
            result.insert(0, node.data)
            if node.left != None:
                stack.append(node.left)
            if node.right != None:
                stack.append(node.right)
        
        print(result)

    def postorder_traverse(self):
        stack = []
        current = self.root
        while(True):  
            while current != None:
                stack.append(current)
                stack.append(current)
                current = current.left
            if (len(stack) == 0):
                return
            current = stack.pop()
    
            if (len(stack) > 0 and stack[-1] == current):
                current = current.right
            else:
                print(current.data, end=" ")
                current = None

    def get_succesor(self, node):
        curr = node.right
        prev = None
        while curr.left != None:
            prev = curr
            curr = curr.left
        if prev != None:
            prev.left = curr.right
            curr.right = None
        else:
            node.right = None
        return curr

    def get_predecessor(self, node):
        curr = node.left
        prev = None
        while curr.right != None:
            prev = curr
            curr = curr.right
        if prev != None:
            prev.right = curr.left
            curr.left = None
        else:
            node.left = None
        return curr
    
    def delete_item(self, key):
        curr = self.root
        prev = None
        # Find the node with key
        while (curr != None and curr.data != key):
            if key < curr.data:
                prev = curr
                curr = curr.left
            elif key > curr.data:
                prev = curr
                curr = curr.right
            else:
                break

        # replace the node with succ or pred
        targ_node = None
        if curr != None:
            if curr.right != None:
                targ_node = self.get_succesor(curr)
            elif curr.left != None:
                targ_node = self.get_predecessor(curr)
            if targ_node != None:
                targ_node.right = curr.right
                targ_node.left = curr.left

            if prev == None:
                self.root = targ_node
            elif prev.left == curr:
                prev.left = targ_node
            else:
                prev.right = targ_node

    def deleteIterative(self, key):
        curr = self.root
        prev = None
        while(curr != None and curr.data != key):
            prev = curr
            if curr.data < key:
                curr = curr.right
            else:
                curr = curr.left
        if curr == None:
            print("Key % d not found in the provided BST." % key)
            return self.root

        if curr.left == None or curr.right == None:
            newCurr = None
            if curr.left == None:
                newCurr = curr.right
            else:
                newCurr = curr.left
    
            # check if the node to
            # be deleted is the root.
            if prev == None:
                return newCurr
    
            # Check if the node to be
            # deleted is prev's left or
            # right child and then
            # replace this with newCurr
            if curr == prev.left:
                prev.left = newCurr
            else:
                prev.right = newCurr
    
            curr = None
    
        # node to be deleted
        # has two children.
        else:
            p = None
            temp = None
    
            # Compute the inorder
            # successor of curr.
            temp = curr.right
            while(temp.left != None):
                p = temp
                temp = temp.left
    
            # check if the parent of the
            # inorder successor is the root or not.
            # if it isn't, then make the left
            # child of its parent equal to the
            # inorder successor's right child.
            if p != None:
                p.left = temp.right
    
            else:
                curr.right = temp.right
    
            curr.data = temp.data
            temp = None
    
        return self.root

    def build_tree(self, nodes):
        pass
            
        
t = Tree()
t.insert(20)
t.insert(10)
t.insert(40)
t.insert(30)
t.insert(50)
t.insert(80)
t.insert(100)
t.insert(70)
t.deleteIterative(20)

# t.preorder_traverse()
t.inorder_traverse()
# t.postorder_traverse()