class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.index = 0

    def build_tree(self, nodes):
        if self.index < len(nodes):
            if nodes[self.index] == None:
                self.index += 1
                return None

            item = nodes[self.index]
            self.index += 1
            current = Node(item)
            current.left = self.build_tree(nodes)
            current.right = self.build_tree(nodes)
            return current

    def preorder_traverse(self, current):
        if current != None:
            print(current.data)
            self.preorder_traverse(current.left)
            self.preorder_traverse(current.right)
        else:
            print(None)

    def count_node(self, current):
        if current == None:
            return 0
        count_left = self.count_node(current.left)
        count_right = self.count_node(current.right)
        return count_left + count_right + 1
    
    def tree_height(self, current):
        if current == None:
            return 0
        height_left = self.tree_height(current.left)
        height_right = self.tree_height(current.right)
        return max(height_left, height_right) + 1
    
    def tree_sum(self, current):
        if current == None:
            return 0
        sum_left = self.tree_sum(current.left)
        sum_right = self.tree_sum(current.right)
        return sum_left + sum_right + current.data
    
    def leafSequence(self, root):
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [root.data]
        else:
            return self.leafSequence(root.left) + self.leafSequence(root.right)

        

b = BinaryTree()
# root = b.build_tree([1,2,4,None, None, 5,None,None, 6,7,None,None,None])
# b.preorder_traverse(root)
# print(b.count_node(root))
# print(b.tree_height(root))
# print(b.tree_sum(root))
root = b.build_tree([1,2,4])
print(b.leafSequence(root))



