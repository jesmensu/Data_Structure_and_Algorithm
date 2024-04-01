class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.size = 0

    def insert_to_bst(self, root:Node, data):
        current = root
        if current == None:
            n = Node(data)
            current = n
        else:
            if data< current.data:
                current.left = self.insert_to_bst(current.left,data)
            elif data> current.data:
                current.right = self.insert_to_bst(current.right,data)
        return current

    def build_bst(self, lst):
        root = Node(lst[0])
        for i in range(1,len(lst)):
            root = self.insert_to_bst(root, lst[i])
        return root
    
    def inorder_traverse(self, root:Node, ans:list):
        if root == None:
            return
        self.inorder_traverse(root.left, ans)
        ans.append(root.data)
        self.inorder_traverse(root.right, ans)
        return ans
    
    def merge_tree(self, tree1, tree2):
        ans1 = self.inorder_traverse(tree1, [])
        ans2 = self.inorder_traverse(tree2, [])
        print(ans1)
        print(ans2)
        ans = []
        i,j = 0,0
        while i < len(ans1) and j<len(ans2):
            if ans1[i]<ans2[j]:
                ans.append(ans1[i])
                i += 1
            else:
                ans.append(ans2[j])
                j += 1
        if i<len(ans1):
            ans.extend(ans1[i:])
        elif j<len(ans2):
            ans.extend(ans2[j:])
        root = None
        while ans:
            l = len(ans)
            mid = l//2
            root = self.insert_to_bst(root, ans[mid])
            ans.remove(ans[mid])
        print(self.inorder_traverse(root, []))
        




        
bst1 = BST()
lst1 = [25,30,6,22,12,80]
root1 = bst1.build_bst(lst1)
# ans1 = bst1.inorder_traverse(root1, [])
# print(ans1)

bst2 = BST()
lst2 = [50,13,60,23,31,18]
root2 = bst2.build_bst(lst2)
# ans2 = bst2.inorder_traverse(root2, [])
# print(ans2)

bst = BST()
bst.merge_tree(root1, root2)
        

