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
        
t = Trie()
t.insert_word("the")
t.insert_word("tree") 
t.insert_word("art")
print(t.search_word("the"))
print(t.search_word("treuio"))
print(t.search_word("arte"))
