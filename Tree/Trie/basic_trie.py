class Node:
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    def insert_word(self, word):
        current = self.root
        for ch in word:
            index = ord(ch) - ord("a")
            if current.children[index] == None:
                current.children[index] = Node()
            current = current.children[index]
        current.end_of_word = True

    def search_word(self, word):
        current = self.root
        for ch in word:
            index = ord(ch) - ord("a")
            if current.children[index] == None:
                return False
            current = current.children[index]
        else:
            if current.end_of_word == True:
                return True  
            else:
                return False 

    def count_word(self):
         count = 0
         current = self.root
         count = self.check_children(current, count)
         return count
    
    def check_children(self, current, count):
        children = current.children
        for i in range(26):
            if children[i] != None:
                if children[i].end_of_word == True:
                    count += 1
                count = self.check_children(children[i], count)

        return count

        
t = Trie()
t.insert_word("the")
t.insert_word("tree") 
t.insert_word("art")
print(t.count_word())
